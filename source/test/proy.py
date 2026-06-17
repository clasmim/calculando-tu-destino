import pandas as pd
import matplotlib.pyplot as plt

'''
Un simple programa que ligeramente limpia, filtra y recopila los datos de un archivo
.csv para crear un gráfico con las variables de los países de la EU y su índice de calidad
de vida basado en diferentes parámetros y categorías.
'''

import libProy as lib       # Importamos la libreria del proyecto.
year = lib.eleccionAnyo()   # Invocando funciones de la libreria para 
age = lib.rangoEdad()       # elegir el filtro de búsqueda.

dataset = pd.read_csv("DatosQoL.csv")
# Leemos la base de datos.

dataset.drop("CONF_STATUS",inplace=True,axis="columns")
dataset.drop("OBS_FLAG",inplace=True,axis="columns")
# Eliminamos dos columnas que solo tienen valores NaN.

dataset["OBS_VALUE"].dropna(axis='rows', how='any',inplace=True)
# Eliminamos las filas que tienen valores NaN en la columna con el índice de calidad de vida.

filter = dataset.loc[(dataset["age"]==age) & (dataset["TIME_PERIOD"]==year)]
# Creamos el filtro con la función loc con las elecciones del usuario.

group = filter.groupby("geo")["OBS_VALUE"].mean().sort_values()
print(group.index, group.values)

set = filter.sort_values(by="OBS_VALUE",ascending=True)
# Ordenamos los valores a partir de los valores de calidad de vida.

fig,ax=plt.subplots(figsize=(10,10))
ax.barh(group.index,group.values)
ax.grid("x")
ax.set_title(f"Calidad de vida basado para edad {age} durante el año {year}.")
# Creamos un gráfico de barras horizontales, lo cuadriculamos y le damos un titulo.