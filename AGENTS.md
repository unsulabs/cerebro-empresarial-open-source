# Cerebro Empresarial — contrato de Codex

Este es **el repositorio maestro del producto**. El objetivo es un segundo cerebro operativo para quien dirige una empresa mexicana: recuperar cómo trabaja y decide, convertir sus patrones en conocimiento que pueda usar y transferir a personas o agentes, y mantenerlo al día con cada conversación, archivo, cliente, decisión o trabajo nuevo. Si pide «instala y construye mi empresa», activa `.agents/skills/ce-desarrollo-empresa/SKILL.md` como orquestador: llama a `ce-instalacion`, `ce-descubrimiento` y `guia/PRIMERA_EMPRESA_CON_CODEX.md` según corresponda, y continúa hasta desarrollar y usar conocimiento con el dueño. Para una instancia existente, el orquestador entra por `ce-continuidad` sin repetir instalación; para una tarea concreta, activa `ce-consulta`. Ni instalación ni captura provisional cierran el encargo integral.

Si el dueño pide **terminar primero el sistema general**, trabaja sobre el producto y copias aisladas: reproduce fallas, corrige código/instrucciones, ejecuta suite e instalación sintética, inspecciona el exportado sin datos privados y documenta los gates que requieren Obsidian o una sesión independiente. Nunca uses la bóveda de una empresa como plantilla ni reemplaces su instancia activa. Sólo después de tener un candidato técnico verificable se instala y prueba con una empresa autorizada. El conocimiento empresarial debe poder leerse y corregirse como texto útil para personas, y mantenerse en Obsidian en el mismo ciclo; no exige una fase documental separada.

**Separación de datos:** este repositorio público no contiene bóvedas ni originales empresariales. Cada empresa conserva su conocimiento fuera de Git. No publiques fuentes, datos personales, secretos ni copias de bóvedas sin autorización específica.

## Dos entradas distintas: instancia NUEVA vs EXISTENTE

Si una tarea nombra una bóveda existente, resuélvela primero con `obsidian-router` y confirma la ruta, el registro nativo y sus instrucciones locales **antes de listar, buscar o leer cualquier archivo dentro de ella**. Una ruta escrita en el prompt indica la candidata, pero no reemplaza la comprobación del destino. Después de resolverla, carga `Como_usar` e `Inicio`; no selecciones por la ventana activa.

Cuando la persona diga "continúa mi empresa", "recupera mi bóveda" o se identifique una instancia privada que ya contiene D/X y fuentes, **NO ejecutar crear, copiar la plantilla, modificar D01 por defecto ni pedir otra entrevista inicial**. Una revisión concreta de D01 sí puede aplicarse con autorización, respaldo, huella y validación. El flujo obligatorio es la [aceptación real de Codex en una instancia existente](guia/ACEPTACION_REAL_CODEX_INSTANCIA_EXISTENTE.md): Git SHA/árbol limpio → script de integración en lectura → Obsidian GUI/CLI → ensayo sintético → revisión humana del mapa → acciones en bóveda sólo con autorizaciones separadas.

Codex debe ejecutar scripts/aceptacion_integracion_local.py para generar reporte saneado SIN subir fuentes ni datos a GitHub. Si el git checkout está sucio, si falla la suite en Mac o si cambia un archivo real, **detenerse y corregir el producto**, no arreglarlo editando manualmente los documentos de empresa. La sesión nueva debe leer primero el estado canónico y fuentes originales, no reconstruir desde resúmenes. El GitHub maestro y la bóveda real jamás se sincronizan por copia directa.

Si no existe instancia, sí seguir el onboarding de instalación en ruta privada separada. En ambos casos la prueba de integración y permisos se separa de la aceptación empresarial.

## Construcción y uso de la empresa completa

Al instalar, crear o continuar una bóveda para conocer el negocio, activa `.agents/skills/ce-desarrollo-empresa/SKILL.md` tras la bifurcación nueva/existente. Coordina las skills actuales y `docs/FLUJO_EMPRESA_COMPLETA.md`: mapa de cobertura D01–D07 por **tarea y fuente**, primera pieza útil, revisión, uso, corrección y continuidad. No esperar a que el dueño pida cada familia ni imponer siete archivos. Si solicita marketing, marca, demanda o contenido, sigue `docs/MARKETING_EMPRESARIAL.md` y conecta D02/D03 con dirección, entrega, economía y permisos. Una corrección no alimenta memoria automática ni una tarea programada sin revisión/permiso. El objetivo es que la siguiente sesión haga trabajo empresarial con el conocimiento, no sólo que lo describa.

## Invariantes (siempre)

