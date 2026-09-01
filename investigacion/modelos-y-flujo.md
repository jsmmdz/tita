# Qué modelo usar y cómo correr las pruebas

Investigado el 2026-08-31 con `models_explore(type:'audio')` y con la lista de
la interfaz de Higgsfield. Costos verificados uno por uno con `get_cost` sobre
el texto real de `prompts/texto-de-prueba.md` (12 segundos).

---

## Los cinco modelos de la interfaz, y cómo se llaman por API

La interfaz muestra cinco. Por API no son cinco modelos: son dos, y uno de
ellos tiene cuatro motores adentro. Esta es la traducción:

| Como aparece en la interfaz | Cómo se pide por API | Costo por línea |
|---|---|---|
| Seed Audio 1.0 | `model: "seed_audio"` | **1.0** |
| ElevenLabs v3 | `model: "text2speech_v2"` + `variant: "elevenlabs"` | **0.45** |
| MiniMax Speech 2.8 HD | `model: "text2speech_v2"` + `variant: "minimax"` | **0.45** |
| Seed Speech | `model: "text2speech_v2"` + `variant: "seed_speech"` | **0.30** |
| ~~Qwen Audio 3.0 TTS~~ | ~~`model: "qwen_audio_tts"`~~ | ~~0.07~~ |

**Qwen queda descartado (2026-08-31): su interfaz no deja seleccionar la voz.**
Era el más barato de los cinco y el único con un campo de instrucción libre
—se le podía pedir "español de Colombia, acento bogotano"— pero si no se puede
fijar la voz, no sirve para comparar las finalistas. Quedan cuatro.

La interfaz no los muestra, pero `text2speech_v2` tiene dos motores más:
`vibe_voice` y `cozy_voice`.

**Seed Audio, el default, es el más caro de los cuatro que quedan — más del
triple que Seed Speech.**

## Lo que dice cada uno de sí mismo

Las descripciones de la interfaz son el único lugar donde aparece información
de idioma. Vale leerlas con cuidado:

- **Seed Speech** — *"Voz multilingüe en más de 30 idiomas."* Es la **única
  declaración explícita de multilingüismo** en todo el catálogo. Y cuesta 0.30.
  Con esto pasa a ser el primer candidato para español, no una alternativa.
- **ElevenLabs v3** — *"Control de emoción y entrega."* Es el que está marcado
  por defecto en tu interfaz. ElevenLabs tiene fama merecida en español.
- **MiniMax Speech 2.8 HD** — *"Narración de una sola voz de alta fidelidad."*
  Suena a locución institucional más que a personaje.
- **Seed Audio 1.0** — *"Escenas de varios hablantes."* Está pensado para
  diálogo entre voces, que no es este caso. **Su única ventaja real aquí es que
  es el único con `pitch_rate`**, o sea el único donde se puede afinar el tono
  después.

## El flujo de prueba

El plan anterior (las 6 voces en 2 motores, 12 audios) era caro en atención y
resolvía dos preguntas mezcladas. Con cinco motores en juego conviene
separarlas, porque son preguntas distintas:

> **1. ¿Cuál motor habla español decente?**
> **2. ¿Cuál de las seis voces es Tita?**

### Ronda A — el motor. Una voz, los cuatro motores

Se toma **una sola** de las finalistas y se genera el mismo texto en los cuatro.

**Costo: 2.20 créditos.** Cuatro audios de 12 segundos, menos de un minuto de
escucha.

Aquí no se juzga la voz, se juzga el motor: cuál pronuncia español sin acento
prestado, cuál dice "2023" bien, cuál no mete tonito de robot. **Es probable que
dos de los cuatro se caigan en la primera escuchada.**

Recomiendo correrla con **Luna** por ser un nombre que el motor no va a leer
como extranjero, pero da igual cuál: lo que se compara es el motor.

### Ronda B — la voz. Las seis finalistas, en el motor ganador

**Costo: entre 1.8 y 6.0 créditos**, según cuál gane. Si gana Seed Speech son
1.8; si gana Seed Audio, 6.0.

Seis audios, el mismo texto, comparación limpia con los criterios de
`prompts/texto-de-prueba.md`.

### Total

**Entre 4.0 y 8.2 créditos**, 10 generaciones. La gracia no es la plata, es que
lanzando a mano cada audio cuesta clics: dos tandas ordenadas se hacen
tranquilo, comparar todo contra todo, no.

## Cómo se lanza (a mano, en la interfaz)

Samuel lanza todo a mano. El orden que menos clics cuesta:

**Ronda A — el motor.**

1. Elige una finalista y déjala fija. No la cambies en toda la ronda.
2. Pega el texto de `prompts/texto-de-prueba.md`. **No lo toques más**: si le
   cambias una coma entre un motor y otro, la comparación no vale.
3. Genera con **Seed Speech** primero — es el que dice ser multilingüe y el
   más barato de los que quedan.
4. Repite con **ElevenLabs v3**, **MiniMax Speech 2.8 HD** y **Seed Audio 1.0**,
   sin cambiar ni voz ni texto.
5. Escúchalos seguidos, no salteados. Menos de un minuto en total.

**Ronda B — la voz.**

Ya con el motor decidido, corre las seis finalistas ahí mismo, mismo texto.
Seis audios, comparación limpia.

**Guarda cada audio con nombre que se entienda** —`ronda-a-luna-seedspeech.wav`,
`ronda-b-kaia.wav`— y anota la ruta en `registro/bitacora.md`. Los audios no
entran al repo; la fila que dice dónde están, sí. Un audio sin fila es un audio
que en dos semanas nadie sabe qué era.

## Ajuste fino, si hace falta

Solo sobre la ganadora, y solo si "casi" queda.

Con Qwen fuera, `seed_audio` es **el único de los cuatro con perillas**:

| Parámetro | Rango | Default |
|---|---|---|
| `speech_rate` | −50 a 100 | 0 |
| `pitch_rate` | −12 a 12 | 0 |
| `loudness_rate` | −50 a 100 | 0 |

`text2speech_v2` **no tiene ninguna** — ni ElevenLabs, ni MiniMax, ni Seed
Speech. Solo `variant`, `voice_type` y `voice_id`. Ese es su costo oculto: si
la voz sale un poco rápida o un poco aguda, no hay nada que mover.

**Esto ahora pesa más.** Si gana Seed Speech, ElevenLabs o MiniMax, el único
control que queda es la puntuación: las comas controlan las pausas y son
gratis. Si el ajuste resulta indispensable, toca pasar la finalista a Seed
Audio y afinar ahí, aunque cueste el triple.

## Nota sobre créditos

`models_explore` reporta `unlim: available: false`. **No hay generaciones
ilimitadas disponibles**, así que todo sale del saldo. Las cifras de arriba son
el costo real.

## Salida

`wav` a `44100` Hz para la propuesta final. Para las pruebas, el default
(`wav`, 24000) sobra y pesa menos.

## Pendiente

- [ ] Probar `vibe_voice` y `cozy_voice`, los dos motores de `text2speech_v2`
      que la interfaz no lista. Con Qwen descartado vale más la pena mirarlos.
- [ ] Verificar si Qwen deja fijar la voz por API aunque la interfaz no lo
      permita. Si sí, vuelve a entrar: era el más barato y el único con
      instrucción de dialecto.
- [ ] Si alguna vez conviene automatizar esto: por API son `generate_audio_batch`
      (hasta 12 de una), luego `jobs_wait`, luego **una sola**
      `show_generation_by_ids`. Y `get_cost` no funciona dentro de un batch.
