# %% Taller 07 - Estadistica descriptiva y EDA
# Curso: Estadistica III - Ingenieria de Sistemas, UCO

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

RUTA_DATOS = Path(__file__).resolve().parent / "data" / "07 - canciones.csv"

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", None)

sns.set_theme(style="whitegrid")


# %% ========================= PARTE 1 - INGESTA Y LIMPIEZA =========================

print("\n" + "=" * 78)
print("  PARTE 1 - INGESTA Y LIMPIEZA INICIAL")
print("=" * 78)

# %% Ejercicio 1 - Carga del conjunto de datos

print("\n--- Ejercicio 1: primeras 5 filas ---")

df = pd.read_csv(RUTA_DATOS)

print(df.head())

# %% Ejercicio 2 - Estructura, tipos de datos y valores nulos

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

# ANALISIS EJERCICIO 2: ver `analisis-parte-1.md`
# Resumen: isna() no reporta nulos, pero el conjunto SI requiere limpieza.
# Hay 59 duplicados exactos, 126 ceros en popularity y 22 "set()" en genre
# que son datos faltantes disfrazados de valores validos, ademas de key y
# mode tipadas como enteros siendo categoricas.


# %% ==================== PARTE 2 - ESTADISTICA DESCRIPTIVA ====================

print("\n" + "=" * 78)
print("  PARTE 2 - ESTADISTICA DESCRIPTIVA UNIVARIADA")
print("=" * 78)

# %% Ejercicio 3 - Duracion en minutos

print("\n--- Ejercicio 3: duracion en minutos ---")

df["duration_min"] = df["duration_ms"] / 60000

print(df[["song", "duration_ms", "duration_min"]].head())

# %% Ejercicio 4 - Medidas de tendencia central y dispersion

print("\n--- Ejercicio 4: medidas de tendencia central y dispersion ---")

variables = ["duration_min", "popularity", "danceability"]

resumen_4 = df[variables].agg(["mean", "median", "std", "min", "max"]).T
resumen_4.columns = ["media", "mediana", "desv_est", "minimo", "maximo"]

print(resumen_4.round(3))

print(f"\npopularity -> media {df['popularity'].mean():.2f} | "
      f"mediana {df['popularity'].median():.1f} | "
      f"diferencia {df['popularity'].mean() - df['popularity'].median():.2f}")
print(f"popularity -> coeficiente de asimetria: {df['popularity'].skew():.3f}")

# ANALISIS EJERCICIO 4: ver `analisis-parte-2.md`

# %% Ejercicio 5 - Generos mas frecuentes y porcentaje de explicitas

print("\n--- Ejercicio 5: generos frecuentes y canciones explicitas ---")

# CRITERIO PARA LOS GENEROS COMPUESTOS:
# El 64 % de las celdas (1279 de 2000) contiene varios generos separados por
# coma. Se separan en generos individuales, porque el enunciado pide los
# generos mas frecuentes y no las combinaciones mas frecuentes. El valor
# "set()" (22 canciones) se descarta: no es un genero sino un conjunto vacio,
# es decir, un dato faltante. Justificacion completa en `analisis-parte-2.md`.

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
print("Nota: los porcentajes suman mas de 100 % porque una cancion puede "
      "pertenecer a varios generos.")

print(f"\nCanciones explicitas: {df['explicit'].sum()} de {len(df)} "
      f"({df['explicit'].mean() * 100:.1f} %)")

# ANALISIS EJERCICIO 5: ver `analisis-parte-2.md`


# %% ====================== PARTE 3 - VISUALIZACION ======================

print("\n" + "=" * 78)
print("  PARTE 3 - VISUALIZACION DE DATOS")
print("=" * 78)

# %% Ejercicio 6 - Histograma de tempo con la media marcada

print("\n--- Ejercicio 6: histograma de tempo ---")

tempo_medio = df["tempo"].mean()

fig, ax = plt.subplots(figsize=(10, 6))

sns.histplot(data=df, x="tempo", bins=40, color="#4C72B0", edgecolor="white", ax=ax)

ax.axvline(tempo_medio, color="red", linestyle="--", linewidth=2,
           label=f"Media = {tempo_medio:.1f} BPM")

ax.set_title("Distribucion del tempo en los exitos globales (1998-2020)", fontsize=13)
ax.set_xlabel("Tempo (BPM)")
ax.set_ylabel("Frecuencia (numero de canciones)")
ax.legend()

fig.tight_layout()
plt.show()

print(f"Media del tempo: {tempo_medio:.2f} BPM")
print(f"Mediana del tempo: {df['tempo'].median():.2f} BPM")

# ANALISIS EJERCICIO 6: ver `analisis-parte-3.md`

# %% Ejercicio 7 - Boxplot de popularity segun explicit

print("\n--- Ejercicio 7: boxplot de popularidad segun contenido explicito ---")

n_grupo = df["explicit"].value_counts()

fig, ax = plt.subplots(figsize=(8, 6))

sns.boxplot(data=df, x="explicit", y="popularity", hue="explicit",
            palette="Set2", legend=False, ax=ax)

ax.set_title("Popularidad segun contenido explicito", fontsize=13)
ax.set_xlabel("Contenido explicito")
ax.set_ylabel("Popularidad (indice 0-100)")
ax.set_xticks([0, 1])
ax.set_xticklabels([f"No explicita\n(n = {n_grupo[False]})",
                    f"Explicita\n(n = {n_grupo[True]})"])

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

# ANALISIS EJERCICIO 7: ver `analisis-parte-3.md`


# %% ================= PARTE 4 - ANALISIS BIVARIADO Y CORRELACION =================

print("\n" + "=" * 78)
print("  PARTE 4 - ANALISIS BIVARIADO Y CORRELACION")
print("=" * 78)

# %% Ejercicio 8 - Matriz de correlacion de Pearson

print("\n--- Ejercicio 8: matriz de correlacion de Pearson ---")

atributos = ["danceability", "energy", "valence", "loudness"]

matriz_correlacion = df[atributos].corr(method="pearson")

print(matriz_correlacion.round(4))

# %% Ejercicio 9 - Mapa de calor de la matriz de correlacion

print("\n--- Ejercicio 9: mapa de calor ---")

fig, ax = plt.subplots(figsize=(8, 6.5))

sns.heatmap(
    matriz_correlacion,
    annot=True,
    fmt=".3f",
    cmap="coolwarm",     # paleta divergente
    vmin=-1,
    vmax=1,
    center=0,
    square=True,
    linewidths=0.5,
    cbar_kws={"label": "Coeficiente de correlacion de Pearson"},
    ax=ax,
)

ax.set_title("Correlacion entre atributos de audio", fontsize=13, pad=14)

fig.tight_layout()
plt.show()

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
    line_kws={"color": "red", "linewidth": 2, "label": f"Recta de ajuste (r = {r_max:.3f})"},
    ax=ax,
)

ax.set_title(f"Relacion entre {var_x} y {var_y}", fontsize=13)
ax.set_xlabel("Energia (indice 0-1)")
ax.set_ylabel("Volumen promedio (dB)")
ax.legend()

fig.tight_layout()
plt.show()

# ANALISIS EJERCICIO 10: ver `analisis-parte-4.md`
