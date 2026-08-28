# Parte 4 — Análisis bivariado y correlación

## Ejercicio 8 — Matriz de correlación

De las seis relaciones posibles entre `danceability`, `energy`, `valence` y
`loudness`, cinco son positivas y solo dos superan 0.4. La más fuerte es
`energy`–`loudness` con **r = +0.651**, seguida de `danceability`–`valence` con
+0.403. En el extremo opuesto, `danceability` frente a `energy` (−0.104) y frente
a `loudness` (−0.033) son relaciones prácticamente nulas: que una canción sea
intensa o suene fuerte no dice casi nada sobre si es apta para bailar, un
resultado contraintuitivo que conviene señalar.

## Ejercicio 9 — Mapa de calor

La matriz se representó con una paleta divergente (`coolwarm`), la escala fijada
entre −1 y 1 y centrada en 0, y los coeficientes anotados sobre cada celda.
Fijar la escala no es un detalle estético: garantiza que el blanco corresponda
siempre a correlación nula y que la intensidad del color sea comparable entre
celdas. Si la escala se ajustara automáticamente al rango de los datos, una
correlación débil podría aparecer con el mismo color intenso que una fuerte y la
lectura visual resultaría engañosa.

## Ejercicio 10 — Relación entre `energy` y `loudness`

El par más correlacionado en valor absoluto es `energy`–`loudness`, con
**r = +0.651** y un coeficiente de determinación r² = 0.424. La relación es de
**dirección positiva** —a mayor energía percibida, mayor volumen promedio, ya
que `loudness` se mide en decibelios negativos y "mayor" significa más cercano a
cero— y de **fuerza moderada a fuerte**, pero lejos de ser determinante: las dos
variables comparten el 42.4 % de su variabilidad y el 57.6 % restante responde a
factores que la relación no captura. En términos del fenómeno, las canciones más
enérgicas tienden a sonar considerablemente más fuerte, con un margen de error
amplio. En cuanto a la **forma**, la nube no presenta curvatura apreciable, pero
sí se estrecha en abanico: la desviación estándar del volumen pasa de 3.52 dB en
las canciones de baja energía a 1.31 dB en las de alta, de modo que la
predicción es más confiable en un extremo que en el otro.

Hay valores atípicos visibles en la esquina inferior izquierda —piezas acústicas
como *I See Fire* de Ed Sheeran (−20.5 dB) o *Mad World* de Gary Jules
(−17.2 dB)—, pero **no están inflando el coeficiente**: al excluir las canciones
por debajo de −15 dB, r pasa de 0.651 a 0.641. Tampoco son errores de medición,
sino canciones legítimas que deben registrar bajo volumen y baja energía.
Finalmente, esta correlación **no permite concluir causalidad**: que energía y
volumen varíen juntos no demuestra que subir el volumen vuelva más enérgica una
canción, y ambas pueden responder a decisiones de producción o convenciones de
género que este análisis no mide. Como el conjunto contiene únicamente éxitos de
listas, tampoco puede afirmarse nada sobre la música que no alcanzó ese estatus.
