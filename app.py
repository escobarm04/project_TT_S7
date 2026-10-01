import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# 1. Leer los datos del archivo CSV
car_data = pd.read_csv('~/Documents/project_TT_S7/vehicles_us.csv')
columnas = car_data.columns.tolist()

# Encabezado principal
st.header('🚗 ¡Hola terrícolas! Bienvenidos a la aplicación de visualización de datos de anuncios de venta de coches.')

# 2. Mostrar un vistazo de la base de datos
st.subheader('🔍 Vista previa de las variables')
st.dataframe(car_data.head())

st.divider()

# 3. Histograma Dinámico
st.subheader('📊 Análisis de Distribución')
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    var_hist = st.selectbox(
        'Selecciona la variable a distribuir:', 
        columnas, 
        index=columnas.index('odometer') if 'odometer' in columnas else 0
    )
    
    st.write(f'Creación de un histograma para la variable: **{var_hist}**')

    fig = go.Figure(data=[go.Histogram(x=car_data[var_hist])])
    fig.update_layout(title_text=f'Distribución de {var_hist.capitalize()}')
    
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# 4. Scatter Plot Dinámico con Color
st.subheader('📈 Análisis de Relación')
build_scatter_plot = st.checkbox('Construir scatter plot')

if build_scatter_plot:
    # Dividimos en 3 columnas para que los selectores queden alineados
    col1, col2, col3 = st.columns(3)
    
    with col1:
        var_x = st.selectbox(
            'Eje X:', 
            columnas, 
            index=columnas.index('odometer') if 'odometer' in columnas else 0
        )
    with col2:
        var_y = st.selectbox(
            'Eje Y:', 
            columnas, 
            index=columnas.index('price') if 'price' in columnas else 0
        )
    with col3:
        var_color = st.selectbox(
            'Color (Categoría):', 
            columnas, 
            index=columnas.index('condition') if 'condition' in columnas else 0
        )

    st.write(f'Relacionando **{var_x}** vs **{var_y}** agrupado por **{var_color}**')

    # Usamos Plotly Express para mapear el color automáticamente
    fig = px.scatter(car_data, x=var_x, y=var_y, color=var_color)
    fig.update_layout(title_text=f'Relación: {var_x.capitalize()} vs {var_y.capitalize()}')
    
    st.plotly_chart(fig, use_container_width=True)