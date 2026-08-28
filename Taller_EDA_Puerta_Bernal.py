# %% ============================================================================
# TALLER 07 - ESTADISTICA DESCRIPTIVA Y ANALISIS EXPLORATORIO DE DATOS (EDA)
# Curso: Estadistica III - Ingenieria de Sistemas
# Universidad Catolica de Oriente
# ==============================================================================

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

RUTA_DATOS = Path(__file__).resolve().parent / "data" / "07 - canciones.csv"

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", None)

sns.set_theme(style="whitegrid")


# %% ============================================================================
# PARTE 1 - INGESTA Y LIMPIEZA INICIAL
# ==============================================================================

print("\n" + "=" * 78)
print("  PARTE 1 - INGESTA Y LIMPIEZA INICIAL")
print("=" * 78)

# %% Ejercicio 1 - Cargue el conjunto de datos y muestre sus primeras 5 filas

print("\n--- Ejercicio 1: primeras 5 filas ---")

df = pd.read_csv(RUTA_DATOS)

print(df.head())

# ------------------------------------------------------------------------------
# ANALISIS - EJERCICIO 1
#
# Se carga el archivo con pandas.read_csv() y se inspeccionan las primeras cinco
# filas. Se usa el .csv y no el .xlsx porque solo el primero incluye la columna
# `explicit`, necesaria en los ejercicios 5 y 7.
# ------------------------------------------------------------------------------

# %% Ejercicio 2 - Resumen del DataFrame: dimensiones, tipos y valores nulos

print("\n--- Ejercicio 2: estructura, tipos y valores nulos ---")

filas, columnas = df.shape
print(f"Filas: {filas}")
print(f"Columnas: {columnas}")

print("\nTipos de datos:")
print(df.dtypes)

print("\nValores nulos por columna:")
print(df.isna().sum())
print(f"Total de valores nulos: {df.isna().sum().sum()}")

print(f"\nFilas duplicadas exactas: {df.duplicated().sum()}")
print(f"Canciones con popularity = 0: {(df['popularity'] == 0).sum()}")
print(f"Canciones con genre = 'set()': {(df['genre'] == 'set()').sum()}")

# ------------------------------------------------------------------------------
# ANALISIS - EJERCICIO 2: ¿requiere limpieza el conjunto?
#
# Si. La verificacion de nulos devuelve cero en las 18 columnas, pero eso no
# significa que el conjunto este limpio: los datos faltantes de este archivo
# llegan disfrazados de valores validos y isna() no los detecta. Hay 59 filas
# duplicadas exactas, 126 canciones con popularity igual a 0 y 22 con genre
# igual a "set()". Un indice de popularidad de exactamente cero en una cancion
# que figuro en las listas globales no es una medicion creible, y el propio
# conjunto lo confirma: cinco canciones aparecen dos veces con atributos de
# audio identicos y popularidades de 0 frente a valores entre 66 y 77. El 0 no
# mide impopularidad, senala que el dato no se registro. El literal "set()", por
# su parte, es un conjunto vacio de Python que quedo escrito como texto.
#
# A esto se suma que key y mode estan tipadas como enteros aunque codifican
# categorias -las doce tonalidades y los modos menor y mayor-, por lo que
# cualquier promedio sobre ellas carece de sentido y quedan excluidas de todo
# calculo. El enunciado pide indicar y justificar la necesidad de limpieza, no
# ejecutarla, de modo que se conservan las 2000 filas: eliminar los duplicados
# mueve los estadisticos menos de una decima y no altera ninguna conclusion. Lo
# que si se trata de forma explicita es cada dato faltante donde interviene -se
# excluye "set()" del conteo de generos y se reporta la mediana en lugar de la
# media en el ejercicio 4-, sin borrar filas que conservan atributos validos.
# ------------------------------------------------------------------------------


# %% ============================================================================
# PARTE 2 - ESTADISTICA DESCRIPTIVA UNIVARIADA
# ==============================================================================

print("\n" + "=" * 78)
print("  PARTE 2 - ESTADISTICA DESCRIPTIVA UNIVARIADA")
print("=" * 78)

# %% Ejercicio 3 - Cree la columna duration_min a partir de duration_ms

print("\n--- Ejercicio 3: duracion en minutos ---")

df["duration_min"] = df["duration_ms"] / 60000

print(df[["song", "duration_ms", "duration_min"]].head())

