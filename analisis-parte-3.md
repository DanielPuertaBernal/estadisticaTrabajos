# Parte 3 — Visualización de datos · Análisis

Taller 07 — Estadística descriptiva y EDA
Fuente: `data/07 - canciones.csv` (2000 registros, 18 columnas).
Figuras producidas por `main.py` (se muestran en ventana; no se guardan a disco).

> Borrador de trabajo. Verifiquen cada cifra contra la salida de `main.py` y
> redáctenlo con sus palabras antes de entregar.

---

# Ejercicio 6 — Histograma de `tempo`

**Figura:** histograma de `tempo` producido por el ejercicio 6 de `main.py`.

## Evidencia numérica

| Medida | Valor |
|---|---|
| n | 2000 canciones |
| Media | 120.12 BPM |
| Mediana | 120.02 BPM |
| Desviación estándar | 26.97 BPM |
| Mínimo / Máximo | 60.02 / 210.85 BPM |
| Q1 / Q3 | 99.0 / 134.3 BPM |
| Rango intercuartílico | 35.3 BPM |
| Coeficiente de asimetría | +0.547 |

Conteos por intervalos de 5 BPM en la zona central:

| Intervalo (BPM) | Canciones |
|---|---|
| 90 – 95 | 133 |
| 95 – 100 | **180** |
| 100 – 105 | 138 |
| 105 – 110 | 57 |
| 110 – 115 | 91 |
| 115 – 120 | 121 |
| 120 – 125 | 177 |
| 125 – 130 | **240** |
| 130 – 135 | 105 |

---

## Pregunta 1 — ¿En qué rango de BPM se concentra la mayor parte del repertorio?

**Respuesta: entre 90 y 140 BPM, franja que reúne el 67.7 % de las canciones.**

El 50 % central del repertorio es todavía más estrecho: queda entre 99 y 134 BPM
(Q1 y Q3), con un rango intercuartílico de apenas 35.3 BPM. Es decir, una de
cada dos canciones exitosas del periodo cabe en una ventana de 35 pulsos por
minuto.

Fuera de esa banda la densidad cae con rapidez. Por debajo de 75 BPM hay 33
canciones y por encima de 180 BPM menos de 50, sobre un total de 2000. El
repertorio de éxitos globales es, en materia de tempo, mucho más homogéneo de lo
que sugiere su rango total de 60 a 211 BPM.

## Pregunta 2 — ¿La distribución es unimodal o aparecen varias concentraciones?

**Respuesta: es claramente bimodal. Aparecen dos concentraciones separadas por un
valle.**

- Primera moda alrededor de **95 – 105 BPM**, con su punto más alto en el
  intervalo 95 – 100 (180 canciones).
- Segunda moda alrededor de **125 – 130 BPM**, el pico más alto de todo el
  histograma (240 canciones).
- Entre ambas, un valle en torno a **105 – 115 BPM**, donde el conteo baja a 57
  y 91 canciones por intervalo: menos de la mitad del pico principal.

Aquí conviene detenerse en algo que el histograma revela y las medidas de
resumen esconden. La media (120.12 BPM) y la mediana (120.02 BPM) son
prácticamente idénticas, lo que aisladamente haría pensar en una distribución
simétrica y bien resumida por un solo número. **Pero ese centro no corresponde a
ninguna de las dos modas.** La línea roja del histograma cae en el espacio que
separa los dos grupos de canciones.

La conclusión es que describir el repertorio como "canciones de unos 120 BPM"
es estadísticamente correcto y musicalmente falso: oculta que conviven dos
repertorios rítmicos distintos, ninguno de los cuales suena a 120 BPM. Cuando
una distribución es bimodal, la media deja de representar a un individuo típico
y pasa a describir un punto donde casi no hay observaciones características.

La asimetría positiva (+0.547) añade un matiz: hay una cola derecha larga —unas
pocas canciones llegan a 210 BPM— sin contrapeso equivalente por la izquierda,
donde el mínimo se detiene en 60 BPM.

## Pregunta 3 — Explicación musical de los dos picos

**Respuesta: los dos picos corresponden a dos tradiciones de producción
distintas que convivieron en las listas globales del periodo cubierto (1998-2020).**

- **La moda baja (95 – 105 BPM)** es el pulso habitual del hip-hop, el R&B y la
  balada pop de tempo medio. Son estilos con presencia sostenida en las listas
  durante todo el periodo, y ese rango de tempo es el que permite acomodar
  fraseos vocales densos sin que la métrica se vuelva atropellada.
- **La moda alta (125 – 130 BPM)** es el tempo canónico de la música de baile de
  raíz house y de la corriente EDM que dominó el pop de listas, sobre todo en la
  segunda mitad del periodo. Los 128 BPM funcionan como estándar de producción
  en ese repertorio —facilitan la mezcla continua entre pistas—, lo que explica
  que sea el pico más pronunciado del histograma.

El valle intermedio de 105 – 115 BPM no responde a ninguna imposibilidad
musical: es simplemente una zona que ninguna de las dos tradiciones reclama como
propia.

