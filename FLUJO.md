# Flujo — voz de Tita en Higgsfield

Procedimiento para clonar la voz y generar líneas con ella. Los nombres entre
`backticks` son las herramientas reales del MCP de Higgsfield, tal como se
llaman al invocarlas.

---

## Fase 1 — Conseguir el audio de referencia

Higgsfield clona a partir de una muestra de voz. Requisitos de la muestra:

- **Habla clara**, una sola persona, sin música ni ruido de fondo.
- **Entre 10 segundos y 3 minutos.** Más corto no alcanza; más largo lo rechaza.
- Mismo tono y energía que se quiere en Tita: si la muestra suena plana, la
  clonación sale plana.

El audio se registra en `referencias/README.md` con su ruta local. **No se sube
al repo.**

> PENDIENTE: definir de dónde sale la muestra — ¿locución nueva grabada para
> esto, o material de archivo de la Universidad? Si es material de archivo, hay
> que confirmar que se tienen los derechos de uso de esa voz.

## Fase 2 — Crear la voz clonada

Dos caminos, según de dónde venga el audio:

**Camino A — grabar o subir desde el navegador (el normal).**
Se llama `create_voice`. Abre una interfaz que graba o sube el archivo,
lo confirma y crea la voz de una vez. `initial_tab: "upload"` si el archivo ya
existe; `record` si se va a grabar en el momento.

**Camino B — el archivo ya está subido a Higgsfield.**
`media_upload` → subir los bytes → `media_confirm` con `type: "audio"` →
`create_voice_from_confirmed_audio` con ese `audio_media_id` y un `name`.

En ambos casos: **la clonación cuesta créditos** y es **asíncrona**. Al
terminar devuelve un `voice_id`, pero recién creada la voz queda en
`processing` y todavía no sirve.

**No generes de una.** Verifica con `list_voices` que la voz esté
`status: "completed"` y `is_audio_eligible: true`. Si sale
`voice_clone_failed` o `failed`, la clonación no sirvió y toca repetir la
Fase 1 con mejor muestra.

Apenas salga el `voice_id`, va a `registro/bitacora.md`. Sin eso se pierde.

## Fase 3 — Generar líneas con la voz

`generate_audio`, una línea por llamada. Para varias líneas independientes
(2 a 12), `generate_audio_batch`.

Parámetros que importan:

| Parámetro | Valor |
|---|---|
| `model` | `seed_audio` (Seed Audio 1.0, ByteDance). Es el que se usa por defecto. |
| `voice_type` | `element` — porque es voz propia clonada, no una del catálogo. |
| `voice_id` | El que devolvió la Fase 2. |
| `prompt` | La línea a decir. Sale de `prompts/guion-base.md`. |

Ajuste fino disponible en `seed_audio`: `speech_rate` (velocidad),
`pitch_rate` (tono), `loudness_rate` (volumen), `format`, `sample_rate`.
Estos son los que se mueven cuando la voz "casi" queda pero no del todo.

Antes de gastar, `get_cost: true` devuelve el costo en créditos **sin generar
nada**. Úsalo para presupuestar una tanda antes de lanzarla.

Si se quiere comparar contra otro motor: `model: "text2speech_v2"` más
`variant` (`elevenlabs`, `minimax`, `seed_speech`, `vibe_voice`, `cozy_voice`).
Sirve para contrastar, pero el default se queda en `seed_audio`.

## Fase 4 — Registrar

Cada tanda que se escuche va a `registro/bitacora.md`: fecha, `voice_id`,
modelo, parámetros, qué línea, dónde quedó el archivo y el veredicto.

Una generación sin fila en la bitácora es una generación que no se puede
repetir. Ese es el punto entero de este repo.

---

## Cuidado con los créditos

`generate_audio` y la clonación cobran. El parámetro `use_unlim` decide si
paga el saldo de créditos o las generaciones ilimitadas de prueba. **Déjalo
sin poner** salvo que Samuel pida explícitamente usar las ilimitadas: así el
servidor pregunta antes de gastar en vez de decidir solo.

## Pendientes del flujo

- [ ] Definir el origen de la muestra de voz (Fase 1) y sus derechos de uso.
- [ ] Confirmar si hay una guía de marca de la Universidad El Bosque que
      defina cómo debe sonar Tita (edad, energía, acento).
- [ ] Fijar los valores de `speech_rate` / `pitch_rate` una vez se apruebe
      una versión, para que todas las líneas futuras salgan iguales.
