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
c1, c2 = st.columns([4,6])

with c1:
    c1 = ventasmes.sort_values(ascending=False)
    c1b=px.line(ventasmes, x=ventasmes.index,y="Ventas") 
    st.plotly_chart(c1b,use_container_width=False)
    st.write("Explicación de la gráfica")

with c2:
    c2a = px.bar(ventasmes, x=ventasmes.index, y="Ventas", template='presentation')
    st.plotly_chart(c2a)
    st.write("Explicación de la gráfica")


i1, i2 = st.columns([4,6])

with i1:
    st.write("")
    st.write("PODEMOS EMPEZAR A VER COMO EL VÍRUS PARÓ EL CRECIMIENTO DEL NEGOCIO, SE DEBERÍA CONTRASTAR SI ESTA FUE LA CAUSA")
    st.write("")

    sumaventas=[0.0]
    def suma(ventas):
        sumaventas.append(sumaventas[-1] + ventas)
    ventasporano.apply(lambda x: suma(x["Ventas"]), axis=1)
    sumaventas.remove(0.0)
    ventasporano['Suma'] = pd.Series(sumaventas)
    plt.figure(figsize=(20,8))
    sns.lineplot(x=ventasporano["Fecha"], y=ventasporano['Suma'], data=ventasporano)
    plt.xticks(rotation=45)
    plt.grid()
    plt.title("Evolución temporal acumulativa para ver el efecto del virus en el volumen")
    plt.xlabel('Tiempo')
    plt.ylabel('Ventas acumuladas')
    st.pyplot()

with i2:
    fig=px.bar(gananciasanuales, x=list(gananciasanuales.index), y="Ventas",
    labels={'x':"Año", 'Suma': "Dólares", "year":"Año"})
    st.plotly_chart(fig)



