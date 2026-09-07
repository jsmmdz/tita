# Referencias de audio

Los audios **no van en el repo**. Acá solo queda el registro de cuáles hay y
dónde están, para que se puedan volver a encontrar.

**Esta carpeta ya no es para muestras de clonación.** Desde el 2026-08-31 no
se clona ninguna voz. Lo que se registra acá son **los audios generados** de la
serie: dónde quedó cada pista, para poder volver a encontrarla al montar.

## Cómo se anota

| Ruta local | Duración | Capítulo | Personaje | Fecha |
|---|---|---|---|---|
| _(vacío)_ | | | | |

Ejemplo de cómo se llena una fila:

    ~/Audio/tita/01-medicina-tita.wav | 0:14 | 01-medicina | TITA (Giselle) | 2026-09-07

## Cómo se nombran los archivos

    <capítulo>-<personaje>.wav

`01-medicina-tita.wav`, `01-medicina-rol.wav`, `00-presentacion-tita.wav`.

Un archivo por personaje, no uno por capítulo: los diálogos se generan por
pista separada y se arman en el editor.

Y **cada archivo va también en `registro/bitacora.md`** con su `voice_id` y sus
parámetros. La ruta dice dónde está; la bitácora dice cómo se hizo. Sin las
dos, el audio no se puede repetir.

> PENDIENTE: no hay ningún audio generado todavía. Falta la Ronda A.
