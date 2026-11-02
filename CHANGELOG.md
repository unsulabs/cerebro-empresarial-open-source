# Cambios

## 0.4.0-rc.1 — red de conocimiento y navegación derivada (PILOTO)

- El flujo de Codex planifica notas autónomas, existentes y referencias antes de redactar D/X; evita duplicaciones y documentos monolíticos sin justificar.
- plan-conocimiento: repara clases X01–X07, duplicidad potencial por título, Dnn existente aunque el ID YAML difiera, extremos no-creados y avisos artificiales en empresas con un solo asunto.
- Ofertas nuevas ya no asumen MXN: moneda por_definir hasta que la persona responsable la determine.
- mapa-conocimiento: índice Markdown y Canvas nativo de Obsidian derivados de notas, etiquetas y vínculos tipados, con estados declarados y exclusión de restringidos.
- publicar-mapa: escritura opcional limitada a mapas generados, con SHA confirmado, respaldo externo privado, bloqueo de concurrentes y restauración ante fallo. No reescribe notas ni establece autoridad.
- Las 16 vistas Bases existentes se conservan. Sin migración automática de bóvedas, ni plugins comunitarios.
- Suite sintética y aceptación de instalación en Mac/Obsidian y segunda computadora pendientes por separado.


## 0.3.0-rc.1 — candidato de piloto controlado (NO producción multiempresa)

- Conserva vNext-1.0R y contrato 0.9 sin reescribir sus especificaciones originales.
- Excluye el legado empresarial editorialmente rechazado e incorpora reglas de reconstrucción desde fuentes originales.
- Corrige 16 Bases para no mostrar plantillas como registros; incorpora un migrador específico con diagnóstico y respaldo.
- Introduce capturas de descubrimiento, creación D/X con unicidad e inventario de conocimiento por capas.
- Corrige la continuidad reciente por hora con zona y añade pruebas para sesiones del mismo día.
- Incorpora revisión D/X no destructiva, historial, restauración, evaluación G1–G7 y promoción editorial sólo con cobertura suficiente y autorización explícita.
- Registra relaciones tipadas propuestas/ratificadas con ID, ámbito y fuente; el grafo distingue las dos capas.
- Añade preflight `aceptacion` que separa estructura de GUI, revisión humana y pruebas semánticas.
- Las pruebas GitHub Actions validan Python 3.10, 3.12 y 3.13. Falta la aceptación local en Obsidian, segunda computadora y revisión de permisos reales.
- Se conserva `RELEASE_MANIFEST.json` 0.2.0-alpha como baseline histórico utilizado por la migración de Bases.


## Corrección de CI posterior al primer commit

- La auditoría preventiva omite la carpeta `.git` del checkout, que nunca forma parte del paquete distribuido.
- La prueba de continuidad normaliza rutas temporales antes de compararlas en macOS.

## 0.2.0-alpha — primera entrega para GitHub privado

- Conserva el prototipo v0.1 y la metodología empresarial vNext-1.0R completa.
- Añade catálogo operativo candidato de 27 tipos con distinciones, relaciones y preguntas de prueba.
- Añade plantillas adaptativas para 14 clases D/X y 27 entidades, 12 vistas Bases nuevas, onboarding Codex y 10 skills.
- Añade CLI consolidada `scripts/cerebro.py` y diagnóstico sin dependencias, fichas, fuentes, búsqueda literal, consulta de autoridad, bandeja de propuestas, continuidad y estados.
- Importador preserva fuentes, IDs, bloques y autoridades, y usa staging/rollback para aplicación local de traspaso.
- Amplía pruebas automatizadas, ejemplos sintéticos, documentación y CI.
- Candidaturas pendientes: migraciones, permisos multiusuario, consulta semántica validada, aplicación de cambios e integraciones externas.

## 0.1.0 — prototipo previo

- Bóveda base, importación de contrato 0.9, exportación de grafo, validador y ocho pruebas originales.
