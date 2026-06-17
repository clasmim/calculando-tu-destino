import streamlit as st

def main(education,jobs,income,housing,safety,health,environment,civic,access,community):
    
    st.markdown("# 🌍 Optimizando tu destino: Análisis de tu lugar ideal")
    st.markdown("##### Ajusta las barras según tus preferencias:")

    col1, col2, col3 = st.columns([2,2,4],gap="large")

    with col1:
        education = st.slider("🎓 Educación", 0.0, 10.0, education, 0.1)
        jobs = st.slider("💼 Trabajo", 0.0, 10.0, jobs, 0.1)
        income = st.slider("💰 Finanzas", 0.0, 10.0, income, 0.1)
        housing = st.slider("🏠 Alojamiento", 0.0, 10.0, housing, 0.1)
        safety = st.slider("🛡️ Seguridad", 0.0, 10.0, safety, 0.1)

    with col2:
        health = st.slider("❤️ Salud", 0.0, 10.0, health, 0.1)
        environment = st.slider("🌿 Medio Ambiente", 0.0, 10.0, environment, 0.1)
        civic = st.slider("🗳️ Compromiso Civil", 0.0, 10.0, civic, 0.1)
        access = st.slider("🚌 Acceso a Servicios", 0.0, 10.0, access, 0.1)
        community = st.slider("🤝 Comunidad", 0.0, 10.0, community, 0.1)

    with col3:
        st.markdown("### 🧭 Leyenda de Variables:")
        st.markdown("""<div style='line-height: 2.5; font-size: 1.1rem;'>
            <b>🎓 Educación:</b> Calidad del sistema educativo y nivel de instrucción.<br>
            <b>💼 Trabajo:</b> Oportunidades laborales, estabilidad y satisfacción.<br>
            <b>💰 Finanzas:</b> Nivel de ingresos y capacidad adquisitiva promedio.<br>
            <b>🏠 Alojamiento:</b> Calidad, asequibilidad y disponibilidad de vivienda.<br>
            <b>🛡️ Seguridad:</b> Niveles de criminalidad y percepción de seguridad.<br>
            <b>❤️ Salud:</b> Acceso a servicios de salud y bienestar general.<br>
            <b>🌿 Medio Ambiente:</b> Calidad del aire, agua y políticas ecológicas.<br>
            <b>🗳️ Compromiso Civil:</b> Participación ciudadana y confianza en instituciones.<br>
            <b>🚌 Acceso a Servicios:</b> Disponibilidad de transporte, tecnología y servicios públicos.<br>
            <b>🤝 Comunidad:</b> Conexión social, apoyo entre vecinos y cohesión comunitaria. </div>""", unsafe_allow_html=True)

    return education, jobs, income, safety, health, environment, civic, access, housing, community