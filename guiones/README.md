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
| Método | **PENDIENTE** — lo decide la Prueba 1. Ver `PRUEBA-01.md` |
| Duración por capítulo | **máximo 30 segundos** |
| Persona | **Primera persona.** Confirmado por Samuel, 2026-09-07 |
| Tema de los diez de facultad | **Invitar a conocer la facultad y sus programas** |

**Giselle es la voz de Tita en toda la serie.** Decisión de Samuel,
2026-09-07. No se cambia entre capítulos: la voz es el personaje.

## Los capítulos

El orden lo fijó Samuel: **Medicina primero, Creación y Comunicación segundo**,
y de ahí para abajo los demás.

| # | Archivo | Facultad | El gancho |
|---|---|---|---|
| 00 | `00-presentacion.md` | — | Tita se presenta |
| **01** | `01-medicina.md` | **Medicina** | La puerta de simulación · **capítulo de prueba** |
| **02** | `02-creacion-comunicacion.md` | **Creación y Comunicación** | Siete programas en un piso |
| 03 | `03-odontologia.md` | Odontología | Del modelo a la clínica |
| 04 | `04-enfermeria.md` | Enfermería | Cabeza fría y manos firmes |
| 05 | `05-psicologia.md` | Psicología | No es solo escuchar |
| 06 | `06-ciencias.md` | Ciencias | Laboratorio, tablero y campo |
| 07 | `07-ingenieria.md` | Ingeniería | "Todavía" |
| 08 | `08-juridicas-politicas.md` | Ciencias Jurídicas y Políticas | El consultorio jurídico |
| 09 | `09-economicas-administrativas.md` | Ciencias Económicas y Administrativas | Detrás de cada cifra hay alguien |
| 10 | `10-educacion.md` | Educación | Nadie termina de aprender a enseñar |

Los diez de facultad tienen **la misma forma**: Tita pregunta por algo que ve,
el rol responde con algo concreto y con los programas, y **Tita cierra con la
invitación**. El remate es siempre de ella y siempre dice el nombre de la
Facultad, para que se pueda buscar después.

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

## Cómo se hacen las voces

**Se graba con voz real y a Tita se le pone la de Giselle encima.** Esa es la
prueba que decide todo, y está en `PRUEBA-01.md`.

Dos cosas que hay que saber antes de grabar:

- **`voice_change` recibe video, no audio.** Hay que grabar en video aunque la
  imagen sea un plano fijo. Con un `.wav` suelto no se puede entrar.
- **Solo se convierte la voz de Tita.** El rol se queda con la voz de quien lo
  grabó: son personas distintas y así se distinguen sin esfuerzo.

Se graban **dos videos por capítulo**, uno por personaje, y se montan. Nunca
los dos en la misma toma: si están mezclados, `voice_change` no puede
convertir a uno solo.

## Antes de grabar, confirma esto

- [x] **Persona.** Primera persona. Confirmado 2026-09-07.
- [ ] **Los nombres de los programas.** Cada capítulo los nombra y **ninguno
      está verificado** contra `unbosque.edu.co` — el dominio está bloqueado
      por el proxy de esta sesión. Es el pendiente más urgente: decir mal el
      nombre de un programa en una pieza institucional es el error que sí se
      nota.
- [ ] **El método**, con la Prueba 1.
- [ ] **Si Giselle aguanta lo institucional.** El capítulo 04 es el termómetro.

## Los programas que se nombran

Salieron de resultados de búsqueda, no de la página oficial. **Verifícalos
antes de grabar.**

| Capítulo | Programas nombrados |
|---|---|
| 01 Medicina | Medicina, Instrumentación Quirúrgica, Optometría |
| 02 Creación y Comunicación | Arquitectura, Artes Plásticas, Arte Dramático, Diseño Industrial, Diseño de Comunicación, Creación Digital, Formación Musical |
| 06 Ciencias | Biología, Matemática, Estadística |
| 07 Ingeniería | Ambiental, de Sistemas, Electrónica, Industrial |
| 08 Jurídicas y Políticas | Derecho, Ciencia Política |
| 09 Económicas y Administrativas | Administración de Empresas, Negocios y Relaciones Internacionales |
| 03, 04, 05 | Un solo programa, del mismo nombre de la Facultad |
| 10 Educación | **Ninguno** — no se pudo verificar la oferta |
