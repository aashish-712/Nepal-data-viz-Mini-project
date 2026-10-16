import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

final_df = pd.read_csv("Nepal_df.csv")
list_of_states = list(final_df["State"].unique())
list_of_states.insert(0, "Overal Nepal")


st.sidebar.title("Nepal Data Visualization")
selected_state = st.sidebar.selectbox("Select Province", list_of_states)
primary = st.sidebar.selectbox("Select Primary Parameter", sorted(final_df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(final_df.columns[5:]))

plot = st.sidebar.button("Plot Graph")

if plot:
    st.text("Size Represent Primary Parameter")
    st.text('Color Represents Secondary Parameter')
    if selected_state == "Overal Nepal" :
        #plot for Nepal
        fig = px.scatter_map(final_df, lat='Latitude', lon='Longitude',center={"lat": 28.4, "lon": 84.1}, zoom = 5.5, size= primary,
                             color= secondary,color_continuous_scale="Turbo", size_max= 35, map_style= "carto-positron", width= 1000,
                              hover_name= "District", height= 500)
        st.plotly_chart(fig, use_container_width= True)
    else :
        #plot for state
        state_df = final_df[final_df['State'] == selected_state ]
        fig = px.scatter_map(state_df, lat='Latitude', lon='Longitude',center={"lat": 28.4, "lon": 84.1}, zoom = 5.5, size= primary,
                             color= secondary,color_continuous_scale="Turbo", size_max= 35, map_style= "carto-positron", width= 1000,
                              hover_name="District", height= 500)
        st.plotly_chart(fig, use_container_width= True)                      