1. Nunca confundas la instalación del software con la construcción del conocimiento empresarial. Verifica ambas de manera independiente.
2. No inventes modelo de negocio, productos, precios, acuerdos, pagos, clientes, procesos ni facultades. Una salida de IA es **propuesta** hasta verificación apropiada; distingue hechos, decisiones, hipótesis, histórico y pendientes.
3. Conserva metodología vNext-1.0R (`metodologia/vNext-1.0R/Guia_...md`): P01 → K1/K2/K3/K4 → elicitación experta K1 → G1–G7 → documento especializado → auditoría. No reemplaces D01–D07/X01–X07 por un catálogo de notas vacías.
4. Autoridad por **asunto + entidad + contexto/ámbito + fecha + fuente + permiso**. No selecciones la información más reciente por defecto. Separa usado / ofrecido / cotizado / aceptado / contratado / entregado / facturado / cobrado.
4a. Una ficha F puede localizar o resumir un original; su propiedad `lectura` registra trabajo anterior, **no demuestra que esta sesión abrió ese original**. Antes de atribuirle una afirmación o citar su ruta como leída, abre el pasaje pertinente en esta sesión y verifica su alcance. Si sólo consultaste la ficha, cita la ficha e indica que el original no fue revisado ahora. Verifica esta correspondencia contra los comandos realmente ejecutados antes de entregar.
5. Un `[[enlace]]` no prueba una relación ni una respuesta correcta. Prueba recuperación con preguntas reales y casos negativos.
5a. Los nombres visibles de las notas describen el asunto para la persona que usa Obsidian; los IDs permanecen en propiedades. Resolver rutas por ID cuando importe la identidad y seguir `docs/NOMBRES_LEGIBLES.md` para migrar una instalación existente.
6. Cada empresa usa una carpeta privada fuera de Git (o `instancias/` ignorada) y el producto distribuible no contiene datos reales. No compartas fuentes, datos personales o secretos fuera del ámbito autorizado.
7. No instales plugins comunitarios, descargues código, publiques, envíes comunicaciones, subas datos ni cambies permisos sin autorización. `obsidian-projects` está archivado: no instalarlo por defecto. Bases nativo primero; verificar GUI/versiones.
8. Cambios a notas vigentes o autorizadas: fuente y relectura → propuesta no destructiva → impacto → decisión humana → revisión de versiones → verificación. No reescribir históricos.
9. Si no puedes comprobar el entorno local, informa `NO VERIFICADO`. No declares Obsidian/CLI/Bases instalados ni un agente con permisos que no observaste.
10. **No reinicies desde cero el producto:** preserva código probado, el contrato `vNext-0.9`, la guía `vNext-1.0R` y la trazabilidad de recursos. Esta regla NO obliga a conservar textos empresariales que su propietario rechazó. Corrige código mediante tests e incrementos pequeños; no «arregles» pruebas borrando datos.
11. **Rechazo editorial explícito:** si el propietario declara que una bóveda, documentos o redacciones anteriores son incorrectos, genéricos o no representan su negocio, clasifícalos como **legado rechazado**. NO importes, reescribas, resumas, indexes ni uses esos textos como autoridad o como borrador encubierto. Conserva respaldos sin tocarlos. Sólo utiliza fuentes primarias autorizadas o criterio nuevo del experto; cualquier excepción requiere aprobación expresa por fuente. Sigue `docs/RECONSTRUCCION_EDITORIAL_Y_FUENTES.md`.
12. **Desarrollar el negocio, no narrar carencias:** una síntesis empresarial debe empezar por hechos, actividades, mecanismos, criterios, decisiones, capacidades y su posible utilidad; no por la lista de lo que el agente no demostró. El propietario/decisor es fuente primaria de su estrategia y criterio interno; los sistemas acreditan sus propios hechos; contratos y mediciones acreditan transacciones y resultados. La trazabilidad, restricciones y preguntas pendientes pertenecen mayormente a CONTROL, no al cuerpo. Conserva la incertidumbre donde sea material, sin convertir cada oportunidad en una negación. Relee `docs/SINTESIS_EMPRESARIAL_CONSTRUCTIVA.md` y la sección «documento empresarial vs. CONTROL» de vNext-1.0R.
13. **Conservar el significado completo:** por cada intervención sustantiva del dueño, contrasta el original íntegro y sus correcciones con las notas resultantes. Asigna cada afirmación material a una unidad desarrollada o a la fuente con razón explícita. No conviertas un producto futuro en mera mejora interna, no reduzcas un mecanismo a una lista de temas ni sustituyas el patrón de decisión por una transcripción sin uso. Coteja fuente→nota y nota→fuente antes de declarar utilidad. La voz del cuerpo debe servir al equipo que trabaja en la empresa, no narrarla desde fuera.

## Puerta obligatoria de arquitectura antes de redactar

Cuando el propietario explica varios mecanismos, ofertas, decisiones, procesos, casos o investigaciones en una conversación, **el primer entregable no es un ensayo D01 ni fichas automáticas**: es un mapa de unidades y sus relaciones. Activa de oficio `.agents/skills/ce-arquitectura-conocimiento/SKILL.md` y `docs/ARQUITECTURA_CONOCIMIENTO_ANTES_DE_REDACTAR.md`.

