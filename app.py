import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px

# Título
st.title("Dashboard Interactivo - Titanic")

# Cargar dataset
df = sns.load_dataset('titanic')

# Sidebar para filtro
sexo = st.sidebar.selectbox("Selecciona el sexo:", df['sex'].dropna().unique())

# Filtrar datos
df_filtrado = df[df['sex'] == sexo]

# Gráfico de barras: supervivencia por clase
st.subheader("Supervivencia por Clase")
fig1 = px.histogram(
    df_filtrado, x='class', color='survived', barmode='group',
    labels={'survived':'Sobrevivió'}, color_discrete_map={0:'crimson',1:'mediumseagreen'}
)
st.plotly_chart(fig1)

# Histograma de edades
st.subheader("Distribución de Edades")
fig2 = px.histogram(df_filtrado, x='age', nbins=30, color_discrete_sequence=['steelblue'])
st.plotly_chart(fig2)

# Mostrar tabla con datos filtrados
st.subheader("Datos Filtrados (primeras 10 filas)")
st.dataframe(df_filtrado[['sex', 'age', 'class', 'survived']].head(10))
