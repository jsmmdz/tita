# Guiones — serie de cortos de Tita

Una serie de capítulos cortos. **Uno por facultad**, más el de presentación.
Cada capítulo es un diálogo entre Tita y **el rol** que representa esa
facultad: un estudiante, un docente, alguien en su práctica.

---

## Ficha de producción

| Dato | Valor |
|---|---|
| Voz de Tita | **Giselle** |
| `voice_id` | `9d3128b8-dd25-5158-9bdb-2e69ac8998b9` |
| `voice_type` | `preset` |
| Motor | **PENDIENTE** — lo decide la Ronda A (`investigacion/modelos-y-flujo.md`) |
| Duración por capítulo | **máximo 30 segundos** |
| Persona | Tita habla en **primera persona** |

**Giselle es la voz de Tita en toda la serie.** Decisión de Samuel,
2026-09-07. No se cambia entre capítulos: la voz es el personaje.

## Los capítulos

| # | Archivo | Facultad | Rol que dialoga con Tita |
|---|---|---|---|
| 00 | `00-presentacion.md` | — | Tita sola |
| 01 | `01-medicina.md` | Medicina | Estudiante en su primera rotación |
| 02 | `02-odontologia.md` | Odontología | Estudiante en clínica |
| 03 | `03-enfermeria.md` | Enfermería | Estudiante en turno de noche |
| 04 | `04-psicologia.md` | Psicología | Estudiante de práctica clínica |
| 05 | `05-ciencias.md` | Ciencias | Estudiante en el laboratorio |
| 06 | `06-ingenieria.md` | Ingeniería | Estudiante con un prototipo |
| 07 | `07-juridicas-politicas.md` | Ciencias Jurídicas y Políticas | Estudiante en consultorio jurídico |
| 08 | `08-economicas-administrativas.md` | Ciencias Económicas y Administrativas | Estudiante de administración |
| 09 | `09-creacion-comunicacion.md` | Creación y Comunicación | Estudiante realizadora |
| 10 | `10-educacion.md` | Educación | Docente en formación |

## Reglas de escritura de esta serie

Estas reglas salen de `investigacion/lenguaje-institucional-ueb.md`. No son
gusto: son el brief.

1. **Tita pregunta, no explica.** Su atributo central es la curiosidad. El que
   sabe del tema es el rol, no ella. Tita abre la puerta; el otro la cruza.
2. **Nadie recita el portafolio.** Ningún personaje dice "en nuestra facultad
   formamos profesionales integrales". Se muestra la facultad por lo que se
   hace en ella un martes cualquiera.
3. **Suena a estudiante, no a comercial.** A Tita la eligió la comunidad en
   votación. Si la línea se puede leer en voz de locutor de radio, se reescribe.
4. **Un solo remate.** Cada capítulo cierra con una frase de Tita que se pueda
   citar sola. Nada después de esa frase.
5. **Los números van escritos en letras** — "cuarenta y uno", no "41". Los TTS
   se caen ahí y no hay forma de corregirlos después.
6. **Sin emojis ni hashtags dentro del texto hablado.** Van en el copy del
   post, no en el guion.
7. **Nadie dice el lema.** *"Por una cultura de la vida, su calidad y su
   sentido"* es línea institucional; hasta que se corra el filtro de lema sobre
   Giselle no se pone en boca de nadie. Ver `prompts/texto-de-prueba.md`.

## Cuánto dura un guion

Referencia: **español narrado ≈ 2,6 palabras por segundo.** Con pausas de
diálogo, calcula **2,3**.

- 30 segundos ≈ **70 palabras como techo**.
- Los guiones de esta carpeta van entre 55 y 75 palabras a propósito: dejan
  aire para respirar y para el corte de imagen.

Si un guion crece, se corta una réplica entera. No se acelera la voz: subir
`speech_rate` para meter texto se oye, y suena a que no cupo.

## Cómo se generan los diálogos

Cada capítulo tiene **dos voces**. Hay dos caminos:

1. **Por separado y se edita** — recomendado. Se genera la pista de Tita
   (Giselle) y la del rol aparte, y se arman en el editor. Funciona con
   cualquier motor y deja controlar las pausas al montar.
2. **Multi-hablante en `seed_audio`** — es el único motor pensado para
   "escenas de varios hablantes". Cuesta el triple y todavía no está probado.

Hasta que la Ronda A decida el motor, se va por el camino 1.

## Las segundas voces están sin audicionar

Cada capítulo propone una voz para el rol. **Son propuestas, no decisiones.**
Las femeninas salen de las cinco finalistas que Samuel ya aprobó a oído; las
masculinas nunca se han escuchado.

Regla: la voz del rol **no puede parecerse a Giselle**. Si al montar el
capítulo cuesta saber quién habla, se cambia la voz del rol, nunca la de Tita.

## Antes de grabar, confirma esto

- [ ] **Persona.** Todo está escrito con Tita en primera persona. Lo oficial de
      la UEB la narra en tercera. Si la serie va en tercera, se reescriben los
      once guiones. Pregunta antes de generar.
- [ ] **Nombres de las facultades**, contra `unbosque.edu.co`. El dominio está
      bloqueado por el proxy de esta sesión; la lista se armó con resultados de
      búsqueda.
- [ ] **Las segundas voces**, con una audición corta.
- [ ] **El motor**, con la Ronda A.
