import streamlit as st, pandas as pd, os, pydeck as pdk
from translate import Translator
from functions import df_country_to_dict,df_to_sorted_dict,best_countries_by_variable,traducir_pal,traducir_lista,traducir_variable,graficar_histograma

def results(path, top, probs, user_input):
    
    # Carga los datos
    df = pd.read_csv(os.path.join(path, "csv", "BetterLife_clean.csv"))
    uni = pd.read_csv(os.path.join(path, "csv", "UniversityRanks_clean.csv"))
    coords_df = pd.read_csv(os.path.join(path, "csv", "CountryCoords.csv"))
    
    # Crea el diccionario con los países y sus universidades
    dicUni = {}
    for _, row in uni.iterrows():
        if row["Country"] in top and row["Country"] not in dicUni:
            dicUni[row["Country"]] = (row["Institution Name"],
            row["QS Overall Score"],
            row["2025 Rank"],
            os.path.join(path, "svg", f"{row['Location'].lower()}.svg"),
            df[df["Country"] == row["Country"]]["Life satisfaction"].values)

    # UI top 3
    for i in range(3):
        country = top[i]
        university, score, rank, flag_path, life_satisfaction = dicUni[country]
        translator = Translator(from_lang="autodetect",to_lang="es")
        try:
            pais = translator.translate(str(country))
            universidad = translator.translate(str(university))
            if pais == "PLEASE SELECT TWO DISTINCT LANGUAGES":
                pais = str(country)
            if universidad == "PLEASE SELECT TWO DISTINCT LANGUAGES":
                universidad = str(university)
        except:
            pais = country
            universidad = university
        try: 
            with st.container():
                card = st.columns([2, 4, 8],vertical_alignment="center",gap="medium")
                
                with card[0]:
                    st.image(flag_path, width=200)

                with card[1]:
                    st.markdown(f"""
                        <div style='padding: 00px 0px; font-size: 1.1rem; margin-bottom:15px'>
                        <h4 style='margin-bottom: -8px;'>{i+1}. {pais}:</h4>
                        <p style='margin: 0px;'>
                        🏫 <b>{universidad}</b><br>
                        ⭐ Puntuación: <b>{score}</b><br>
                        📊 Ranking Mundial: <b>{rank}</b></p></div>""", unsafe_allow_html=True)
                
                with card[2]:
                    satisfaction_percent = float(life_satisfaction)
                    stroke_width = 3
                    radius = 15.9155
                    circumference = 2 * 3.1416 * radius
                    offset = circumference * (1 - satisfaction_percent / 10)

                    st.markdown(f"""<div style="display: flex; flex-direction: column; align-items: left;">
                            <div style="position: relative; width: 80px; height: 80px;margin-left:10px">
                            <svg width="80" height="80" viewBox="0 0 36 36">
                            <circle cx="18" cy="18" r="{radius}" 
                            fill="none" stroke="#444" stroke-width="{stroke_width}" />
                            <circle cx="18" cy="18" r="{radius}"
                            fill="none" stroke="#FFD700" stroke-width="{stroke_width}"
                            stroke-dasharray="{circumference:.2f}"
                            stroke-dashoffset="{offset:.2f}"
                            stroke-linecap="round"
                            transform="rotate(-90 18 18)" /></svg>
                            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
                            font-size: 1em; color: white;">
                            {satisfaction_percent:.1f}/10</div></div>
                            <div style="margin-top: 5px; color: white;"><b>Calidad de Vida</b></div></div>""", unsafe_allow_html=True)

                st.markdown("<hr style='margin-top: 10px; margin-bottom: 30px;'>", unsafe_allow_html=True)
        except:
            st.write("Ha habido un error en el sistema.")

    # Compara 
    best = best_countries_by_variable(df) # diccionario del tipo {variable: [pais1, pais2, pais3]}
    dic_top_en_best = dict()
    for variable, valor in best.items():
        for country in top:
            if country in valor:
                if country not in dic_top_en_best:
                    dic_top_en_best[traducir_pal(country)] = [traducir_variable(variable)]
                else:
                    dic_top_en_best[traducir_pal(country)].append(traducir_variable(variable))
    
    if dic_top_en_best != {}:
        st.markdown(f"### 🏆 Comparación de las recomendaciones respecto a los mejores países en cada variable:")
        for pais, l_variables in dic_top_en_best.items():
            if len(l_variables) == 1:
                st.markdown(f"**{pais}** está entre los mejores países en {l_variables[0]}.")
            elif len(l_variables) == 2:
                st.markdown(f"**{pais}** está entre los mejores países en {l_variables[0]} y {l_variables[1]}.")
            elif len(l_variables) == 3:
                st.markdown(f"**{pais}** está entre los mejores países en {l_variables[0]}, {l_variables[1]} y {l_variables[2]}.")
            elif len(l_variables) > 3:
                st.markdown(f"**{pais}** está entre los mejores países en {l_variables[0]}, {l_variables[1]} y {len(l_variables)-2} variables más.")

    # Gráfico de puntos donde aparezca el input del usuario, y uno de los países recomendados
    input = df_to_sorted_dict(user_input) # diccionario del tipo {variable: valor}
    st.markdown("### 📊 Comparación de variables entre el input del usuario y los países recomendados:")
    with st.container():
        col1, col2, col3 = st.columns([3, 3, 3], gap = 'medium')
        dic_top1 = df_country_to_dict(df, top[0])
        dic_top2 = df_country_to_dict(df, top[1])
        dic_top3 = df_country_to_dict(df, top[2])
        with col1:
            graficar_histograma(input, dic_top1, top[0])
        with col2:
            graficar_histograma(input, dic_top2, top[1])
        with col3:
            graficar_histograma(input, dic_top3, top[2])

    # Mapa
    try:
        map_data = []
        for country in top:
            coord_row = coords_df[coords_df["Country"] == country]
            if not coord_row.empty:
                map_data.append({"Country": country,
                                "lat": coord_row.iloc[0]["lat"],
                                "lon": coord_row.iloc[0]["lon"],
                                "University": dicUni[country][0],
                                "Satisfaction": float(dicUni[country][4])})
                        
        top_coords_df = pd.DataFrame(map_data)
        st.markdown("### 🗺️ Ubicación de Países Recomendados:")
        st.pydeck_chart(pdk.Deck(map_style="mapbox://styles/mapbox/dark-v10",
                                initial_view_state=pdk.ViewState(latitude=top_coords_df["lat"].mean(),
                                                                longitude=top_coords_df["lon"].mean(),
                                                                zoom=1, pitch=30),
                                layers=[pdk.Layer("ScatterplotLayer",
                                        data=top_coords_df,
                                        get_position='[lon, lat]',
                                        get_color='[255, 140, 0, 160]',
                                        get_radius=500000,
                                        pickable=True)],
                                tooltip={"html": "<b>{Country}</b><br/>🏫 {University}<br/>😊 Calidad de Vida: {Satisfaction}<br/>", "style": {"color": "white"}}))
    except:
        st.write("Ha habido un error con la generación del mapa.")
    