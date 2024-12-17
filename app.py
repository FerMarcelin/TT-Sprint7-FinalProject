import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('TT - Proyecto S7 - Car Data')

hist_button = st.button('Construir histograma')
disp_button = st.button('Contruir un gráfico de dispersión')

if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

if disp_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un grafico de dispersión a para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.scatter(car_data, x="odometer", y="price")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)
