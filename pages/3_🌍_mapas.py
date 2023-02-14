import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.graph_objects as go
import folium
from folium.plugins import MarkerCluster
from folium.plugins import MousePosition
from folium.features import DivIcon
from geopy.geocoders import Nominatim
import os
import streamlit.components.v1 as components



st.set_option('deprecation.showPyplotGlobalUse', False)


st.set_page_config(
    page_title="Reporte",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
    
)

df = pd.read_csv('data/ventas_updated.csv')
ventas = df
ventas = ventas.drop(axis=1, columns = "Unnamed: 0")
ventas['Fecha'] = pd.to_datetime(ventas['Fecha'])
ventasmes = ventas.groupby(ventas['Fecha'].dt.strftime('%m-%Y'))['Ventas'].sum()
ventasporano = ventas.groupby("Fecha").sum()
ventasporano.reset_index(inplace=True)
gananciasanuales = ventasporano.groupby(ventasporano["Fecha"].dt.year).sum()


#html mapita easy embed 
path_to_html = "html/mapa1.html" 
with open(path_to_html,'r') as f: 
    html_data = f.read()
components.html(html_data, height=400)
st.write('Texto para el mapa')

##Mapeando con plotly
import plotly.express as px
df_localidades = pd.read_csv('data/localidades.csv')
fig = px.scatter_mapbox( df_localidades, lat="latitude", lon="longitude",
                    hover_name="direccion",
                    zoom=10,
                    height=300)
fig.update_layout(mapbox_style="carto-positron",
                    margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig, use_container_width=True)