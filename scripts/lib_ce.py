"""Funciones compartidas: el YAML contiene metadatos, no determina verdad de negocio."""
from __future__ import annotations
import re
import unicodedata
from pathlib import Path
import yaml

WIKI_RE = re.compile(r'!?\[\[([^\]]+)\]\]')
BLOCK_RE = re.compile(r'<!--\s*kb:id=([^\s]+)\s*-->')
EDITORIAL = {"borrador", "en_revision", "aprobado", "retirado"}
TEMPORAL = {"vigente", "futuro", "superseded", "caducado", "sin_verificar"}
SENSITIVITY = {"interno", "confidencial", "restringido"}
KNOWLEDGE = {"hecho_observado", "decision_aprobada", "propuesta", "hipotesis", "historico", "pendiente", "desconocido", "conflicto"}
COVERAGE = {"sin_fuente", "parcial", "suficiente_para_tarea", "no_aplica"}


TAG_RE = re.compile(r"^[a-z][a-z0-9-]*(?:/[a-z][a-z0-9-]*){0,2}$")


def validate_tags(tags: list[str] | None) -> list[str]:
    """Etiquetas son navegación temática; NO son identidad ni autoridad."""
    if tags is None:
        return []
    if not isinstance(tags, list) or len(tags)>5:
        raise ValueError("Máximo cinco etiquetas temáticas por nota")
    if any(not isinstance(t,str) or not TAG_RE.fullmatch(t) for t in tags) or len(set(tags))!=len(tags):
        raise ValueError("Etiquetas inválidas o duplicadas; usar minúsculas, guiones y /")
    return list(tags)


def split_frontmatter(text: str) -> tuple[dict, str]:
    """Conserva el cuerpo Markdown intacto; solo administra YAML de cabecera."""
    if not text.startswith('---\n'):
        return {}, text
    match = re.match(r'\A---\n(.*?)\n---\n', text, re.DOTALL)
    if not match:
        raise ValueError('Encabezado YAML inicial no cerrado')
    raw = yaml.safe_load(match.group(1)) or {}
    if not isinstance(raw, dict):
        raise ValueError('El YAML de propiedades debe ser un objeto plano')
    return raw, text[match.end():]


def make_note(front: dict, body: str) -> str:
    fm = yaml.safe_dump(front, allow_unicode=True, sort_keys=False, default_flow_style=False, width=1000)
    return f'---\n{fm}---\n{body.lstrip(chr(10))}'


def visible_filename(title: str) -> str:
    """Nombre humano de archivo; el ID estable vive en el frontmatter.

    No agrega sufijos técnicos para resolver colisiones: el creador debe
    elegir un asunto distinguible y la operación debe fallar sin sobrescribir.
    """
    name = unicodedata.normalize('NFC', title).strip()
    name = re.sub(r'\s+', ' ', name)
    name = re.sub(r'[\\/:*?"<>|\[\]#]', ' ', name)
    name = re.sub(r'\s+', ' ', name).strip(' .')
    if not name or name in {'.', '..'} or len(name) > 100:
        raise ValueError('El título no produce un nombre legible (máximo 100 caracteres)')
    if re.fullmatch(r'(?:D\d{2}|X\d{2}(?:[-_][A-Za-z0-9]+)*|CAP-[A-Za-z0-9]+|SES-[A-Za-z0-9]+|F-[A-Za-z0-9_-]+)', name, re.IGNORECASE):
        raise ValueError('El nombre visible necesita palabras que describan el asunto')
    return name + '.md'


def path_by_id(vault: Path, note_id: str) -> Path | None:
    """Resolver identidad sin inferir rutas a partir de códigos."""
    found = []
    for p in notes_in_vault(vault):
        fm, _ = split_frontmatter(p.read_text(encoding='utf8'))
        if str(fm.get('id') or '') == note_id:
            found.append(p)
    if len(found) > 1:
        raise ValueError('ID duplicado: ' + note_id)
    return found[0] if found else None


def notes_in_vault(vault: Path) -> list[Path]:
    return sorted(p for p in vault.rglob('*.md') if 'Plantillas' not in p.parts and '.obsidian' not in p.parts)


def wiki_targets(text: str) -> list[str]:
    output = []
    for m in WIKI_RE.finditer(text):
        dest = m.group(1).split('|', 1)[0].split('#', 1)[0].strip()
        if dest: output.append(dest.removesuffix('.md'))
    return output


def target_index(vault: Path) -> tuple[dict[str, Path], dict[str, list[Path]]]:
    paths, names = {}, {}
    for p in notes_in_vault(vault):
        relative = str(p.relative_to(vault).with_suffix('')).replace('\\', '/')
        paths[relative] = p
        names.setdefault(p.stem, []).append(p)
    return paths, names


def resolve_link(target: str, paths: dict, names: dict) -> Path | None:
    clean = target.lstrip('/')
    if clean in paths: return paths[clean]
    candidates = names.get(Path(clean).name, [])
    return candidates[0] if len(candidates) == 1 else None
