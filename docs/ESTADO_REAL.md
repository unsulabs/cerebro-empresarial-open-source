# Estado del producto público — 0.4.0-rc.1

Este repositorio contiene el producto general de Cerebro Empresarial: metodología vNext-1.0R, contrato vNext-0.9, instrucciones para Codex, CLI Python, plantilla de bóveda Obsidian, 16 Bases y ejemplos ficticios. Las bóvedas de empresas y sus fuentes originales se guardan fuera de Git.

## Implementado

- Diagnóstico e instalación no destructiva de una bóveda nueva; lectura estructural de una instancia existente.
- Fuentes, capturas provisionales, documentos D/X, revisión con historial y respaldo, relaciones tipadas, consultas literales con contexto, continuidad y mapas Markdown/Canvas derivados.
- Exportación de un ZIP de producto con manifiesto y exclusión de rutas privadas.
- Suite automatizada y ejemplos sintéticos. Las pruebas de la versión publicada deben ejecutarse en el checkout exacto; un resultado de otra versión no certifica ésta.

## Límites

- La CLI no autentica por sí misma la identidad de quien aprueba una nota, ni proporciona ACL multiusuario para una bóveda compartida.
- La búsqueda contextual es literal; el agente debe leer fuentes y evaluar significado, autoridad y vigencia. Un PASS estructural no aprueba conocimiento empresarial.
- La instalación de Obsidian Desktop, sus funciones nativas y permisos se comprueba en cada computadora. No se instalan plugins comunitarios automáticamente.
- No hay migrador general de esquema para cualquier versión anterior. Para una bóveda existente, seguir [actualizaciones y rollback](ACTUALIZACIONES_Y_ROLLBACK.md) y probar en copia aislada.
- El programa no integra automáticamente ERP, CRM ni cuentas empresariales. No expone una aplicación web multiusuario.

## Comprobación recomendada

Ejecutar `python3 -m unittest discover -s tests -q`; luego crear una empresa ficticia fuera del repositorio y correr `validar`. En una instalación real, comprobar Obsidian GUI, Inicio, Bases, fuentes, una tarea empresarial y su recuperación en otra sesión. Registrar por separado lo probado técnicamente y lo revisado por la persona propietaria.
