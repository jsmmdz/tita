# Guion base — pruebas de voz

Líneas fijas para probar y comparar. La gracia es que **siempre sean las
mismas**: si cambias el guion entre pruebas, no sabes si mejoró la voz o
mejoró la frase.

Cada línea ataca una cosa distinta de la voz.

## L1 — Saludo (calidez, primera impresión)

> ¡Hola! Yo soy Tita, y esta es tu casa: la Universidad El Bosque.

## L2 — Frase larga (respiración y ritmo)

> Aquí vas a encontrar gente que te acompaña, profesores que te escuchan y un
> campus que se siente distinto apenas entras por la portería.

## L3 — Entusiasmo (energía alta sin gritar)

> ¡Vamos, que esto apenas empieza!

## L4 — Instrucción (claridad, tono neutro)

> Para inscribirte, entra a la página, busca tu programa y sigue los pasos.

## L5 — Números y siglas (donde los TTS se caen)

> Te espero el 15 de febrero, a las 8 de la mañana, en el edificio El Campito.

## L6 — Pausa y remate (control del silencio)

> ¿Sabes qué es lo mejor de todo? Que ya estás aquí.

---

## Cómo se usa

Se genera **el bloque completo, las seis líneas**, con los mismos parámetros.
Se escuchan seguidas. Se anota el veredicto por línea en la bitácora, no un
"quedó bien" general — casi siempre hay una o dos líneas que delatan el
problema mientras el resto suena aceptable.

## Notas de escritura

- Español de Colombia, tuteo.
- Sin emojis ni símbolos raros en el `prompt`: el modelo intenta leerlos.
- Los signos de puntuación **sí** importan: las comas y los puntos son lo que
  controla las pausas. Si una pausa queda mal, primero mueve la puntuación,
  después toca `speech_rate`.

> PENDIENTE: estas líneas son un punto de partida. Falta que alguien de la
> Universidad valide que Tita habla así — si hay tono de marca definido, este
> guion se reescribe según eso.
