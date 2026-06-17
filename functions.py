""" 
Libreria de todas las funciones utilizadas para facilidad de
lectura y quitar clutter del código principal.
"""

import matplotlib.pyplot as plt
from translate import Translator
import streamlit as st
import numpy as np

def worst_best_country(df):
        dic = {"": ["Mejor","Peor"]}
        for column in df.columns:
            sort = df.sort_values(column, ascending=False)
            best = sort.head(1)
            worst = sort.tail(1)
            dic[column] = [best["Country"].values, worst["Country"].values]
        return dic

def df_to_sorted_dict(df):
    d = dict()
    for i, row in df.iterrows():
        for variable, valor in row.items():
            d[variable] = valor
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

def best_countries_by_variable(df):
    # Esta función debe recibir un dataframe y una lista con los países recomendados,
    # y devolver un diccionario del tipo {variable: [pais1, pais2, pais3]}
    d = dict()
    for column in df.columns[1:]:
        df.sort_values(column, ascending = False, inplace = True)
        # Añade los tres primeros países a la lista
        d[column] = df.head(3)['Country'].tolist()
    return d

def df_country_to_dict(df, pais):
	# Esta función recibe un df con todos los países y sus valores, y devuelve un diccionario del tipo {variable: valor} para el país buscado como parámetro
	d = dict()
	for i, row in df.iterrows():
		if row['Country'] == pais:
			for variable, valor in row.items():
				if variable != 'Country':
					d[variable] = float(valor)
			break
		else:
			continue

	return d

def traducir_pal(str, entrada = 'autodetect', salida = 'es'):
    # Esta función recibe un string y un diccionario de entrada y otro de salida, y traduce el string de entrada al de salida
    translator = Translator(from_lang = entrada, to_lang = salida)
    try:
        traduccion = translator.translate(str)
        if traduccion == "PLEASE SELECT TWO DISTINCT LANGUAGES":
            # Si la traducción no se ha podido realizar, se devuelve el string original
            return str
        return translator.translate(str)
    except:
        return str

def traducir_lista(lista, entrada = 'autodetect', salida = 'es'):
    # Esta función recibe una lista de strings y un diccionario de entrada y otro de salida, y traduce la lista de entrada al de salida
    try:
        return [traducir_pal(i, entrada, salida) for i in lista]
    except:
        return lista

def traducir_variable(variable):
    d = {'Education': 'Educación', 'Jobs': 'Trabajo', 'Income': 'Finanzas', 'Housing': 'Alojamiento', 'Safety': 'Seguridad', 'Health': 'Salud','Environment': 'Medio Ambiente',
        'Civic Engagement': 'Compromiso Civil', 'Access to Services': 'Acceso a Servicios', 'Community': 'Comunidad', 'Life satisfaction': 'Satisfacción con la vida'}
    try:
        return d[variable]
    except:
        return traducir_pal(variable)

def graficar_histograma(input, dic_pais, pais):
    del dic_pais['Life satisfaction']
    claves = input.keys()
    valores_usuario = np.array([k for k in input.values()])
    valores_pais = np.array([k for k in dic_pais.values()])
    plt.figure()
    plt.bar(claves, valores_usuario / 2, label='Usuario')
    plt.bar(claves, abs(valores_pais - valores_usuario) / 2, label=pais, bottom=valores_usuario / 2)
    plt.xticks([])
    plt.yticks([])
    plt.ylim(0, 10)
    plt.xlabel('Variables')
    plt.ylabel('Valores')
    plt.title(f'Comparación de valores entre {traducir_pal(pais)} y el input del usuario.')
    plt.legend()
    # Mostrar
    st.pyplot(plt)