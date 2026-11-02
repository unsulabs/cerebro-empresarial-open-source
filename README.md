# Cerebro Empresarial para empresas y emprendedores de México

**Versión 0.4.0-rc.1 — candidato público para instalación y pilotos.** Las pruebas automatizadas no sustituyen la comprobación de Obsidian ni la revisión empresarial de cada bóveda.

Una persona que dirige una micro, pequeña o mediana empresa puede entregar este repositorio a **Codex** para preparar una bóveda empresarial en **Obsidian** y comenzar a **crear, recuperar, mejorar, vincular y usar conocimiento real de su empresa**. También se puede trabajar con otros asistentes compatibles mediante instrucciones portables; no se presupone que cualquier chat pueda ejecutar comandos o leer archivos locales.

Este repositorio público contiene el producto general, metodología, plantillas y ejemplos ficticios. Las bóvedas empresariales se crean fuera del checkout y permanecen privadas. Ninguna operación instala plugins comunitarios automáticamente.

## Para empezar (sin experiencia técnica)

1. Clona `https://github.com/unsulabs/cerebro-empresarial-open-source.git` y abre esa carpeta en Codex en la computadora donde usarás Obsidian. Conserva `.agents/` y `plantilla_boveda/.obsidian/`.
2. Comprueba Python 3.10 o posterior y Obsidian Desktop. Las dependencias Python están en `requirements.txt`; solicita autorización antes de instalarlas.
3. Copia el texto de **[PROMPT_INICIO_CODEX.md](PROMPT_INICIO_CODEX.md)**. Codex debe leer `AGENTS.md` y seguir la skill de instalación.
4. Autoriza selectivamente instalaciones y escrituras. El asistente verifica Obsidian (GUI, versión, Bases), prepara tu bóveda privada y empieza con el descubrimiento empresarial.
5. Continúa desde la primera unidad hacia tareas reales, correcciones y recuperación en otra sesión. Una primera nota no equivale a una empresa construida ni a un sistema aceptado.

[Guía completa de primera instalación y construcción](guia/PRIMERA_EMPRESA_CON_CODEX.md) · [Manual de mejora del repositorio](guia/EVOLUCION_PARA_CODEX.md)

En macOS o Linux, para preparar Python sin instalar paquetes globales:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/cerebro.py doctor
python -m unittest discover -s tests -q
```

En Windows, activa el entorno virtual con `.venv\Scripts\Activate.ps1`. Obsidian Desktop debe instalarse desde su fuente oficial; Codex comprueba la versión y las funciones nativas en la computadora de destino. La CLI de Obsidian es opcional para el flujo básico.

Para distribuir una versión fijada del producto, ejecuta `python3 scripts/exportar_producto.py --dest /ruta/privada/cerebro-producto.zip` desde un checkout Git limpio. El ZIP incluye un manifiesto de tamaño y SHA-256 y excluye rutas reservadas para datos privados.

## Continuar una empresa instalada: GitHub + Codex + bóveda

No vuelvas a ejecutar crear si la bóveda ya existe. Actualizar GitHub no cambia la versión ni los archivos del empresario. En el checkout limpio y actualizado, sigue [aceptación real de una instancia existente](guia/ACEPTACION_REAL_CODEX_INSTANCIA_EXISTENTE.md) y [prompt específico para Codex](PROMPT_RECUPERAR_EMPRESA_EXISTENTE_CODEX.md) y ejecuta el diagnóstico en modo sólo lectura:

    python3 scripts/aceptacion_integracion_local.py --vault "RUTA_PRIVADA_BOVEDA" --salida "CARPETA_NUEVA_EXTERNA" --commit-esperado SHA_MAIN_CONFIRMADO

El informe comprimido es **saneado**: resumen, recuentos, hashes, estados y fallas, pero no fuentes, notas ni rutas privadas. Codex debe validar aparte la GUI de Obsidian, una segunda sesión autónoma y restauración de punta a punta. Si aparece una falla, no tocar D01 ni las Bases para esconderla: reparar GitHub y repetir la prueba. Migrar o publicar mapas necesita autorización distinta.

## Funciones técnicas disponibles

```bash
python3 -m pip install -r requirements.txt
python3 scripts/cerebro.py doctor
python3 -m unittest discover -s tests -v

