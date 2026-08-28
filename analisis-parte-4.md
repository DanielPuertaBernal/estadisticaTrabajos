# Parte 4 — Análisis bivariado y correlación

## Ejercicio 8 — Análisis

**Resultados:** matriz de correlación de Pearson entre `danceability`, `energy`,
`valence` y `loudness`.

| | danceability | energy | valence | loudness |
|---|---|---|---|---|
| **danceability** | 1.000 | −0.104 | 0.403 | −0.033 |
| **energy** | −0.104 | 1.000 | 0.334 | 0.651 |
| **valence** | 0.403 | 0.334 | 1.000 | 0.232 |
| **loudness** | −0.033 | 0.651 | 0.232 | 1.000 |

De las seis relaciones posibles, cinco son positivas y solo dos superan 0.4. La
más fuerte es `energy`-`loudness` con r = +0.651, seguida de
`danceability`-`valence` con +0.403. En el extremo opuesto, `danceability`
frente a `energy` (−0.104) y frente a `loudness` (−0.033) son relaciones
prácticamente nulas: que una canción sea intensa o suene fuerte no dice casi
nada sobre si es apta para bailar, un resultado contraintuitivo que conviene
señalar.

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

**Resultados:** el par más correlacionado en valor absoluto es
`energy`-`loudness`, con r = +0.651 y un coeficiente de determinación
r² = 0.424.

**Pregunta:** caracterice dirección, fuerza y forma. ¿La nube de puntos sugiere
una relación lineal o hay curvatura? ¿Observa valores atípicos que puedan estar
inflando el coeficiente? Cierre advirtiendo qué no permite concluir esta
correlación.

La **dirección** es positiva: a mayor energía percibida, mayor volumen promedio.
Como `loudness` se mide en decibelios negativos, "mayor" significa aquí más
cercano a cero. La **fuerza** es moderada a fuerte, pero lejos de ser
determinante: las dos variables comparten el 42.4 % de su variabilidad y el
57.6 % restante responde a factores que la relación no captura. En términos del
fenómeno, las canciones más enérgicas tienden a sonar considerablemente más
fuerte, con un margen de error amplio.

En cuanto a la **forma**, la nube no presenta curvatura apreciable: la recta de
ajuste sigue el centro de los puntos en todo el rango. Lo que sí se observa es
un estrechamiento en abanico, ya que la desviación estándar del volumen pasa de
3.52 dB en las canciones de baja energía a 1.31 dB en las de alta. La predicción
es por tanto más confiable en un extremo que en el otro.

Sí hay valores atípicos, visibles en la esquina inferior izquierda: piezas
acústicas como *I See Fire* de Ed Sheeran (−20.5 dB) o *Mad World* de Gary Jules
(−17.2 dB). Pero no están inflando el coeficiente, y conviene comprobarlo en vez
de suponerlo: al excluir las canciones por debajo de −15 dB, r pasa de 0.651 a
0.641. Tampoco son errores de medición, sino canciones legítimas que deben
registrar bajo volumen y baja energía.

Esta correlación no permite concluir causalidad. Que energía y volumen varíen
juntos no demuestra que subir el volumen vuelva más enérgica una canción, y
ambas pueden responder a decisiones de producción o convenciones de género que
este análisis no mide. Como el conjunto contiene únicamente éxitos de listas,
tampoco puede afirmarse nada sobre la música que no alcanzó ese estatus.
