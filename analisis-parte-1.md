# Parte 1 — Ingesta y limpieza inicial · Análisis

Taller 07 — Estadística descriptiva y EDA
Fuente: `data/07 - canciones.csv` (2000 registros, 18 columnas).

> Borrador de trabajo. Verifiquen cada cifra contra la salida de `main.py` y
> redáctenlo con sus palabras antes de entregar.

---

# Ejercicio 1 — Carga y primeras filas

El archivo se carga con `pandas.read_csv()` y se inspeccionan las primeras cinco
filas con `df.head()`.

Se usa el `.csv` y no el `.xlsx` porque solo el primero incluye la columna
`explicit`, indispensable para los ejercicios 5 y 7.

---

# Ejercicio 2 — Estructura, tipos y valores nulos

## Resultados

- **Dimensiones:** 2000 filas × 18 columnas.
- **Valores nulos:** **0** en todas las columnas.
- **Tipos de datos:** 2 columnas de texto (`artist`, `song`), 1 booleana
  (`explicit`), 1 de texto multivaluada (`genre`), 5 enteras (`duration_ms`,
  `year`, `popularity`, `key`, `mode`) y 9 de punto flotante (los atributos de
  audio).

## Pregunta — ¿Requiere limpieza el conjunto antes de continuar?

**Respuesta: sí. `isna()` no reporta un solo nulo, y aun así el conjunto tiene
cuatro problemas de calidad que condicionan todo lo que viene después.**

Este es el punto central del ejercicio. La verificación de nulos devuelve cero y
la conclusión intuitiva sería "el conjunto está limpio". Esa conclusión es
falsa. `isna()` solo detecta ausencias declaradas como tales; los datos
faltantes de este archivo llegan disfrazados de valores válidos y ninguna
función automática los señala.

### Problema 1 — 59 filas duplicadas exactas

`df.duplicated().sum()` devuelve **59**. Son 118 filas involucradas, agrupadas
en 59 pares idénticos en las 18 columnas: mismo artista, misma canción, mismo
año, mismos atributos de audio. Ejemplos: *Love Me Harder* de Ariana Grande,
*Suga Suga* de Baby Bash, *lovely* de Billie Eilish.

**Consecuencia:** cada una de esas 59 canciones pesa el doble en toda medida
posterior. Afecta las medias y medianas del ejercicio 4, las frecuencias de
género del 5, los histogramas y boxplots de la Parte 3 y la matriz de
correlación de la Parte 4. Es un 3 % del conjunto contado dos veces.

### Problema 2 — 126 canciones con `popularity` igual a 0

Un índice de popularidad de exactamente cero en una canción que figuró entre los
éxitos de las listas globales no es una medición creíble. Todo indica que el 0
funciona como marcador de dato faltante.

**Esto no es una suposición; el propio conjunto lo demuestra.** Existen cinco
canciones que aparecen en dos filas distintas con idénticos atributos de audio y
popularidades incompatibles entre sí:

| Canción | Artista | Popularidad fila A | Popularidad fila B |
|---|---|---|---|
| Here | Alessia Cara | 0 | 66 |
| Hotline Bling | Drake | 0 | 77 |
| Jumpman | Drake | 0 | 72 |
| Stole the Show | Kygo | 0 | 74 |
| Team | Lorde | 0 | 76 |

La misma canción no puede tener popularidad 0 y 77 simultáneamente. El 0 no
mide impopularidad: señala que el dato no se registró.

**Consecuencia:** esos 126 registros arrastran la media de `popularity` de 63.90
a 59.87 y producen la asimetría de −1.824 analizada en el ejercicio 4. También
generan la cola de atípicos inferiores del boxplot del ejercicio 7.

### Problema 3 — 22 canciones con `genre` igual a `"set()"`

El literal `set()` es la representación textual de un conjunto vacío de Python,
que quedó escrita en el archivo durante la construcción del conjunto de datos.
No es un género musical: es un dato faltante convertido en texto.

