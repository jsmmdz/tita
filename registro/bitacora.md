# Bitácora de generaciones

Una fila por tanda. Si no está acá, no se puede repetir.

## Voces en uso

No se creó ninguna voz: todas son presets del catálogo.

| Personaje | Voz | voice_id | Estado |
|---|---|---|---|
| **Tita** | Giselle | `9d3128b8-dd25-5158-9bdb-2e69ac8998b9` | **Elegida** 2026-09-07 |
| Rol — Medicina | Juan | `6b528d43-c056-4a2f-9d82-1591a7ba13b0` | Propuesta, sin audicionar |
| Rol — Odontología | Kaia | `bb9db352-f345-59f3-90b3-fa9432bcff91` | Propuesta, sin audicionar |
| Rol — Enfermería | Helena | `3c2b83c0-2e0a-5ae8-998a-a5fe71b7eccd` | Propuesta, sin audicionar |
| Rol — Psicología | Julian | `95429266-c0ac-4137-a209-63b8812b0f23` | Propuesta, sin audicionar |
| Rol — Ciencias | Zoe | `d0374db1-44b9-4f05-939e-0a9ae9dbbe6a` | Propuesta, sin audicionar |
| Rol — Ingeniería | Marcus | `6f98d3dd-324f-4845-8c28-c1d1647a06cd` | Propuesta, sin audicionar |
| Rol — Jurídicas | Luna | `375a3398-e3b4-4f91-845d-42181e352899` | Propuesta, sin audicionar |
| Rol — Económicas | Andre | `f1e8226e-2248-4d5f-b43c-0a79e9949dbf` | Propuesta, sin audicionar |
| Rol — Creación | Chloe | `e9cfbbf0-4476-46be-b396-596eb774b165` | Propuesta, sin audicionar |
| Rol — Educación | Miles | `e18664a7-ee4f-5273-acf8-533eb24cd366` | Propuesta, sin audicionar |

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
| 2026-09-07 | **Los diálogos se generan por pista separada y se editan.** Nada de multi-hablante hasta que haya motor decidido. |

### Todavía sin decidir

- **El motor.** Falta la Ronda A. Sin esto no se graba nada.
- **La persona.** Primera o tercera. Reescribe los once guiones si cambia.
- **Las voces de los roles.** Las de arriba son propuestas.
- **Si Giselle aguanta el lema.** Filtro sin correr.