# ------------------------------------------------------------------------------
# ANALISIS - EJERCICIO 3
#
# duration_min se obtiene dividiendo duration_ms entre 60 000, producto de los
# 1000 milisegundos de un segundo por los 60 segundos de un minuto. La primera
# cancion, con 211 160 ms, queda en 3.52 minutos: una duracion plausible que
# confirma que el factor de conversion es correcto.
# ------------------------------------------------------------------------------

# %% Ejercicio 4 - Media, mediana, desviacion estandar, minimo y maximo

print("\n--- Ejercicio 4: medidas de tendencia central y dispersion ---")

variables = ["duration_min", "popularity", "danceability"]

resumen_4 = df[variables].agg(["mean", "median", "std", "min", "max"]).T
resumen_4.columns = ["media", "mediana", "desv_est", "minimo", "maximo"]

print(resumen_4.round(3))

print(f"\npopularity -> media {df['popularity'].mean():.2f} | "
      f"mediana {df['popularity'].median():.1f} | "
      f"diferencia {df['popularity'].mean() - df['popularity'].median():.2f}")
print(f"popularity -> coeficiente de asimetria: {df['popularity'].skew():.3f}")

# ------------------------------------------------------------------------------
# ANALISIS - EJERCICIO 4: media frente a mediana de popularity
#
# La media de popularity es 59.87 y la mediana 65.5. Que la media quede casi
# seis puntos POR DEBAJO de la mediana indica una distribucion asimetrica hacia
# la izquierda, con una cola larga de valores bajos; el coeficiente de asimetria
# lo confirma con -1.824. La mayoria del catalogo se concentra en niveles de
# popularidad altos -el 50 % central va de 56 a 73-, pero un grupo minoritario
# de canciones con valores muy bajos arrastra el promedio hacia abajo. El origen
# de esa cola es identificable: 126 canciones registran popularidad exactamente
# 0, valor que funciona como marcador de dato faltante y no como medicion real.
#
# Para describir la popularidad tipica con un solo numero reportaria la MEDIANA,
# 65.5. La media esta contaminada por esos 126 ceros, que incorpora como si
# fueran mediciones legitimas; la mediana, al depender solo de la posicion
# central, apenas se altera. Ademas, la media unicamente representa bien al caso
# tipico cuando la distribucion es aproximadamente simetrica, condicion que aqui
# no se cumple. De las otras dos variables, duration_min muestra el patron
# inverso -media ligeramente por encima de la mediana, con cola hacia las
# canciones largas- y danceability es practicamente simetrica, de modo que en
# ella la media si resulta un resumen razonable.
# ------------------------------------------------------------------------------

# %% Ejercicio 5 - Cinco generos mas frecuentes y porcentaje de explicitas

print("\n--- Ejercicio 5: generos frecuentes y canciones explicitas ---")

# Los generos compuestos se separan en generos individuales. La justificacion
# completa esta en el bloque de analisis al final del ejercicio.
generos = df["genre"].str.split(",").explode().str.strip()
generos = generos[generos != "set()"]

frecuencia_generos = generos.value_counts()
canciones_con_genero = generos.index.nunique()

top_5 = frecuencia_generos.head(5).to_frame("canciones")
top_5["% del total"] = (top_5["canciones"] / canciones_con_genero * 100).round(1)

print(f"Celdas con mas de un genero: {df['genre'].str.contains(',').sum()} de {len(df)}")
print(f"Canciones sin genero identificado: {(df['genre'] == 'set()').sum()}")
print(f"Generos individuales distintos: {frecuencia_generos.size}")

print("\nTop 5 generos mas frecuentes:")
print(top_5)

print(f"\nCanciones explicitas: {df['explicit'].sum()} de {len(df)} "
      f"({df['explicit'].mean() * 100:.1f} %)")