Codex debe identificar asuntos, distinguir identidad por versión, autoridad, vigencia, permisos, responsable o consulta, recuperar notas existentes, justificar crear/revisar/reutilizar/no crear, y establecer un único dueño canónico para cada afirmación. Las síntesis D/X enlazan entidades con identidad propia, sin repetir sus datos cambiantes. Proponer etiquetas temáticas y relaciones tipadas con evidencia y ámbito. Si hay varios asuntos, ejecutar `plan-conocimiento` en sólo lectura y **mostrar la arquitectura al dueño ANTES de redactar o pedir escrituras**. Una nota puede bastar si hay justificación empresarial; no fijar cuotas de notas.

Los tags ayudan a navegar, no son autoridad. El CLI revisa integridad del plan, no decide semánticamente qué importa. **El propietario no debe recordarle a Codex esta puerta de arquitectura.**

## Navegación del conocimiento ya creado

Cuando existan notas y relaciones tipadas aprobadas para registrar, **no dejarlas invisibles en JSON**. Codex usa primero mapa-conocimiento en sólo lectura: revisa notas, etiquetas, aristas candidatas y estado de ratificación; luego muestra el plan, SHA y limitaciones. Sólo con autorización humana específica ejecuta publicar-mapa con confirmación literal, SHA original/propuesto y respaldo externo privado. El mapa genera Markdown y Canvas bajo 00_Mapas y **NO edita notas, D/X, fuentes, ofertas ni vistas Bases**. Al cambiar notas debe regenerarse con nueva autorización; nunca considerarlo autoritativo.

Leer docs/ESPECIFICACION_RED_CONOCIMIENTO_V0_4.md y docs/RELACIONES_TIPADAS.md. Las 16 Bases siguen siendo vistas derivadas sobre propiedades de notas. En una instalación nueva pueden usarse junto con el mapa; en una bóveda anterior ninguna migración o publicación se aplica por defecto.

## Captura provisional mientras se conversa

Durante el descubrimiento, no esperar a tener aprobado un D/X completo para conservar un progreso verificable en la bóveda. Cuando el propietario autorice guardar notas de trabajo, registrar fuentes admisibles con `fuente` y cada ronda sustantiva con `capturar` en `90_Sistema/Descubrimiento/`. Es **control provisional**, no conocimiento aprobado. Mostrar rutas/IDs y ejecutar `estado` + `validar`. No utilizar textos empresariales rechazados ni elevar un caso a venta o servicio de la empresa sin autoridad. Ver `docs/CAPTURA_PROGRESIVA.md`.

Para pasar de la conversación a una pieza útil, ejecutar el ciclo de `docs/CICLO_EXPERTO_DESARROLLO_EMPRESARIAL.md`: volver al original, contrastar capturas y correcciones, desarrollar mecanismo y alternativas, distribuir asuntos, entregar una propuesta corregible y materializar sólo con el permiso correspondiente. Ante una corrección del dueño, suspender la propagación de la afirmación cuestionada y rehacerla desde el original antes de continuar. Este ciclo también aplica a instancias existentes; no repetir el onboarding.

## Comandos mínimos

Si un comando falla por una dependencia ausente, comprueba primero el intérprete y los entornos Python ya disponibles para esa instancia. Reintenta con uno que tenga las dependencias instaladas antes de declarar `NO VERIFICADO` o pedir una instalación. Un fallo de `python3` no demuestra que falle el Python de trabajo; registra cuál se usó. No instales dependencias sin la autorización correspondiente.

```bash
python -m pip install -r requirements.txt  # solicitar autorización si requiere red
python scripts/cerebro.py doctor
python -m unittest discover -s tests -v
python scripts/cerebro.py crear --id EMPRESA-ID --nombre "Mi empresa" --dest /ruta/privada
python scripts/cerebro.py validar --vault /ruta/privada
python scripts/cerebro.py estado --vault /ruta/privada
```

Consulta la skill específica antes de ampliar cualquier flujo. Para arquitectura o cambios de código consulta `docs/ARQUITECTURA.md`, `docs/HOJA_DE_RUTA.md` y `docs/CRITERIOS_DE_ACEPTACION.md`; no los cargues para tareas triviales.


## Reparar Bases existentes después de navegar GUI

Cuando Obsidian haya autoguardado vistas .base, no intentes copiar
plantillas, forzar versiones antiguas ni tratar los cambios YAML como
corrupción. La observación de la GUI no garantiza igualdad byte por byte.
Usa docs/BASES_FILTROS_Y_ACTUALIZACION.md: cierra Obsidian, prepara plan
actual de 16 vistas, captura sha_plan y respalda fuera de Git/bóveda; con
autorización limitada, actualiza exclusivamente filtros raíz con --sha-plan.
El migrador respalda las 16 vistas actuales y workspace.json, detecta cambios
concurrentes y conserva views:/groupBy del estado actual. Luego valida
Bases desde GUI/CLI y D01/fuentes mediante SHA. No exijas segunda computadora
para permitir el uso local de una empresa ya instalada.
