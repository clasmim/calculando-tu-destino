import streamlit as st

def aboutus():
    st.title("ℹ️ Acerca de esta App")

    st.markdown("""
        Bienvenido a **Optimizando tu destino: Análisis de tu lugar ideal** 🌍

        Esta aplicación utiliza tus preferencias personales en áreas como educación, seguridad, salud y más,
        para recomendarte los mejores países donde podrías considerar estudiar.

        Todo está basado en un estudio de los índices de Calidad de Vida de varias fuentes: **OECD**, **Eurostat** e **INE**.

        ---

        ### ¿Qué hace esta aplicación?
        - Predice los mejores países según tus prioridades.
        - Muestra universidades destacadas y sus rankings.
        - Visualiza los resultados en un mapa interactivo.

        ---

        ### Tecnologías utilizadas:
        - **Streamlit** para la interfaz.
        - **scikit-learn** para predicción con modelo Random Forest.
        - **Pydeck** para mapas.
        - **Pandas** y **NumPy** para manejo de datos.
        - **Joblib** para la optimización del código.

        ---

        Desarrollado por Chafik Laslouni, Juanjo Fernández, Juan López, Alejandro Ruiz y Álvaro Santafé, estudiantes de la Universidad Politécnica de Valencia.

        """)