# ------------------------------------------------------------------------------
# ANALISIS - EJERCICIO 5: generos frecuentes y criterio con los compuestos
#
# Los cinco generos mas frecuentes son pop (1633 canciones, 82.6 %), hip hop
# (778, 39.3 %), R&B (452, 22.9 %), Dance/Electronic (390, 19.7 %) y rock (234,
# 11.8 %). Las canciones explicitas son 551 de 2000, es decir el 27.6 %.
#
# CRITERIO ADOPTADO CON LOS GENEROS COMPUESTOS: se separo cada celda en generos
# individuales y se conto cada aparicion. El problema afecta a la mayoria del
# conjunto -1279 de las 2000 celdas contienen mas de un genero separado por
# comas- y la razon de separar es que el enunciado pide los generos mas
# frecuentes, no las combinaciones mas frecuentes. Contar la combinacion
# completa como categoria habria tratado "hip hop, pop" y "hip hop, pop, R&B"
# como categorias ajenas al pop, ocultando que el pop aparece en 1633 canciones,
# mas de ocho de cada diez. El costo de la decision, que conviene declarar, es
# que los porcentajes ya no suman 100 % y deben leerse por separado. Aparte, las
# 22 canciones cuyo genero es "set()" se excluyeron por tratarse de un dato
# faltante y no de un genero, por lo que los porcentajes se calculan sobre las
# 1978 canciones con genero identificado.
# ------------------------------------------------------------------------------


# %% ============================================================================
# PARTE 3 - VISUALIZACION DE DATOS
# ==============================================================================

print("\n" + "=" * 78)
print("  PARTE 3 - VISUALIZACION DE DATOS")
print("=" * 78)

# %% Ejercicio 6 - Histograma de tempo con linea vertical roja en la media

print("\n--- Ejercicio 6: histograma de tempo ---")

tempo_medio = df["tempo"].mean()

fig, ax = plt.subplots(figsize=(10, 6))

sns.histplot(data=df, x="tempo", bins=40, color="#4C72B0", edgecolor="white", ax=ax)

ax.axvline(tempo_medio, color="red", linestyle="--", linewidth=2,
           label=f"Media = {tempo_medio:.1f} BPM")

ax.set_title("Distribución del tempo en los éxitos globales (1998-2020)", fontsize=13)
ax.set_xlabel("Tempo (pulsos por minuto, BPM)")
ax.set_ylabel("Frecuencia (número de canciones)")
ax.legend()

fig.tight_layout()
plt.show()

print(f"Media del tempo: {tempo_medio:.2f} BPM")
print(f"Mediana del tempo: {df['tempo'].median():.2f} BPM")

# ------------------------------------------------------------------------------
# ANALISIS - EJERCICIO 6: rango de concentracion y modas del tempo
#
# El repertorio se concentra entre 90 y 140 BPM, franja que reune el 67.7 % de
# las canciones; el 50 % central es aun mas estrecho, entre 99 y 134 BPM. Fuera
# de esa banda la densidad cae rapidamente: por debajo de 75 BPM hay 33
# canciones y por encima de 180 BPM menos de 50, sobre un total de 2000.
#
# La distribucion NO es unimodal: aparecen dos concentraciones claras, una
# alrededor de 95-105 BPM y otra, la mas alta del histograma, alrededor de
# 125-130 BPM, separadas por un valle en torno a 105-115 BPM. Lo relevante es
# que la media (120.12) y la mediana (120.02) son casi identicas y aun asi no
# corresponden a ninguna de las dos modas: la linea roja cae en el espacio entre
# ambos grupos. Describir el repertorio como "canciones de unos 120 BPM" es
# estadisticamente correcto y musicalmente enganoso, porque oculta que conviven
# dos repertorios ritmicos distintos. La explicacion musical de esos dos picos
# es que corresponden a tradiciones de produccion diferentes: la moda baja es el
# pulso habitual del hip-hop, el R&B y la balada pop de tempo medio, mientras
# que la moda alta coincide con el tempo canonico de la musica de baile de raiz
# house y de la corriente EDM que dominó las listas en la segunda mitad del
# periodo, donde los 128 BPM funcionan como estandar de produccion.
# ------------------------------------------------------------------------------

# %% Ejercicio 7 - Boxplot de popularity segun explicit

print("\n--- Ejercicio 7: boxplot de popularidad segun contenido explicito ---")

n_grupo = df["explicit"].value_counts()

fig, ax = plt.subplots(figsize=(8, 6))

sns.boxplot(data=df, x="explicit", y="popularity", hue="explicit",
            palette="Set2", legend=False, ax=ax)

ax.set_title("Popularidad según contenido explícito", fontsize=13)
ax.set_xlabel("Contenido explícito")
ax.set_ylabel("Popularidad (índice 0-100)")
ax.set_xticks([0, 1])
ax.set_xticklabels([f"No explícita\n(n = {n_grupo[False]})",
                    f"Explícita\n(n = {n_grupo[True]})"])

