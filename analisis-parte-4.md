# Parte 4 — Análisis bivariado y correlación

## Ejercicio 8 — Análisis

**Resultado — matriz de correlación de Pearson:**

| | danceability | energy | valence | loudness |
|---|---|---|---|---|
| danceability | 1.00 | -0.10 | 0.40 | -0.03 |
| energy | -0.10 | 1.00 | 0.33 | 0.65 |
| valence | 0.40 | 0.33 | 1.00 | 0.23 |
| loudness | -0.03 | 0.65 | 0.23 | 1.00 |

La relación más fuerte es entre `energy` y `loudness` que es de r = 0.65, las canciones más enérgicas tienden a sonar  más fuerte. Le sigue `danceability` y `valence` con r = 0.40, esta es  moderada las canciones más bailables tienden a ser también más alegres. En contraste, `danceability` y `loudness` casi no se relacionan con r = -0.03.

## Ejercicio 9 — Análisis

**Resultados:** mapa de calor de la matriz anterior, con paleta divergente
`coolwarm`, escala fijada entre −1 y 1 centrada en 0, y los coeficientes
anotados sobre cada celda.

Fijar la escala no es un detalle estético: garantiza que el blanco corresponda
siempre a correlación nula y que la intensidad del color sea comparable entre
celdas. Si la escala se ajustara automáticamente al rango de los datos, una
correlación débil podría aparecer con el mismo color intenso que una fuerte y la
lectura visual resultaría engañosa.

## Ejercicio 10 — Análisis

**Resultado:** el par con correlación más fuerte en valor absoluto es `energy` – `loudness` con r = 0.65.

**Pregunta:** caracterice dirección, fuerza y forma. ¿Sugiere relación lineal o hay curvatura? ¿Hay atípicos que inflen el coeficiente? ¿Qué no permite concluir esta correlación?

La relación es positiva y tiene una fuerza moderada-alta,  a mayor energía, mayor volumen promedio de la canción. La nube de puntos sigue una tendencia lineal razonablemente clara, sin una curvatura marcada. Sí se ven algunos atípicos abajo a la izquierda, canciones acústicas muy suaves como *I See Fire* de Ed Sheeran (-20.5 dB) o *Mad World* de Gary Jules (-17.2 dB), pero no están inflando el coeficiente: si se sacan, r apenas baja de 0.65 a 0.64.

Lo que no permite concluir esta correlación es que  no se puede afirmar que una canción suene más fuerte porque es enérgica y tampoco lo contrario Solo indica que ambas variables tienden a moverse juntas en el catálogo; la explicación real puede deberse a decisiones conjuntas de producción y mezcla que afectan ambos atributos a la vez.
