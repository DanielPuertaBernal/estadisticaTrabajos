# Parte 3 — Visualización de datos

## Ejercicio 6 — Análisis

**Resultados:** histograma de `tempo` con 40 intervalos y una línea vertical
roja en la media, situada en 120.12 BPM. La mediana es 120.02 BPM.

**Pregunta:** ¿en qué rango de BPM se concentra la mayor parte del repertorio?
¿La distribución es unimodal o aparecen varias concentraciones? Si observa más
de un pico, proponga una explicación musical.

El repertorio se concentra entre 90 y 140 BPM, franja que reúne el 67.7 % de las
canciones; el 50 % central es aún más estrecho, entre 99 y 134 BPM. Fuera de esa
banda la densidad cae rápidamente: por debajo de 75 BPM hay 33 canciones y por
encima de 180 BPM menos de 50, sobre un total de 2000.

La distribución no es unimodal. Aparecen dos concentraciones claras, una
alrededor de 95-105 BPM y otra, la más alta del histograma, alrededor de 125-130
BPM, separadas por un valle en torno a 105-115 BPM. Lo relevante es que la media
y la mediana son casi idénticas y aun así no corresponden a ninguna de las dos
modas: la línea roja cae en el espacio entre ambos grupos. Describir el
repertorio como "canciones de unos 120 BPM" es estadísticamente correcto y
musicalmente engañoso, porque oculta que conviven dos repertorios rítmicos
distintos.

La explicación musical es que esos dos picos corresponden a tradiciones de
producción diferentes. La moda baja es el pulso habitual del hip-hop, el R&B y
la balada pop de tempo medio. La moda alta coincide con el tempo canónico de la
música de baile de raíz house y de la corriente EDM que dominó las listas en la
segunda mitad del periodo, donde los 128 BPM funcionan como estándar de
producción.

## Ejercicio 7 — Análisis

**Resultados:**

| | No explícitas | Explícitas |
|---|---|---|
| n | 1449 | 551 |
| mediana | 65.0 | 67.0 |
| media | 59.26 | 61.48 |
| desv. estándar | 21.57 | 20.64 |
| rango intercuartílico | 17.0 | 17.0 |

**Pregunta:** ¿hay una diferencia visual apreciable entre ambos grupos? Compare
medianas y dispersión, no solo la posición de las cajas. Advierta si los tamaños
de los dos grupos son muy desiguales y qué implica eso para la comparación.

No hay diferencia apreciable: las cajas se superponen casi por completo. Las
medianas difieren en apenas dos puntos sobre una escala de 0 a 100 —65 en las no
explícitas frente a 67 en las explícitas— y la dispersión es prácticamente
idéntica, con un rango intercuartílico de exactamente 17 en los dos grupos y
desviaciones estándar de 21.57 y 20.64. Los dos grupos no solo se centran en el
mismo lugar, sino que varían igual. La lectura es negativa y no por ello pobre:
el contenido explícito no separa a las canciones exitosas por su nivel de
popularidad.

Los grupos sí son de tamaños desiguales, 1449 canciones no explícitas frente a
551 explícitas. Con 551 observaciones la mediana del grupo menor sigue siendo
estable, así que la comparación de medianas es válida; el riesgo está en la
lectura visual. El grupo no explícito aparenta mayor dispersión porque muestra
más puntos atípicos por debajo, pero eso ocurre simplemente porque tiene 2.6
veces más canciones y, por tanto, más oportunidades de contener valores
extremos. Como el rango intercuartílico es idéntico, concluir que las canciones
no explícitas son más heterogéneas sería un error inducido por el tamaño de la
muestra. Por eso la comparación debe apoyarse en los estadísticos de dispersión
y no en la extensión aparente de bigotes y atípicos.
