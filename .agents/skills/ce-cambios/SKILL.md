---
name: ce-cambios
description: "Gestionar modificaciones en conocimiento empresarial sin sobrescribir autoridad: cambios de precios, procesos, decisiones o promesas."
---

# ce-cambios

1. Identifica qué fue solicitado, qué nota/bloque es autoridad, su versión y vigencia, qué otras piezas dependen de ella.
2. Recupera fuente de cambio y quién tiene facultad de aprobar. Propuesta de IA no equivale a decisión.
3. Guarda cambio candidato en archivo temporal local y ejecuta `python scripts/cerebro.py proponer --vault ... --id ID --motivo ... --archivo /ruta/candidato.md`; esto **no cambia el original** y conserva SHA-256 previo.
4. Compara contradicciones, excepciones, contratos particulares y fechas; presenta diff humano y efecto sobre derivados.
5. Solicita aprobación explícita de decisor autorizado antes de aplicar; no hay motor automático de merge en esta versión, por lo que no declares que la modificación ya quedó vigente.
6. En aplicación futura preservar histórico/versiones y volver a validar, no sobrescribir para tests verdes.
**Salida:** propuesta, fuentes, impactos, aprobación pendiente y límites de alcance.
