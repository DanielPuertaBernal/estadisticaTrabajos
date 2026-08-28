# Parte 2 — Estadística descriptiva univariada

## Ejercicio 3 — Duración en minutos

`duration_min` se obtiene dividiendo `duration_ms` entre 60 000, producto de los
1000 milisegundos de un segundo por los 60 segundos de un minuto. La primera
canción, con 211 160 ms, queda en 3.52 minutos: una duración plausible que
confirma que el factor de conversión es correcto.

## Ejercicio 4 — Análisis

**Resultados:**

| | duration_min | popularity | danceability |
|---|---|---|---|
| media | 3.81 | 59.87 | 0.667 |
| mediana | 3.72 | 65.50 | 0.676 |
| desv. estándar | 0.65 | 21.34 | 0.140 |
| mínimo | 1.88 | 0.00 | 0.129 |
| máximo | 8.07 | 89.00 | 0.975 |

**Pregunta:** compare media y mediana de `popularity`. ¿Qué indica esa
diferencia? ¿Cuál reportaría usted como valor "típico" y por qué?

La media (59.87) es menor que la mediana (65.5). Esa diferencia indica una
distribución con asimetría negativa: hay un grupo de canciones con popularidad
muy baja, incluyendo 126 casos en exactamente 0, que en realidad son datos
faltantes que aparecen como 0 y no canciones genuinamente sin popularidad. Ese
grupo arrastra la media hacia abajo, mientras la mayoría del catálogo se
concentra en valores más altos.

Reportaría la **mediana** como valor típico, porque no se ve afectada por esos
valores extremos bajos y refleja mejor dónde se agrupa realmente la mayor parte
de las canciones.

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
