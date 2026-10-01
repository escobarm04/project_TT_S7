import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# 1. Leer los datos del archivo CSV
car_data = pd.read_csv('~/Documents/project_TT_S7/vehicles_us.csv')
columnas = car_data.columns.tolist() # Extraemos los nombres de las variables

# Encabezado principal
st.header('¡Hola terrícolas! Bienvenidos a la aplicación de visualización de datos de anuncios de venta de coches.')

# 2. Mostrar un vistazo de la base de datos
st.subheader('Vista previa de las variables')
st.dataframe(car_data.head()) # Muestra las primeras 5 filas interactiva

st.divider() # Línea divisoria para limpiar el diseño

# 3. Histograma Dinámico
st.subheader('Análisis de Distribución')
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    # Menú desplegable para elegir la variable (por defecto muestra 'odometer')
    var_hist = st.selectbox(
        'Selecciona la variable a distribuir:', 
        columnas, 
        index=columnas.index('odometer') if 'odometer' in columnas else 0
    )
    
    st.write(f'Creación de un histograma para la variable: **{var_hist}**')

    # Se inyecta la variable elegida al gráfico
    fig = go.Figure(data=[go.Histogram(x=car_data[var_hist])])
    fig.update_layout(title_text=f'Distribución de {var_hist.capitalize()}')
    
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# 4. Scatter Plot Dinámico
st.subheader('Análisis de Relación')
build_scatter_plot = st.checkbox('Construir scatter plot')

if build_scatter_plot:
    # Usamos columnas de Streamlit para poner los selectores lado a lado
    col1, col2 = st.columns(2)
    
    with col1:
        var_x = st.selectbox(
            'Variable para el eje X:', 
            columnas, 
            index=columnas.index('odometer') if 'odometer' in columnas else 0
        )
    with col2:
        var_y = st.selectbox(
            'Variable para el eje Y:', 
            columnas, 
            index=columnas.index('price') if 'price' in columnas else 0
        )

    st.write(f'Creación de un scatter plot relacionando **{var_x}** vs **{var_y}**')

    # Se inyectan ambas variables al gráfico
    fig = go.Figure(data=[go.Scatter(x=car_data[var_x], y=car_data[var_y], mode='markers')])
    fig.update_layout(title_text=f'Relación: {var_x.capitalize()} vs {var_y.capitalize()}')
    
    st.plotly_chart(fig, use_container_width=True)