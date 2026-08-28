# Parte 1 — Ingesta y limpieza inicial

## Ejercicio 1 — Carga y primeras filas

Se carga `data/07 - canciones.csv` con `pandas.read_csv()` y se inspeccionan las
primeras cinco filas. Se usa el `.csv` y no el `.xlsx` porque solo el primero
incluye la columna `explicit`, necesaria en los ejercicios 5 y 7.

## Ejercicio 2 — Análisis

**Resultados:** 2000 filas, 18 columnas, 0 valores nulos en todas las columnas.

**Pregunta:** ¿el conjunto requiere limpieza antes de continuar?

Sí, aunque `isna()` no marque nulos. Hay problemas de calidad que no se detectan
como "faltantes" pero sí condicionan el análisis:

- 59 filas duplicadas exactas tienen el mismo artista, canción y todos sus
  atributos.
- 126 canciones con `popularity = 0`, un 0 en un éxito global que no es tan
  creíble. Hay canciones que aparecen dos veces, una con 0 y otra con una
  popularidad real, por ejemplo *Hotline Bling* con 0 y con 77. El 0 es un dato
  faltante que no es tan claro, no una medición.
- 22 filas con `genre = "set()"`, texto residual de Python que no es un género
  real.
- `key` y `mode` son categorías codificadas como números, que son tonalidad y
  modo musical y no cantidades, por lo que no tiene sentido calcular su media.

La decisión fue no eliminar filas, ya que su efecto sobre las medidas es mínimo
—menos del 3 % del conjunto de los datos— y no cambia ninguna conclusión del
taller.
