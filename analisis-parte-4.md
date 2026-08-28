# Parte 4 — Análisis bivariado y correlación · Análisis

Taller 07 — Estadística descriptiva y EDA
Fuente: `data/07 - canciones.csv` (2000 registros, 18 columnas).

> Borrador de trabajo. Verifiquen cada cifra contra la salida de `main.py` y
> redáctenlo con sus palabras antes de entregar.

---

# Ejercicio 8 — Matriz de correlación de Pearson

| | danceability | energy | valence | loudness |
|---|---|---|---|---|
| **danceability** | 1.000 | −0.104 | 0.403 | −0.033 |
| **energy** | −0.104 | 1.000 | 0.334 | **0.651** |
| **valence** | 0.403 | 0.334 | 1.000 | 0.232 |
| **loudness** | −0.033 | 0.651 | 0.232 | 1.000 |

Pares ordenados por magnitud:

| Par | r | \|r\| |
|---|---|---|
| energy – loudness | +0.651 | **0.651** |
| danceability – valence | +0.403 | 0.403 |
| energy – valence | +0.334 | 0.334 |
| valence – loudness | +0.232 | 0.232 |
| danceability – energy | −0.104 | 0.104 |
| danceability – loudness | −0.033 | 0.033 |

Cinco de las seis relaciones son positivas y solo dos superan 0.4. Dos
resultados merecen mención antes de pasar al par más fuerte:

- **`danceability` y `valence` (+0.403).** Las canciones que transmiten más
  positividad emocional tienden a ser algo más bailables. Es una relación
  moderada, no una equivalencia.
- **`danceability` y `energy` (−0.104), y `danceability` y `loudness`
  (−0.033).** Prácticamente nulas. Que una canción sea intensa o suene fuerte
  no dice casi nada sobre si es apta para bailar: son dimensiones
  independientes del sonido. Es un resultado contraintuitivo que vale la pena
  señalar.

---

# Ejercicio 9 — Mapa de calor

La matriz se representó con `seaborn.heatmap` usando la paleta divergente
`coolwarm`, con la escala fijada entre −1 y 1 y centrada en 0, y con los
coeficientes anotados sobre cada celda.

Fijar `vmin=-1`, `vmax=1` y `center=0` no es un detalle estético: garantiza que
el blanco corresponda siempre a correlación nula, que el rojo signifique
positiva y el azul negativa, con la misma intensidad para magnitudes iguales.
Si la escala se ajustara automáticamente al rango de los datos, una correlación
débil de 0.2 podría aparecer con el mismo color intenso que una de 0.9 en otra
matriz, y la lectura visual resultaría engañosa.

La diagonal en rojo intenso (todos los valores 1.000) es un artefacto esperado:
cada variable correlaciona perfectamente consigo misma y no aporta información.

---

# Ejercicio 10 — Par más correlacionado: `energy` y `loudness`

**Par identificado: `energy` – `loudness`, con r = +0.651**, el único que supera
0.5 en valor absoluto.

Coeficiente de determinación: **r² = 0.424**. Las dos variables comparten el
42.4 % de su variabilidad; el 57.6 % restante responde a factores que esta
relación no captura.

## Dirección

**Positiva.** A mayor energía percibida, mayor volumen promedio. Como `loudness`
se mide en decibelios negativos, "mayor" significa aquí más cercano a cero. El
promedio de `loudness` sube de forma sostenida al avanzar por las franjas de
energía: −11.90 dB en las canciones de energía inferior a 0.3, hasta −3.99 dB en
las de energía superior a 0.9.

En lenguaje del fenómeno: **las canciones más enérgicas tienden a sonar
considerablemente más fuerte.**

## Fuerza

**Moderada a fuerte, pero lejos de ser determinante.** Un r de 0.651 marca una
tendencia clara y visible en la nube de puntos, no una correspondencia
mecánica. Conocer la energía de una canción permite anticipar aproximadamente
su volumen, pero con un margen de error amplio: para un mismo nivel de energía
conviven canciones separadas por varios decibelios.

## Forma

**Aproximadamente lineal, pero con dispersión desigual a lo largo del recorrido.**

La nube no muestra curvatura apreciable: la recta de ajuste sigue el centro de
los puntos en todo el rango sin desviarse sistemáticamente. Lo que sí presenta
es una forma de abanico —la dispersión se estrecha a medida que aumenta la
energía—, comprobable en la desviación estándar de `loudness` por franja:

| Franja de `energy` | n | Desv. est. de `loudness` |
|---|---|---|
| 0.00 – 0.30 | 17 | 3.52 dB |
| 0.30 – 0.45 | 95 | 1.97 dB |
| 0.45 – 0.60 | 323 | 1.58 dB |
| 0.60 – 0.75 | 641 | 1.41 dB |
| 0.75 – 0.90 | 700 | 1.31 dB |
| 0.90 – 1.00 | 224 | 1.44 dB |

La variabilidad del volumen se reduce a menos de la mitad al pasar de las
canciones de baja energía a las de alta. Las canciones enérgicas son
consistentemente fuertes; las de baja energía son mucho más heterogéneas en
volumen. Esto significa que la predicción es más confiable en un extremo que en
el otro, matiz que el coeficiente global no revela.

## Valores atípicos

Existen, y son visibles en la esquina inferior izquierda del diagrama:

| Canción | Artista | `energy` | `loudness` |
|---|---|---|---|
| I See Fire | Ed Sheeran | 0.055 | −20.51 dB |
| Mad World | Gary Jules | 0.058 | −17.22 dB |
| Nine Million Bicycles | Katie Melua | 0.247 | −15.64 dB |

**Pero no están inflando el coeficiente**, y conviene verificarlo en vez de
suponerlo. Al recalcular la correlación excluyendo las canciones por debajo de
−15 dB, r pasa de 0.6510 a **0.6405**: una variación de una centésima. La
relación no depende de esos puntos.

Además, no son errores de medición. Son piezas acústicas de tempo lento y
producción sobria, exactamente el tipo de canción que debe registrar baja
energía y bajo volumen. Son observaciones extremas pero legítimas, y eliminarlas
sería descartar información válida.

## Qué NO permite concluir esta correlación

**Primero: no implica causalidad.** Que energía y volumen varíen juntos no
demuestra que subir el volumen de una canción la vuelva más enérgica, ni lo
contrario. Ambas pueden responder a una tercera causa común —decisiones de
producción, convenciones de género, prácticas de masterización de la
industria— que este análisis no mide.

**Segundo, y específico de estos datos: las dos variables no son mediciones
independientes.** Ambas son atributos calculados automáticamente por el mismo
algoritmo de la plataforma, y el volumen figura entre los insumos con los que se
estima la energía percibida. Una parte de la correlación observada puede ser
consecuencia de cómo se define la variable, no de una propiedad del repertorio
musical. Es una advertencia que este conjunto de datos no permite resolver, pero
sí declarar.

**Tercero: el conjunto solo contiene éxitos.** Todas las canciones analizadas
figuraron en las listas globales, de modo que nada puede afirmarse sobre la
relación entre energía y volumen en la música que no alcanzó ese estatus.

---

## Advertencia común a toda la parte

El conjunto contiene **59 filas duplicadas exactas** sobre 2000 registros
(≈ 3 %), que no fueron excluidas. El enunciado no pide eliminarlas, solo
detectarlas y justificar; se conservan las 2000 filas. Su efecto sobre los
estadisticos es despreciable (ver `analisis-parte-1.md`).
