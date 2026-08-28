# Parte 2 — Estadística descriptiva univariada

## Ejercicio 3 — Duración en minutos

`duration_min` se obtiene dividiendo `duration_ms` entre 60 000, producto de los
1000 milisegundos de un segundo por los 60 segundos de un minuto. La primera
canción, con 211 160 ms, queda en 3.52 minutos: una duración plausible que
confirma que el factor de conversión es correcto.

## Ejercicio 4 — Media frente a mediana de `popularity`

La media de `popularity` es 59.87 y la mediana 65.5. Que la media quede casi seis
puntos **por debajo** de la mediana indica una distribución asimétrica hacia la
izquierda, con una cola larga de valores bajos; el coeficiente de asimetría lo
confirma con −1.824. La mayoría del catálogo se concentra en niveles de
popularidad altos —el 50 % central va de 56 a 73—, pero un grupo minoritario de
canciones con valores muy bajos arrastra el promedio hacia abajo. El origen de
esa cola es identificable: 126 canciones registran popularidad exactamente 0,
valor que funciona como marcador de dato faltante y no como una medición real.

**Para describir la popularidad típica con un solo número reportaría la
mediana, 65.5.** La media está contaminada por esos 126 ceros, que incorpora
como si fueran mediciones legítimas; la mediana, al depender solo de la posición
central, apenas se altera. Además, la media únicamente representa bien al caso
típico cuando la distribución es aproximadamente simétrica, condición que aquí
no se cumple. De las otras dos variables, `duration_min` muestra el patrón
inverso —media ligeramente por encima de la mediana, con cola hacia las
canciones largas— y `danceability` es prácticamente simétrica, de modo que en
ella la media sí resulta un resumen razonable.

## Ejercicio 5 — Géneros más frecuentes y canciones explícitas

Los cinco géneros más frecuentes son pop (1633 canciones, 82.6 %), hip hop
(778, 39.3 %), R&B (452, 22.9 %), Dance/Electronic (390, 19.7 %) y rock (234,
11.8 %). Las canciones explícitas son 551 de 2000, es decir el **27.6 %**.

**Criterio adoptado con los géneros compuestos:** se separó cada celda en
géneros individuales y se contó cada aparición. El problema afecta a la mayoría
del conjunto —1279 de las 2000 celdas contienen más de un género separado por
comas— y la razón de separar es que el enunciado pide los géneros más
frecuentes, no las combinaciones más frecuentes. Contar la combinación completa
como categoría habría tratado `hip hop, pop` y `hip hop, pop, R&B` como
categorías ajenas al pop, ocultando que el pop aparece en 1633 canciones, más de
ocho de cada diez. El costo de la decisión, que conviene declarar, es que los
porcentajes ya no suman 100 % y deben leerse por separado. Aparte, las 22
canciones cuyo género es `set()` se excluyeron por tratarse de un dato faltante
y no de un género, por lo que los porcentajes se calculan sobre las 1978
canciones con género identificado.
