import streamlit as st
import os
from about import aboutus
from main import main
from results import results
from prediction import prediction
from general import general
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide", page_title="Optimizando tu destino: Análisis de tu lugar ideal", page_icon="🌍")

# Inicializa las variables de sesión
if "page" not in st.session_state:
    st.session_state.page = "Inicio"
if "done" not in st.session_state:
    st.session_state.done = False
if "path" not in st.session_state:
    st.session_state.path = None
if "top" not in st.session_state:
    st.session_state.top = None
if "probs" not in st.session_state:
    st.session_state.probs = None
if "user_input" not in st.session_state:
    st.session_state.user_input = None

path = str(os.path.dirname(os.path.abspath(__file__)))

with st.sidebar:
    selected = option_menu(
        menu_title = "Menú",
        options = ["Inicio", "Resultados", "Estudio General", "Acerca De"],
        icons = ["house", "bar-chart-line", "book", "info-circle"],
        menu_icon = "cast",
        default_index = 0)
    
    if selected == "Inicio":
        st.session_state.page = "Inicio"
    elif selected == "Resultados":
        st.session_state.page = "Resultados"
    elif selected == "Estudio General":
        st.session_state.page = "Estudio general"
    elif selected == "Acerca De":
        st.session_state.page = "Acerca de"

education=jobs=income=housing=safety=health=environment=civic=access=community= 5.0
if st.session_state.page == "Inicio":
    education, jobs, income, safety, health, environment, civic, access, housing, community = main(education,jobs,income,housing,safety,health,environment,civic,access,community)
    
    if st.button("🌐 Recomienda País"):
        with st.spinner("🧠 Calculando recomendaciones..."):
            
            # Realiza la predicción
            input = (education, jobs, income, safety, health, environment, civic, access, housing, community)
            st.session_state.top, st.session_state.probs, st.session_state.user_input = prediction(input, path)
            
            # Muestra un mensaje de éxito
            st.session_state.done = True
            st.markdown('¡Predicción realizada con éxito! Puede ver la explicación de los resultados en la pestaña "Resultados".')
            
            # Si el usuario hace clic en "Ver Resultados", cambia a la pestaña de resultados
            # results_button = st.button("Ver Resultados") 
            # if results_button:
            #    selected = "Resultados"
            #    st.session_state.page = "Resultados"

if st.session_state.page == "Resultados":
    st.title("📊 Resultados")
    if st.session_state.done:
        results(path, st.session_state.top, st.session_state.probs, st.session_state.user_input)
    else:
        st.markdown("Aquí podrás ver los resultados de tu predicción.")

if st.session_state.page == "Estudio general":
    general(path)

if st.session_state.page == "Acerca de":
    aboutus()

# La página y sus resultados están limitados a los países de la OECD.