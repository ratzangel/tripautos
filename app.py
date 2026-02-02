import pandas as pd    
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('notebook/vehicles_us.csv') # leer los datos
st.header('Análisis de datos de anuncios de venta de coches usados en EE.UU.')

hist_button = st.button('Construir histograma') # crear un botón histograma
disp_button = st.button('Construir dispersión') # crear un botón dispersión

if disp_button: # al hacer clic en el botón
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="year", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)  # mostrar un gráfico Plotly interactivo

if hist_button: # al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer") # crear un histograma
    st.plotly_chart(fig, use_container_width=True)  # mostrar un gráfico Plotly interactivo