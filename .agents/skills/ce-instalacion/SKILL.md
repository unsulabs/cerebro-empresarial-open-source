---
name: ce-instalacion
description: "Instalar y configurar por primera vez el Cerebro Empresarial con Codex. Activar cuando una persona pida instalar, iniciar, configurar o continuar primera instalación de Obsidian/empresa."
---

# ce-instalacion

**0. Bifurcación antes de instalar:** comprobar si el usuario ya dispone de bóveda con 90_Sistema/config_empresa.yaml y D/X o fuentes. Si existe, **no crear otra ni reinstalar**: activar la guía guia/ACEPTACION_REAL_CODEX_INSTANCIA_EXISTENTE.md, comprobar el checkout sin destruir cambios y ejecutar aceptación_integracion_local en sólo lectura. Actualizar código no modifica la instancia; migraciones requieren autorización adicional.

1. Lee `guia/PRIMERA_EMPRESA_CON_CODEX.md` C0–C2; verifica root de repo y no confunde master con instancia.
2. Diagnóstico SOLO LECTURA: `python3 scripts/cerebro.py doctor` y versión de Obsidian verificada por GUI/CLI si disponible; no confiar en una ruta como prueba de funcionamiento.
3. Comunica requisitos e impedimentos reales. La petición expresa de instalar y construir la empresa autoriza las operaciones necesarias dentro de la ubicación elegida; no repitas permisos ya otorgados. Consulta antes de publicar datos, enviar mensajes, instalar plugins externos o usar otra cuenta. No instales `obsidian-projects` (archivado) ni TaskNotes automáticamente. Bases y Templates nativos primero.
4. Instala dependencias Python en venv si el encargo ya lo autoriza y usa `python -m unittest discover -s tests -v`. Si no hay internet, no inventes instalación.
5. Obtén nombre y destino privado sólo si no están en el contexto y no hay instancia existente; genera ID estable. `scripts/cerebro.py crear` falla si existe destino. Nunca copiar `ejemplos` ni datos de otra empresa a una instancia real.
6. Comprueba `validar` en CLI, abre como bóveda existente en Obsidian si la GUI es accesible, observa `Inicio.md` y alguna vista `.base`. Si este entorno usa `obsidian-router`, **termina el registro antes de pasar a descubrimiento**: después de abrir la carpeta en Obsidian, ejecuta `python3 scripts/registrar_boveda_codex.py --vault RUTA --nombre "Nombre" --alias ID_EMPRESARIAL`, seguido del resolver de `obsidian-router --selector RUTA`. El script sólo escribe el registro local de Codex, con respaldo; nunca altera el registro nativo ni la bóveda. Si la GUI no está disponible o el router no confirma la ruta, marca esa integración `NO VERIFICADO`, conserva la instancia y explica el impedimento concreto. No pidas al dueño que edite JSON.
7. Reporta seis superficies por separado: código, Python, Obsidian GUI, Bases, instancia privada, fuentes/conectores. Marca `NO VERIFICADO` cuando proceda. Continúa con `ce-descubrimiento` y `ce-arquitectura-conocimiento` cuando haya varios asuntos. No cierres el encargo por instalar: produce conocimiento utilizable y prueba una tarea con `ce-consulta`.
**Prohibido:** instalar plugins externos sin consentimiento; cambiar modo de seguridad de Obsidian sin explicar; subir datos empresariales a Git sin autorización expresa; declarar cerebro completo por pasar unittest.
