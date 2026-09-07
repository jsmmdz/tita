# Bitácora de generaciones

Una fila por tanda. Si no está acá, no se puede repetir.

## Voces en uso

No se creó ninguna voz: todas son presets del catálogo.

| Personaje | Voz | voice_id | Estado |
|---|---|---|---|
| **Tita** | Giselle | `9d3128b8-dd25-5158-9bdb-2e69ac8998b9` | **Elegida** 2026-09-07 |

**Habla Tita y nadie más.** No hay segundas voces en la serie: los once
capítulos son monólogo, así que es un video por capítulo y una sola conversión.

## Generaciones

| Fecha | Capítulo | voice_id | Toma | Archivo | Veredicto |
|---|---|---|---|---|---|
| _(vacío)_ | | | | | |

- **Capítulo**: el archivo de `guiones/`, por ejemplo `01-medicina`.
- **Toma**: cuál grabación original se convirtió, si hubo varias.
- **Archivo**: ruta local donde quedó el audio. No se sube al repo.
- **Veredicto**: qué falló y en cuál réplica. "Bien" no sirve de nota;
  "se come el 'cuarenta y uno', la pregunta no sube" sí.

### Líneas que hay que escuchar con lupa

Salen de las notas de locución. Son los puntos donde la conversión se puede
caer.

| Guion | Qué revisar |
|---|---|
| `02-creacion-comunicacion` | **Los siete programas seguidos.** La línea más difícil de la serie. |
| `01-medicina` | **"Medicina, Instrumentación Quirúrgica y Optometría"** y el punto y coma del remate. |
| `09-economicas` | **Las dos "y" seguidas** de la línea de programas. |
| `06-ciencias` | **"Estadística"** — esdrújula que algunos motores aplanan. |
| `07-ingenieria` | **"…todavía"** — la pausa antes y el tono. Todo el capítulo cuelga de ahí. |
| `00-presentacion` | La enumeración de cuatro comas. |

## Decisiones tomadas

Acá van los valores que ya se aprobaron y no se vuelven a discutir.

| Fecha | Decisión |
|---|---|
| 2026-08-31 | **No se clona ninguna voz.** Se usa un preset del catálogo. |
| 2026-08-31 | **Qwen queda fuera**: su interfaz no deja seleccionar la voz. |
| 2026-09-07 | **La voz de Tita es Giselle** (`9d3128b8-dd25-5158-9bdb-2e69ac8998b9`). Sin Ronda B, a oído. No se vuelve a discutir. |
| 2026-09-07 | **La serie es de once capítulos**: diez facultades más presentación. Techo de treinta segundos cada uno. |
| 2026-09-07 | **Los once capítulos son monólogo de Tita.** No hay segundas voces ni personajes. Un video por capítulo, una conversión. |
| 2026-09-07 | **Tita habla en primera persona.** Cierra el pendiente que podía reescribir los once guiones. |
| 2026-09-07 | **Los diez capítulos de facultad invitan a conocer la facultad y sus programas**, en cuatro tiempos: el nombre, qué se estudia, el giro, la invitación. |
| 2026-09-07 | **Todos abren presentando la facultad**: "Esta es la Facultad de…", nombre completo y silencio después. El remate ya no lo repite. |
| 2026-09-07 | **Orden de la serie:** Medicina primero, Creación y Comunicación segundo, y de ahí para abajo los demás. |
| 2026-09-07 | **La serie se hace doblando voz real**, no generando desde texto. Motivo: expresividad — el TTS todavía suena robótico y los guiones viven de las pausas. Solo la pista de Tita se convierte. |
| 2026-09-07 | **Las Rondas A y B quedan canceladas.** `voice_change` no tiene parámetro de modelo, así que no hay motor que elegir. |
| 2026-09-07 | **Los videos de entrada pueden ir en negro total.** `voice_change` no mira la imagen. El micrófono sí importa. |

### Todavía sin decidir

- **Si `voice_change` conserva la dicción.** Lo resuelve la Prueba 1 sobre
  `01-medicina`. Ver `guiones/PRUEBA-01.md`.
- **Los nombres de los programas.** Ninguno verificado contra la página oficial.
  Es el pendiente más urgente.
- **Si Giselle aguanta el lema.** Filtro sin correr.
