import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')


cols_numericas = car_data.select_dtypes(include=['float64', 'int64']).columns.tolist()
cols_categoricas = car_data.select_dtypes(include=['object']).columns.tolist()

st.header('🚗 ¡Hola terrícolas! Bienvenidos a la app de anuncios de coches.')


st.subheader('🔍 Vista previa de las variables')
if st.checkbox('Mostrar datos sin procesar'):
    st.dataframe(car_data.head())

st.divider()


st.sidebar.header('⚙️ Filtros de datos')
precio_maximo = st.sidebar.slider(
    'Precio máximo de los vehículos:', 
    min_value=0, 
    max_value=100000, # Ponemos un tope lógico
    value=50000,      # Valor por defecto
    step=1000
)

# Filtramos el dataframe original según lo que elija el usuario
df_filtrado = car_data[car_data['price'] <= precio_maximo]

# 3. Histograma Dinámico
st.subheader('📊 Análisis de Distribución')
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    var_hist = st.selectbox(
        'Selecciona la variable a distribuir:', 
        cols_numericas, # Solo mostramos las numéricas
        index=cols_numericas.index('odometer') if 'odometer' in cols_numericas else 0
    )
    
    df_hist = df_filtrado.dropna(subset=[var_hist])
    
    st.write(f'Creación de un histograma para la variable: **{var_hist}**')

    fig = px.histogram(df_hist, x=var_hist, nbins=50)
    fig.update_layout(title_text=f'Distribución de {var_hist.capitalize()}')
    
    st.plotly_chart(fig, use_container_width=True)

st.divider()


st.subheader('📈 Análisis de Relación')
build_scatter_plot = st.checkbox('Construir scatter plot')

if build_scatter_plot:
    col1, col2, col3 = st.columns(3)
    
    with col1:
        var_x = st.selectbox('Eje X (Numérico):', cols_numericas, index=cols_numericas.index('odometer') if 'odometer' in cols_numericas else 0)
    with col2:
        var_y = st.selectbox('Eje Y (Numérico):', cols_numericas, index=cols_numericas.index('price') if 'price' in cols_numericas else 0)
    with col3:
        var_color = st.selectbox('Color (Categoría):', cols_categoricas, index=cols_categoricas.index('condition') if 'condition' in cols_categoricas else 0)

    st.write(f'Relacionando **{var_x}** vs **{var_y}** agrupado por **{var_color}**')

    df_scatter = df_filtrado.dropna(subset=[var_x, var_y, var_color])

    fig = px.scatter(df_scatter, x=var_x, y=var_y, color=var_color, opacity=0.5)
    fig.update_layout(title_text=f'Relación: {var_x.capitalize()} vs {var_y.capitalize()}')
    
    st.plotly_chart(fig, use_container_width=True)