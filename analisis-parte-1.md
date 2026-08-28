# Parte 1 — Ingesta y limpieza inicial

## Ejercicio 1 — Carga y primeras filas

Se carga `data/07 - canciones.csv` con `pandas.read_csv()` y se inspeccionan las
primeras cinco filas. Se usa el `.csv` y no el `.xlsx` porque solo el primero
incluye la columna `explicit`, necesaria en los ejercicios 5 y 7.

## Ejercicio 2 — ¿Requiere limpieza el conjunto?

**Sí.** La verificación de nulos devuelve cero en las 18 columnas, pero eso no
significa que el conjunto esté limpio: los datos faltantes de este archivo
llegan disfrazados de valores válidos y `isna()` no los detecta. Hay 59 filas
duplicadas exactas, 126 canciones con `popularity` igual a 0 y 22 con `genre`
igual a `"set()"`. Un índice de popularidad de exactamente cero en una canción
que figuró en las listas globales no es una medición creíble, y el propio
conjunto lo confirma: cinco canciones aparecen dos veces con atributos de audio
idénticos y popularidades de 0 frente a valores entre 66 y 77. El 0 no mide
impopularidad, señala que el dato no se registró. El literal `set()`, por su
parte, es un conjunto vacío de Python que quedó escrito como texto.

A esto se suma que `key` y `mode` están tipadas como enteros aunque codifican
categorías —las doce tonalidades y los modos menor y mayor—, por lo que
cualquier promedio sobre ellas carece de sentido y quedan excluidas de todo
cálculo. El enunciado pide indicar y justificar la necesidad de limpieza, no
ejecutarla, de modo que se conservan las 2000 filas: eliminar los duplicados
mueve los estadísticos menos de una décima y no altera ninguna conclusión. Lo
que sí se trata de forma explícita es cada dato faltante donde interviene —se
excluye `set()` del conteo de géneros y se reporta la mediana en lugar de la
media en el ejercicio 4—, sin borrar filas que conservan atributos de audio
válidos.