fig.tight_layout()
plt.show()

resumen_7 = df.groupby("explicit")["popularity"].agg(
    n="count", mediana="median", media="mean", desv="std"
)
cuartiles = df.groupby("explicit")["popularity"].quantile([0.25, 0.75]).unstack()
resumen_7["Q1"] = cuartiles[0.25]
resumen_7["Q3"] = cuartiles[0.75]
resumen_7["RIC"] = resumen_7["Q3"] - resumen_7["Q1"]

print(resumen_7.round(2))

# ------------------------------------------------------------------------------
# ANALISIS - EJERCICIO 7: popularidad segun contenido explicito
#
# NO hay diferencia apreciable entre ambos grupos: las cajas se superponen casi
# por completo. Las medianas difieren en apenas dos puntos sobre una escala de 0
# a 100 -65 en las no explicitas frente a 67 en las explicitas- y la dispersion
# es practicamente identica: el rango intercuartilico es exactamente 17 en los
# dos grupos y las desviaciones estandar son 21.57 y 20.64. Los dos grupos no
# solo se centran en el mismo lugar, sino que varian igual. La lectura es
# negativa y no por ello pobre: el contenido explicito no separa a las canciones
# exitosas por su nivel de popularidad.
#
# Los grupos SI son de tamanos desiguales, 1449 canciones no explicitas frente a
# 551 explicitas. Con 551 observaciones la mediana del grupo menor sigue siendo
# estable, asi que la comparacion de medianas es valida; el riesgo esta en la
# lectura visual. El grupo no explicito APARENTA mayor dispersion porque muestra
# mas puntos atipicos por debajo, pero eso ocurre simplemente porque tiene 2.6
# veces mas canciones y, por tanto, mas oportunidades de contener valores
# extremos. Como el rango intercuartilico es identico, concluir que las
# canciones no explicitas son mas heterogeneas seria un error inducido por el
# tamano de la muestra. Por eso la comparacion debe apoyarse en los
# estadisticos de dispersion y no en la extension aparente de bigotes.
# ------------------------------------------------------------------------------


# %% ============================================================================
# PARTE 4 - ANALISIS BIVARIADO Y CORRELACION
# ==============================================================================

print("\n" + "=" * 78)
print("  PARTE 4 - ANALISIS BIVARIADO Y CORRELACION")
print("=" * 78)

# %% Ejercicio 8 - Matriz de correlacion de Pearson

print("\n--- Ejercicio 8: matriz de correlacion de Pearson ---")

atributos = ["danceability", "energy", "valence", "loudness"]

matriz_correlacion = df[atributos].corr(method="pearson")

print(matriz_correlacion.round(4))

# ------------------------------------------------------------------------------
# ANALISIS - EJERCICIO 8: lectura de la matriz
#
# De las seis relaciones posibles entre danceability, energy, valence y
# loudness, cinco son positivas y solo dos superan 0.4. La mas fuerte es
# energy-loudness con r = +0.651, seguida de danceability-valence con +0.403. En
# el extremo opuesto, danceability frente a energy (-0.104) y frente a loudness
# (-0.033) son relaciones practicamente nulas: que una cancion sea intensa o
# suene fuerte no dice casi nada sobre si es apta para bailar, un resultado
# contraintuitivo que conviene senalar.
# ------------------------------------------------------------------------------

# %% Ejercicio 9 - Mapa de calor con paleta divergente y valores anotados

print("\n--- Ejercicio 9: mapa de calor ---")

fig, ax = plt.subplots(figsize=(8, 6.5))

sns.heatmap(
    matriz_correlacion,
    annot=True,              # muestra los valores sobre las celdas
    fmt=".3f",
    cmap="coolwarm",         # paleta divergente
    vmin=-1,
    vmax=1,
    center=0,
    square=True,
    linewidths=0.5,
    cbar_kws={"label": "Coeficiente de correlación de Pearson"},
    ax=ax,
)

ax.set_title("Correlación entre atributos de audio", fontsize=13, pad=14)

fig.tight_layout()
plt.show()