# Crear una empresa ficticia como ejemplo (elige una ruta PRIVADA)
python3 scripts/cerebro.py crear --id EMPRESA-FICTICIA --nombre "Empresa de prueba" --dest /ruta/privada/demo
python3 scripts/cerebro.py validar --vault /ruta/privada/demo
python3 scripts/cerebro.py tipos --tipo consultoria

# Registrar referencias, no el contenido privado de fuentes
python3 scripts/cerebro.py fuente --vault /ruta/privada/demo --id F-DEMO-001 --titulo "Fuente ficticia" --localizador "urn:synthetic:demo" --clase "ejemplo" 
python3 scripts/cerebro.py estado --vault /ruta/privada/demo

# Sólo después de que Codex prepare un JSON y un Markdown privados y autorizados:
# python3 scripts/cerebro.py plan-conocimiento --vault /ruta/privada/demo --archivo /ruta/privada/plan.json
# python3 scripts/cerebro.py ficha --vault /ruta/privada/demo --tipo oferta --titulo "Oferta en estudio" --archivo /ruta/privada/oferta.md --etiqueta comercial/ofertas --fuente F-DEMO-001
# python3 scripts/cerebro.py mapa-conocimiento --vault /ruta/privada/demo
```

Comandos adicionales: `mapa-conocimiento` (previsualizar Markdown + Canvas derivados, sin escribir), `publicar-mapa` (autorización SHA y respaldo externo), `plan-conocimiento` (plan de notas y relaciones ANTES de escribir, solo lectura), `consulta-contextual` (literal por bloques con fuente, ámbito, fecha y autoridad sin inferencia), `capturar`, `documento` (D/X en borrador), `previsualizar-dx`, `preparar-dx`, `aplicar-dx`, `restaurar-dx`, `evaluar-dx`, `aprobar-dx` (exige decisión explícita y gates), `relacion-proponer`, `relacion-confirmar`, `relaciones`, `aceptacion`, `buscar` (literal), `autoridad`, `importar`, `grafo`, `proponer`, `continuidad`, `validar`, `tipos`. Comprobar flags con `python3 scripts/cerebro.py --help`. **No autorizar cambios en una bóveda real por el simple hecho de disponer de estos comandos.**

## Construir una empresa completa

Tras crear o recuperar una bóveda, Codex activa [flujo de empresa completa](docs/FLUJO_EMPRESA_COMPLETA.md) y la skill `ce-desarrollo-empresa`: mapa de cobertura D01–D07 por tareas, fuentes, primera pieza útil, prueba de uso y correcciones que otra sesión pueda recuperar. Para demanda, marca y contenido sigue [marketing empresarial](docs/MARKETING_EMPRESARIAL.md), conectado a oferta, entrega, economía y permisos. No presupone publicaciones diarias ni activa tareas programadas o memoria automática.

## Qué incluye

- **Metodología empresarial real**: versión vNext-1.0R completa en Markdown, 7 familias D01–D07 y 7 expedientes condicionales X01–X07, prompts adaptativos, metodología K1–K4 y gates G1–G7. **No son 14 archivos obligatorios por empresa.**
- **Conocimiento conectado**: contrato portable vNext-0.9, esquema, validador y herramienta para importar un paquete verificado, más fuente, autoridad, vigencia, bloque e histórico.
- **Bóveda de Obsidian**: Inicio, mapas, plantillas de clases empresariales, 27 tipos de entidad diferenciados, 16 vistas `.base` para funciones empresariales y fuentes. Bases es nativo; se comprueba su versión al instalar.
- **Operación con Codex**: `AGENTS.md`, 12 skills con disparadores, pasos, comprobaciones y límites. CLI local seguro para crear/registrar/proponer/consultar/continuar.
- **Investigación reutilizada**: cinco videos (hallazgos con timestamps, sin redistribuir transcripciones de terceros), expediente de consolidación D0.1, comparación de plugins y trazabilidad.
- **Pruebas y ejemplo**: paquete vNext sintético, suite de regresión local y demo reproducible.

## Reglas que hacen útil el sistema

Una oferta ≠ servicio ≠ consultoría ≠ herramienta usada. Proyecto ≠ caso ≠ reunión. Persona ≠ cliente ≠ organización. Propuesta ≠ contrato. Cotizado ≠ cobrado. Los tipos se crean solo cuando necesitan identidad independiente y son **candidatos** que evolucionarán con pilotos, no una taxonomía sagrada.

El sistema construye una **red de notas especializadas conectadas**, sin exigir que D01 contenga todo. Las 16 vistas Bases son una perspectiva sobre las propiedades de esas notas y el Markdown/Canvas derivado permite recorrer relaciones tipadas. El mapa NO es fuente de verdad; se actualiza sólo tras nueva previsualización y autorización.

Las notas nuevas tienen [nombres visibles por asunto](docs/NOMBRES_LEGIBLES.md); los IDs técnicos permanecen en propiedades. Una bóveda existente puede preparar un plan de renombrado con respaldo externo sin cambiar su conocimiento editorial.

El sistema ayuda a **desarrollar conocimiento**, no solo guardarlo. Primero recupera fuentes y criterio del dueño; **antes de redactar D01 o cualquier otra nota multiasunto, propone la arquitectura del conocimiento**, con un dueño canónico por asunto, notas existentes/nuevas/no creadas y enlaces. Después desarrolla las piezas especializadas y las somete a pruebas de utilidad. Consultar [arquitectura antes de redactar](docs/ARQUITECTURA_CONOCIMIENTO_ANTES_DE_REDACTAR.md).

## Contrato de arquitectura para cualquier empresa

[Especificación de red de conocimiento v0.4](docs/ESPECIFICACION_RED_CONOCIMIENTO_V0_4.md) · [Planificación antes de redactar](docs/ARQUITECTURA_CONOCIMIENTO_ANTES_DE_REDACTAR.md). El software no presupone moneda, organigrama ni una cantidad fija de notas. Cada empresa conserva sus fuentes y documentos fuera de Git.

La CLI permite una previsualización sin escritura del mapa navegable. Codex debe seguir el orden **fuentes → plan → revisión humana → notas con contenido → relaciones → consultas → mapa**. No copiar plantillas sobre bóvedas existentes.

## Mantenimiento de vistas Bases

Si las vistas muestran plantillas como registros empresariales, consulta [actualización segura](docs/BASES_FILTROS_Y_ACTUALIZACION.md). El actualizador exige aprobación y respaldo y no sobrescribe personalizaciones.

## Limitaciones comprobables

- **Sí probado localmente**: creación no destructiva, fichas, fuentes, estados, propuestas, continuidad, validación de IDs/enlaces, importación sintética vNext, grafo declarado y pruebas unitarias.
- **Observación local**: Obsidian 1.14.5, Bases y CLI funcionaron en una Mac de desarrollo. Cada instalación nueva debe comprobar su propia GUI, permisos y recuperación de conocimiento.
- **No implementado**: ACL multiusuario en Obsidian, actualización automática de datos oficiales, aprobación semántica autónoma, sincronización bidireccional con ERP/CRM/Drive ni inferencia semántica automática. La aprobación editorial es un registro de decisión declarada y no prueba identidad humana; las revisiones sólo deben aplicarse con autorización real.

Para mejorar sin perder dirección: [HOJA_DE_RUTA](docs/HOJA_DE_RUTA.md), [CRITERIOS_DE_ACEPTACION](docs/CRITERIOS_DE_ACEPTACION.md) y [DECISIONES_ABIERTAS](docs/DECISIONES_ABIERTAS.md).

**Licencia:** [MIT](LICENSE), autorizada por el propietario para este producto público. Los recursos de terceros se referencian y no se instalan por defecto. Ver [FUENTES_Y_LICENCIAS](docs/FUENTES_Y_LICENCIAS.md).

## Reparación de instalaciones 0.2 existentes en macOS

El producto admite los aliases nativos macOS `/tmp` y `/var`
comprobando `readlink` y destino físico, sin permitir symlinks de usuario.
La aceptación del cambio se ejecuta localmente en la Mac con Python 3.11 y temporal normal; consulta `docs/COMPATIBILIDAD_MACOS_RUTAS.md`. Se retiró el workflow de GitHub Actions: los runners de la cuenta no iniciaban y no forman parte del gate vigente.

Si Obsidian reserializó las Bases al abrirlas, primero cierra la GUI;
consulta `docs/BASES_FILTROS_Y_ACTUALIZACION.md` y ejecuta la
migración controlada con `--sha-plan`, respaldo privado de las 16 Bases
y workspace.json. Tras la migración valida la interfaz y las consultas.
No se cambian documentos de empresa ni se crean notas por actualizar el código.