**Consecuencia:** `isna()` no lo detecta porque es una cadena válida. Si no se
excluye, aparece como un "género" en el ranking del ejercicio 5.

### Problema 4 — `key` y `mode` tienen tipo numérico pero son categóricas

`key` toma los 12 valores enteros de 0 a 11, correspondientes a los doce
semitonos de la escala cromática. `mode` toma 0 y 1, que codifican modo menor y
mayor. Ambas están tipadas como `int64`.

**Consecuencia:** cualquier operación aritmética sobre ellas carece de sentido.
La media de `key` no significa nada: no existe una "tonalidad promedio", y la
distancia entre la tonalidad 2 y la 4 no es el doble que entre la 2 y la 3. Por
eso ninguna de las dos se incluye en las medidas del ejercicio 4 ni en la matriz
de correlación de la Parte 4.

### Observación adicional — el rango de años no coincide con el enunciado

El enunciado describe canciones publicadas entre 2000 y 2019. La columna `year`
abarca en realidad de **1998 a 2020**, con 42 canciones fuera del rango
declarado: 1 de 1998, 38 de 1999 y 3 de 2020. No es un error de los datos, pero
sí una discrepancia con la documentación que conviene registrar.

## ¿Hay que ejecutar la limpieza?

**No, y conviene ser preciso sobre lo que pide el enunciado.** El ejercicio 2
dice: "**Indique** si el conjunto requiere alguna limpieza antes de continuar y
**justifique** su respuesta". Pide detectar y argumentar, no ejecutar. Las
palabras "duplicados" y "eliminar" no aparecen en ningún punto del taller, y la
rúbrica del Criterio 1 solo exige cargar el archivo, describir la estructura,
verificar nulos y crear `duration_min`.

Detectar los cuatro problemas anteriores es por tanto la respuesta completa al
ejercicio. Aplicar las correcciones sería trabajo adicional no solicitado.

**Además, hacerlo no cambiaría las conclusiones.** Los 59 duplicados son el 3 %
del conjunto y su efecto sobre los estadísticos es despreciable:

| Medida | Con duplicados | Sin duplicados |
|---|---|---|
| Media de `popularity` | 59.87 | 59.63 |
| Mediana de `popularity` | 65.5 | 65.0 |
| Media de `duration_min` | 3.8125 | 3.8099 |
| Media de `tempo` | 120.12 | 120.16 |
| % de canciones explícitas | 27.55 % | 27.67 % |
| r entre `energy` y `loudness` | 0.6510 | 0.6520 |

Ninguna interpretación de las Partes 2, 3 o 4 se altera: la asimetría de
`popularity` sigue siendo negativa y pronunciada, el histograma de `tempo` sigue
siendo bimodal y la correlación entre energía y volumen sigue siendo moderada y
positiva.

**Decisión adoptada: conservar las 2000 filas y documentar los cuatro
problemas.** Todos los estadísticos de este trabajo están calculados sobre el
conjunto completo, sin modificaciones.

## Cómo tratar cada problema sin borrar filas

Los dos casos de datos faltantes disfrazados sí requieren una decisión
explícita en los ejercicios donde intervienen, y esa decisión se tomó así:

- **Los 22 `set()` de `genre`** se excluyen del conteo del ejercicio 5, de modo
  que los porcentajes se calculan sobre las 1978 canciones con género
  identificado. No se elimina la fila: esas canciones conservan atributos de
  audio válidos que sí se usan en los ejercicios 6, 8, 9 y 10.
- **Los 126 ceros de `popularity`** motivan reportar la mediana en lugar de la
  media en el ejercicio 4, ya que la mediana resiste su efecto. Tampoco se
  eliminan las filas, por la misma razón.
- **`key` y `mode`** se mantienen fuera de todo cálculo aritmético.

Borrar una fila completa por un solo campo defectuoso descartaría las otras
diecisiete variables válidas de esa canción.
