import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

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


#columns
c1, c2 = st.columns([5,5])

with c1:
    top_vendedores = ventas['Empleado'].value_counts().index[:10].tolist()
    top_vendedores = ventas.groupby("Empleado").sum().loc[top_vendedores]
    top_vendedores.reset_index(inplace=True)
    top_vendedores.sort_values('Ventas',ascending=False,inplace=True)
    fig = px.bar(top_vendedores, x=top_vendedores["Empleado"], y="Ventas", color=top_vendedores["Empleado"], title="TOP10 Vendedores")
    st.plotly_chart(fig,use_container_width=False)

with c2:
    menos_vendedores = ventas['Empleado'].value_counts().index[-10:].tolist()
    menos_vendedores = ventas.groupby("Empleado").sum().loc[menos_vendedores]
    menos_vendedores.reset_index(inplace=True)
    menos_vendedores.sort_values('Ventas',ascending=True,inplace=True)
    fig2=px.bar(menos_vendedores.head(10), x=menos_vendedores.head(10)["Empleado"], y="Ventas", color=menos_vendedores.head(10)["Empleado"], title="Vendedores no efectivos")
    st.plotly_chart(fig2,use_container_width=False)

areasg=px.scatter(ventas, x="Ventas", y="Area", title="Relación entre ventas y area", color="Ventas")
st.plotly_chart(areasg,use_container_width=False)