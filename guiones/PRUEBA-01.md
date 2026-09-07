# Prueba 1 — voz original convertida a Giselle

**Objetivo:** grabar el capítulo `01-medicina` con voz real y ponerle la de
Giselle encima. De ahí sale la decisión técnica de toda la serie.

---

## Lo primero: `voice_change` recibe **video**, no audio

Esto cambia el plan y conviene saberlo antes de grabar.

    voice_change(params: {
      video_id:   <media_id de un video subido, o job_id de un video generado>,
      voice_id:   "9d3128b8-dd25-5158-9bdb-2e69ac8998b9",   # Giselle
      voice_type: "preset"
    })

Reemplaza la voz hablada **de un video** conservando el tiempo y la imagen, y
vuelve a pegar el audio nuevo sobre el video. **No recibe un `.wav` suelto.**

Consecuencia práctica: **hay que grabar en video**, aunque la imagen sea un
plano fijo del techo. Si solo grabas audio, no hay con qué entrar.

## Lo segundo: `voice_change` no tiene parámetro de modelo

Dijiste que el modelo se define al convertir el primer capítulo. Ojo con esto:
`voice_change` **no expone modelo, ni motor, ni variante.** Solo `video_id`,
`voice_id` y `voice_type`. No hay nada que elegir.

Así que la prueba no decide *cuál modelo*. Decide algo más importante:

> **¿La serie se hace doblando voz real, o generando desde texto?**

Son dos caminos distintos y solo uno necesita elegir motor:

| | **Doblaje** — `voice_change` | **Texto a voz** — `generate_audio` |
|---|---|---|
| Entrada | Video con voz real | El texto del guion |
| Elección de motor | **No hay** | Sí — cuatro motores, de 0.30 a 1.0 |
| Quién pone el ritmo | El actor que grabó | El motor |
| Pausas, ironía, el "…Todavía" | Salen de la actuación | Solo con puntuación |
| Rehacer una línea | Volver a grabar | Regenerar, gratis en tiempo |

**Mi lectura:** para esta serie el doblaje se ve mejor. Los guiones dependen de
pausas y de tono —el "…No se mueve", el "Uy. Difícil."— y eso una persona lo
hace bien de una y un TTS no lo hace casi nunca. Pero es una lectura, no un
dato: por eso la prueba.

Si el doblaje funciona, **la Ronda A se cancela entera** y no hay que gastar
las 2.20 créditos en comparar motores.

## Cómo grabar

1. **Video, no audio.** Celular en horizontal, plano fijo, sin música.
2. **Habla natural, en español, a ritmo de conversación.** No imites una voz de
   comadreja: `voice_change` reemplaza el timbre, no la actuación. Lo que hagas
   con las pausas y el énfasis se queda.
3. **Las dos voces por separado.** Un video con las líneas de TITA y otro con
   las del ESTUDIANTE. Solo el de Tita se convierte.
4. **Deja dos segundos de silencio** al principio y al final de cada video.
   Sirven para montar.
5. **Marca los puntos de riesgo**: en `01-medicina` son la enumeración
   "Medicina, Instrumentación Quirúrgica y Optometría" y el punto y coma del
   remate. Grábalos con la pausa bien hecha.

## Cómo convertir

1. Sube el video de las líneas de Tita. Anota el `media_id`.
2. `voice_change` con `voice_id` de Giselle y `voice_type: "preset"`.
3. Guarda el resultado como `01-medicina-tita-giselle.mp4` y anota la ruta.
4. La fila va a `registro/bitacora.md`. Sin fila, la prueba no se puede repetir.

## Qué escuchar en el resultado

Compara el original contra el convertido. En este orden:

1. **¿Se entiende igual de bien?** Si `voice_change` embarra la dicción, se
   acabó el camino del doblaje.
2. **¿"Instrumentación Quirúrgica" sobrevivió?** Es el punto de quiebre.
3. **¿Las pausas que actuaste siguen ahí?** Deberían: conserva el tiempo.
4. **¿El acento suena de aquí, o quedó prestado?** Giselle nunca se ha oído en
   español.
5. **¿Suena a estudiante o a comercial?**
6. **¿Se le nota lo procesado?** Metálico, aguado, con artefactos.

## Cómo se decide

- **Aguanta los seis puntos** → la serie se hace por doblaje. Se graban los
  otros diez y se cancela la Ronda A.
- **Falla en dicción o en el nombre del programa** → se prueba `generate_audio`
  con el mismo texto y ahí sí se corre la Ronda A para elegir motor.
- **Queda "casi"** → se compara contra la versión TTS del mismo capítulo antes
  de decidir. Es un solo audio más y evita casarse con el camino equivocado.

## Antes de gastar

`voice_change` cobra. **No pongas `use_unlim`** salvo que quieras usar las
generaciones ilimitadas: dejándolo sin poner, el servidor pregunta antes de
gastar en vez de decidir solo. Y `models_explore` reportó que no hay ilimitadas
disponibles, así que todo sale del saldo.