**Advertencia sobre la cola derecha.** Los algoritmos de estimación automática
de tempo tienden a duplicar o dividir el pulso real cuando la subdivisión
rítmica es ambigua. Parte de las canciones registradas entre 160 y 175 BPM
podrían ser en realidad temas de 80 a 88 BPM medidos a doble tiempo. Es una
limitación del procedimiento de medición, no un rasgo del repertorio, y conviene
mencionarla antes de sacar conclusiones sobre las canciones más rápidas.

---

# Ejercicio 7 — Boxplot de `popularity` según `explicit`

**Figura:** boxplot producido por el ejercicio 7 de `main.py`.

## Evidencia numérica

| Grupo | n | Mediana | Media | Desv. est. | Q1 | Q3 | RIC |
|---|---|---|---|---|---|---|---|
| No explícita | 1449 | 65.0 | 59.26 | 21.57 | 56.0 | 73.0 | **17.0** |
| Explícita | 551 | 67.0 | 61.48 | 20.64 | 57.0 | 74.0 | **17.0** |

Canciones explícitas: 27.6 % del total.

---

## Pregunta 1 — ¿Hay una diferencia visual apreciable entre ambos grupos?

**Respuesta: no. Las dos cajas se superponen casi por completo.**

La caja de las canciones explícitas está desplazada apenas un punto hacia
arriba respecto a la de las no explícitas (Q1 de 57 frente a 56, Q3 de 74 frente
a 73). Sobre una escala de popularidad de 0 a 100, ese corrimiento es
indistinguible a simple vista y carece de significado práctico.

La lectura correcta de este gráfico es negativa, y eso no lo vuelve un
resultado pobre: **el contenido explícito no separa a las canciones exitosas por
su nivel de popularidad.** Si alguien esperaba que las canciones explícitas
fueran sistemáticamente más o menos populares, los datos no respaldan esa
expectativa.

## Pregunta 2 — Comparación de medianas y dispersión

**Respuesta: las medianas difieren en 2 puntos y la dispersión es prácticamente
idéntica.**

- **Medianas:** 65 en las no explícitas frente a 67 en las explícitas. Una
  diferencia de 2 puntos sobre 100, con muestras de este tamaño, no sostiene
  ninguna afirmación sobre el fenómeno.
- **Dispersión:** el rango intercuartílico es **exactamente 17 en ambos
  grupos**, y las desviaciones estándar son casi iguales (21.57 y 20.64). Los
  dos grupos no solo se centran en el mismo lugar: se dispersan igual.

Conviene mirar también la brecha entre media y mediana. En ambos grupos la media
queda por debajo de la mediana (59.26 frente a 65, y 61.48 frente a 67), señal de
asimetría hacia la izquierda provocada por la cola inferior. El origen de esa
cola es concreto: **126 canciones tienen `popularity` igual a 0** (93 no
explícitas y 33 explícitas). Que un éxito de listas globales registre
popularidad exactamente cero es implausible como medición real; lo más probable
es que el valor 0 esté funcionando como marcador de dato faltante. Esa es
justamente la razón por la que la mediana describe mejor estos grupos que la
media.

## Pregunta 3 — Tamaños de grupo desiguales y qué implican

**Respuesta: los grupos son desiguales (1449 frente a 551, razón 2.6 a 1), y esa
desigualdad distorsiona la comparación visual aunque no invalide las medianas.**

Con 551 observaciones, el grupo de canciones explícitas es suficientemente
grande para que su mediana sea estable; no estamos ante el caso en que un grupo
minúsculo produce estadísticos frágiles.

El problema está en otra parte, y es la trampa de este gráfico. En el boxplot,
el grupo de no explícitas **aparenta** mayor dispersión: su bigote inferior baja
hasta 32 (frente a 39 en el otro grupo) y muestra visiblemente más puntos
atípicos por debajo. La tentación es concluir que las canciones no explícitas
son más heterogéneas en popularidad. **Sería una conclusión falsa.** El rango
intercuartílico es idéntico en ambos grupos: 17. Lo que ocurre es que el grupo
no explícito tiene 2.6 veces más canciones y, por lo tanto, 2.6 veces más
oportunidades de contener valores extremos. Más observaciones producen más
atípicos visibles aunque la dispersión subyacente sea la misma.

De ahí la advertencia del enunciado sobre comparar cajas de tamaños muy
desiguales: la cantidad de puntos atípicos dibujados depende del tamaño del
grupo, no solo de su variabilidad. Por eso la comparación debe apoyarse en los
estadísticos de dispersión —rango intercuartílico y desviación estándar—, y no
en la extensión aparente de bigotes y atípicos.

**Lo que este gráfico no permite concluir.** Aun si la diferencia de 2 puntos
fuera real, no autorizaría ninguna afirmación causal: no diría que marcar una
canción como explícita la vuelva más popular. El conjunto solo contiene
canciones que ya fueron éxitos, de modo que nada puede decirse sobre el
repertorio que no llegó a las listas.

---

## Advertencia común a los dos ejercicios

El conjunto contiene **59 filas duplicadas exactas** sobre 2000 registros
(≈ 3 %). Ninguna figura de esta parte las excluye. El enunciado no pide eliminarlas, solo
detectarlas y justificar; se conservan las 2000 filas. Su efecto sobre los
estadisticos es despreciable (ver `analisis-parte-1.md`).
