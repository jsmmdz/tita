# Bitácora de generaciones

Una fila por tanda. Si no está acá, no se puede repetir.

## Voces en uso

No se creó ninguna voz: todas son presets del catálogo.

| Personaje | Voz | voice_id | Estado |
|---|---|---|---|
| **Tita** | Giselle | `9d3128b8-dd25-5158-9bdb-2e69ac8998b9` | **Elegida** 2026-09-07 |
| Los roles | Voz original de quien graba | — | No se convierte |

Los roles ya no usan preset: se quedan con la voz de la persona que los graba.
Solo la pista de Tita pasa por `voice_change`.

## Generaciones

| Fecha | Capítulo | Personaje | voice_id | Modelo | speech_rate | pitch_rate | Archivo | Veredicto |
|---|---|---|---|---|---|---|---|---|
| _(vacío)_ | | | | | | | | |

- **Capítulo**: el archivo de `guiones/`, por ejemplo `01-medicina`.
- **Personaje**: `TITA` o el rol. Cada uno es una generación aparte.
- **Archivo**: ruta local donde quedó el audio. No se sube al repo.
- **Veredicto**: qué falló y en cuál réplica. "Bien" no sirve de nota;
  "se come el 'cuarenta y uno', la pregunta no sube" sí.

### Palabras que hay que escuchar con lupa

Salen de las notas de locución de los guiones. Son los puntos donde un TTS se
cae, y donde no hay cómo corregir si el motor no tiene perillas.

| Guion | Qué revisar |
|---|---|
| `06-ingenieria` | **"cuarenta y uno"** — el número más largo de la serie. |
| `10-educacion` | **"averigüémoslo"** — esdrújula con diéresis. |
| `02-odontologia` | **"doceava"**, **"la trece"**. |
| `03-enfermeria` | **"a las tres de la mañana"**. |
| `00-presentacion` | La enumeración de cuatro comas. |

## Decisiones tomadas

Acá van los valores que ya se aprobaron y no se vuelven a discutir.

| Fecha | Decisión |
|---|---|
| 2026-08-31 | **No se clona ninguna voz.** Se usa un preset del catálogo. |
| 2026-08-31 | **Qwen queda fuera**: su interfaz no deja seleccionar la voz. |
| 2026-09-07 | **La voz de Tita es Giselle** (`9d3128b8-dd25-5158-9bdb-2e69ac8998b9`). Sin Ronda B, a oído. No se vuelve a discutir. |
| 2026-09-07 | **La serie es de once capítulos**: diez facultades más presentación. Techo de treinta segundos cada uno. |
| 2026-09-07 | **Los diálogos se graban por pista separada y se editan.** Un video por personaje; nunca los dos en la misma toma. |
| 2026-09-07 | **Tita habla en primera persona.** Cierra el pendiente que podía reescribir los once guiones. |
| 2026-09-07 | **Los diez capítulos de facultad invitan a conocer la facultad y sus programas.** |
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
