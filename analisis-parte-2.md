# Parte 2 — Estadística descriptiva univariada · Análisis

Taller 07 — Estadística descriptiva y EDA
Fuente: `data/07 - canciones.csv` (2000 registros, 18 columnas).

> Borrador de trabajo. Verifiquen cada cifra contra la salida de `main.py` y
> redáctenlo con sus palabras antes de entregar.

---

# Ejercicio 3 — Duración en minutos

La columna `duration_min` se obtiene dividiendo `duration_ms` entre **60 000**,
que es el producto de los 1000 milisegundos de un segundo por los 60 segundos de
un minuto.

Verificación rápida sobre la primera fila: *Oops!...I Did It Again* registra
211 160 ms, que equivalen a 3.52 minutos. Es una duración plausible para una
canción pop; si el resultado hubiera dado 211 o 0.06, el factor de conversión
estaría equivocado.

---

# Ejercicio 4 — Medidas de tendencia central y dispersión

## Resultados

| Variable | Media | Mediana | Desv. est. | Mínimo | Máximo |
|---|---|---|---|---|---|
| `duration_min` | 3.812 | 3.721 | 0.652 | 1.883 | 8.069 |
| `popularity` | 59.872 | 65.500 | 21.336 | 0.000 | 89.000 |
| `danceability` | 0.667 | 0.676 | 0.140 | 0.129 | 0.975 |

## Pregunta 1 — ¿Qué indica la diferencia entre media y mediana de `popularity`?

**Respuesta: que la distribución es marcadamente asimétrica hacia la izquierda.**

La media (59.87) queda **5.63 puntos por debajo** de la mediana (65.50). Ese
orden —media menor que mediana— es la firma de una cola larga hacia los valores
bajos, y el coeficiente de asimetría lo confirma con un valor de **−1.824**, muy
lejos del cero que correspondería a una distribución simétrica.

En términos del fenómeno: la mayoría de las canciones del catálogo se agrupa en
niveles de popularidad altos —el 50 % central va de 56 a 73—, pero existe un
grupo minoritario de canciones con valores muy bajos que arrastra el promedio
hacia abajo. La media no se desplaza porque el repertorio sea heterogéneo, sino
porque unos pocos valores extremos pesan sobre ella.

**El origen de esa cola es identificable.** 126 canciones registran
`popularity` exactamente igual a **0**, y 184 quedan por debajo de 20. Que una
canción que figuró entre los éxitos de las listas globales tenga popularidad
cero no es una medición creíble: lo más probable es que el 0 esté funcionando
como marcador de dato faltante, no como una popularidad real nula. Si se
excluyen esos 126 registros, la media sube de 59.87 a 63.90 y se acerca a la
mediana.

## Pregunta 2 — ¿Qué medida reportaría para describir la popularidad "típica"?

**Respuesta: la mediana, 65.5.**

Tres razones, en orden de peso:

1. **La media está contaminada.** Los 126 ceros son casi con seguridad datos
   faltantes codificados como valor numérico. La media los incorpora como si
   fueran mediciones legítimas y baja casi 6 puntos por su culpa; la mediana,
   al depender únicamente de la posición central, apenas se inmuta.
2. **La distribución es asimétrica.** La media solo representa bien a un
   individuo típico cuando la distribución es aproximadamente simétrica. Con una
   asimetría de −1.824 esa condición no se cumple.
3. **La mediana describe mejor el caso central.** Decir "la canción típica de
   este catálogo tiene una popularidad de 65" es una afirmación que se sostiene
   al mirar los datos; decir 60 describe un punto por debajo del cual está
   claramente menos de la mitad del repertorio.

### Nota sobre las otras dos variables

- **`duration_min`** presenta el patrón inverso: media (3.81) ligeramente
  **por encima** de la mediana (3.72), con asimetría positiva de +1.019. La
  cola larga está aquí en las canciones extensas, que llegan hasta 8.07
  minutos, mientras que el mínimo se detiene en 1.88. Aun así la desviación
  estándar es de apenas 0.65 minutos: la duración de los éxitos es notablemente
  homogénea, alrededor de tres minutos y medio.
- **`danceability`** es la más simétrica de las tres (media 0.667 frente a
  mediana 0.676, asimetría −0.428) y en ella la media sí resulta un resumen
  razonable.

---

# Ejercicio 5 — Géneros más frecuentes y canciones explícitas

## Resultados

**Top 5 géneros:**

| Género | Canciones | % de las canciones con género |
|---|---|---|
| pop | 1633 | 82.6 % |
| hip hop | 778 | 39.3 % |
| R&B | 452 | 22.9 % |
| Dance/Electronic | 390 | 19.7 % |
| rock | 234 | 11.8 % |

Los porcentajes suman más de 100 % de manera deliberada: una canción puede
pertenecer a varios géneros y por tanto se cuenta en cada uno de ellos.

**Canciones explícitas: 551 de 2000, es decir el 27.6 %.**

## Criterio adoptado para las celdas con varios géneros

El problema es real y afecta a la mayoría del conjunto: **1279 de las 2000
celdas (64 %) contienen más de un género** separado por comas. Tratadas como
texto literal, esas celdas producen 59 categorías distintas.

**Decisión: separar cada celda en géneros individuales y contar cada aparición.**

La justificación es que el enunciado pide los géneros más frecuentes, no las
combinaciones más frecuentes. Si se contara la combinación completa como
categoría, el resultado sería engañoso: el conteo colocaría `pop` en primer
lugar con 428 canciones, y trataría `hip hop, pop` (277) y `hip hop, pop, R&B`
(244) como categorías ajenas. Se ocultaría así el hecho central del catálogo:
el pop aparece en 1633 canciones, más de ocho de cada diez. La fragmentación
repartiría un mismo género entre docenas de categorías y ninguna alcanzaría a
representarlo.

La ruta alternativa —contar combinaciones completas— es defendible si la
pregunta de investigación fuera qué mezclas de géneros predominan, porque
`hip hop, pop` es una identidad estilística distinta de cada uno por separado.
No es lo que se pregunta aquí.

**Costo de la decisión, que conviene declarar:** al separar, la suma de las
frecuencias (3648 apariciones) excede el número de canciones (2000), de modo que
los porcentajes ya no forman una partición del conjunto y no pueden sumarse
entre sí. Cada porcentaje debe leerse por separado: "el 82.6 % de las canciones
incluye pop entre sus géneros".

## Tratamiento del valor `set()`

22 canciones registran el literal **`set()`** en la columna `genre`. No es un
género musical: es la representación textual de un conjunto vacío de Python que
quedó escrita en el archivo durante la construcción del conjunto de datos. Es
decir, un dato faltante que no aparece como nulo y que `isna()` no detecta.

Esas 22 canciones se excluyen del conteo de géneros. En consecuencia, los
porcentajes de la tabla se calculan sobre las **1978 canciones con género
identificado**, no sobre las 2000. Incluirlas habría producido un "género"
`set()` en el puesto octavo del ranking.

Este caso ilustra por qué el ejercicio 2 no puede resolverse solo con
`isna().sum()`: hay datos faltantes que llegan disfrazados de texto válido y que
únicamente se detectan inspeccionando los valores de cada variable categórica.

---

## Advertencia común a toda la parte

El conjunto contiene **59 filas duplicadas exactas** sobre 2000 registros
(≈ 3 %). Ninguna de las medidas de esta parte las excluye. El enunciado no pide eliminarlas, solo
detectarlas y justificar; se conservan las 2000 filas. Su efecto sobre los
estadisticos es despreciable (ver `analisis-parte-1.md`).
