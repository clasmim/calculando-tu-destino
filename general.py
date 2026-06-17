import streamlit as st
import pandas as pd
import os
from functions import worst_best_country

def general(path):
    df = pd.read_csv(os.path.join(path, "csv", "BetterLifeResumen.csv"))

    st.title("📖 Estudio general de la Calidad de Vida en Europa.")

    st.markdown("### Análisis descriptivo de los parámetros generales de cada país:")

    df_na = df.dropna(how="any",axis="rows")
    st.dataframe(df_na.describe())

    st.markdown("### Los mejores 3 países según la variable:")

    best = pd.DataFrame(worst_best_country(df_na))
    best = best.set_index([""])
    del best["Country"]
    st.dataframe(best)
    
    st.markdown("### Diferentes gráficos extraídos a partir del estudio de los datos:")
    col1, col2 = st.columns(2)
    with col1:
        graf1 = os.path.join(path, "graphs", "corr.png")
        st.image(graf1)
    with col2:
        graf2 = os.path.join(path, "graphs", "mapa.png")
        st.image(graf2)