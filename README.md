# 🚗 Vehículos US - Interactive Plots

¡Bienvenido al proyecto de análisis de mercado de vehículos usados! Esta aplicación web interactiva está construida con Python y Streamlit, diseñada para explorar, visualizar y entender la distribución y relación de las características de coches en venta.

## ✨ Características Principales

*   **Exploración de Datos Crudos:** Tabla interactiva para inspeccionar los primeros registros de la base de datos directamente en el navegador.
*   **Histogramas Dinámicos:** Selecciona cualquier variable numérica o categórica del dataset para analizar su distribución al instante.
*   **Gráficos de Dispersión Avanzados:** Mapea relaciones entre múltiples variables seleccionando el Eje X, el Eje Y y diferenciando subgrupos mediante una tercera variable categórica por color.

## 🛠️ Tecnologías Utilizadas

Este proyecto fue desarrollado utilizando el siguiente ecosistema de herramientas:
*   **Python 3.11+**
*   **Pandas:** Limpieza y manipulación de la base de datos CSV.
*   **Plotly / Plotly Express:** Motor de renderizado para gráficos interactivos (zoom, hover de datos).
*   **Streamlit:** Framework de desarrollo para levantar la interfaz web de manera ágil.

## 📦 Instalación y Configuración

Para correr este proyecto en tu computadora local, sigue estos pasos:

1. Clona este repositorio o descarga los archivos en tu máquina.
2. Es altamente recomendable utilizar un entorno virtual (como Conda o venv) para evitar conflictos con otras librerías.
3. Instala las dependencias necesarias leyendo el archivo de requerimientos:
   ```bash
   pip install -r requirements.txt