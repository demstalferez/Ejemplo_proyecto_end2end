import streamlit as st
import pandas as pd



if "shared" not in st.session_state:
   st.session_state["shared"] = True



st.set_page_config(
    page_title="Inicio",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
    
)


col1, col2, col3 = st.columns([4,6,1])
with col1:
    st.write("")
with col2:
    st.image('img/logo.png' ,width=300 )
    st.title('EJEMPLO APP')
with col3:
    st.write("")
    

st.write("Conjunto de datos de nuestro panel de control, lo ideal es que esto lo puedan actualizar en tiempo real, no con documentos, siempre se debe apuntar a la automatización.")

#reading and show the csv
df = pd.read_csv('data/ventas_updated.csv')
st.write(df)
