# Parte 3 — Visualización de datos

## Ejercicio 6 — Análisis

**Resultado:** media de `tempo` ≈ 120.1 BPM (línea roja del histograma).

**Pregunta:** ¿en qué rango se concentra el repertorio? ¿Es unimodal o hay varios picos? Si hay más de uno, proponga una explicación musical.

La mayor parte de las canciones se concentra entre 90 y 140 BPM, con el pico más alto entre 125 y 130 BPM, tempo característico de la música de baile de raíz house y del EDM que dominó las listas en la segunda mitad del periodo.

La distribución no es estrictamente unimodal aparece una segunda concentración más baja, alrededor de 95-105 BPM. Una explicación musical razonable es la presencia de baladas, hip hop y canciones de R&B, géneros con tempos naturalmente más lentos que conviven en las listas de éxitos junto con el material más bailable.

Vale la pena notar que la media de 120.1 BPM no cae en ninguno de los dos picos, sino en el valle que los separa. Decir que "las canciones rondan los 120 BPM" es cierto en promedio pero engañoso: casi ninguna canción típica suena a ese tempo.

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