# ------------------------------------------------------------------------------
# ANALISIS - EJERCICIO 9: lectura del mapa de calor
#
# La matriz se represento con una paleta divergente (coolwarm), la escala fijada
# entre -1 y 1 y centrada en 0, y los coeficientes anotados sobre cada celda.
# Fijar la escala no es un detalle estetico: garantiza que el blanco corresponda
# siempre a correlacion nula y que la intensidad del color sea comparable entre
# celdas. Si la escala se ajustara automaticamente al rango de los datos, una
# correlacion debil podria aparecer con el mismo color intenso que una fuerte y
# la lectura visual resultaria enganosa.
# ------------------------------------------------------------------------------

# %% Ejercicio 10 - Par mas correlacionado y diagrama de dispersion

print("\n--- Ejercicio 10: par con la correlacion mas fuerte ---")

# Se pasa la matriz a formato largo y se conserva un solo sentido de cada par
# (variable_1 < variable_2), lo que elimina la diagonal y las repeticiones.
pares = matriz_correlacion.stack().rename("r").reset_index()
pares.columns = ["variable_1", "variable_2", "r"]
pares = pares[pares["variable_1"] < pares["variable_2"]].copy()
pares["r_absoluto"] = pares["r"].abs()
pares = pares.sort_values("r_absoluto", ascending=False).reset_index(drop=True)

print(pares.round(4))

var_x = pares.loc[0, "variable_1"]
var_y = pares.loc[0, "variable_2"]
r_max = pares.loc[0, "r"]

print(f"\nPar mas fuerte: {var_x} - {var_y}  (r = {r_max:.4f})")
print(f"Coeficiente de determinacion r^2 = {r_max ** 2:.4f} "
      f"({r_max ** 2 * 100:.1f} % de varianza compartida)")

fig, ax = plt.subplots(figsize=(9, 6.5))

# alpha bajo y puntos pequenos para controlar el solapamiento de 2000 registros
sns.regplot(
    data=df,
    x=var_x,
    y=var_y,
    scatter_kws={"alpha": 0.25, "s": 14, "color": "#4C72B0"},
    line_kws={"color": "red", "linewidth": 2,
              "label": f"Recta de ajuste (r = {r_max:.3f})"},
    ax=ax,
)

ax.set_title("Relación entre energía y volumen promedio", fontsize=13)
ax.set_xlabel("Energía (índice 0-1)")
ax.set_ylabel("Volumen promedio (decibelios, dB)")
ax.legend()

fig.tight_layout()
plt.show()

# ------------------------------------------------------------------------------
# ANALISIS - EJERCICIO 10: relacion entre energy y loudness
#
# El par mas correlacionado en valor absoluto es energy-loudness, con r = +0.651
# y un coeficiente de determinacion r^2 = 0.424. La relacion es de DIRECCION
# POSITIVA -a mayor energia percibida, mayor volumen promedio, ya que loudness
# se mide en decibelios negativos y "mayor" significa mas cercano a cero- y de
# FUERZA moderada a fuerte, pero lejos de ser determinante: las dos variables
# comparten el 42.4 % de su variabilidad y el 57.6 % restante responde a
# factores que la relacion no captura. En terminos del fenomeno, las canciones
# mas energicas tienden a sonar considerablemente mas fuerte, con un margen de
# error amplio. En cuanto a la FORMA, la nube no presenta curvatura apreciable,
# pero si se estrecha en abanico: la desviacion estandar del volumen pasa de
# 3.52 dB en las canciones de baja energia a 1.31 dB en las de alta, de modo que
# la prediccion es mas confiable en un extremo que en el otro.
#
# Hay valores atipicos visibles en la esquina inferior izquierda -piezas
# acusticas como "I See Fire" de Ed Sheeran (-20.5 dB) o "Mad World" de Gary
# Jules (-17.2 dB)-, pero NO estan inflando el coeficiente: al excluir las
# canciones por debajo de -15 dB, r pasa de 0.651 a 0.641. Tampoco son errores
# de medicion, sino canciones legitimas que deben registrar bajo volumen y baja
# energia.
#
# ESTA CORRELACION NO PERMITE CONCLUIR CAUSALIDAD: que energia y volumen varien
# juntos no demuestra que subir el volumen vuelva mas energica una cancion, y
# ambas pueden responder a decisiones de produccion o convenciones de genero que
# este analisis no mide. Como el conjunto contiene unicamente exitos de listas,
# tampoco puede afirmarse nada sobre la musica que no alcanzo ese estatus.
# ------------------------------------------------------------------------------
