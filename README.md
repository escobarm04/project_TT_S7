# 🚗 Vehículos US - Dashboard Interactivo

¡Bienvenido al proyecto de análisis de mercado de vehículos usados! Esta aplicación web interactiva está construida con Python y Streamlit, diseñada para explorar, visualizar y entender la distribución y relación de las características de coches en venta en Estados Unidos.

## ✨ Características Principales

*   **Exploración de Datos Crudos:** Tabla interactiva para inspeccionar los registros de la base de datos directamente en el navegador.
*   **Histogramas Dinámicos:** Selecciona cualquier variable numérica o categórica del dataset para analizar su distribución al instante.
*   **Gráficos de Dispersión Avanzados:** Mapea relaciones entre múltiples variables seleccionando el Eje X, el Eje Y y diferenciando subgrupos mediante una tercera variable categórica por color usando Plotly Express.

## 🛠 Tecnologías Utilizadas

Este proyecto fue desarrollado utilizando el siguiente ecosistema de herramientas:
*   **Python 3.11+**
*   **Pandas:** Limpieza y manipulación de la base de datos CSV.
*   **Plotly / Plotly Express:** Motor de renderizado para gráficos interactivos.
*   **Streamlit:** Framework de desarrollo para levantar la interfaz web de manera ágil.
*   **Jupyter Notebook:** Entorno utilizado para el análisis exploratorio inicial y pruebas de código.

---

## 📦 Instalación y Configuración del Entorno (Paso a Paso)

Para replicar este proyecto en tu computadora local, todo el flujo de trabajo se maneja desde la terminal utilizando comandos Bash y Conda para aislar las dependencias.

### 1. Descarga de la base de datos
Utilizamos el comando `wget` para extraer el archivo original de datos desde Amazon S3 y guardarlo localmente:
```bash
wget -O vehicles_us.csv https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/Data_sprint_4_Refactored/vehicles_us.csv 
```


### 2. Creación del entorno virtual
Para evitar conflictos con otras librerías del sistema, construimos un ambiente aislado con Conda llamado env_TT_S7 e instalamos las paqueterías base desde nuestro archivo de requerimientos:
```bash
# Crear el ambiente con una versión específica de Python
conda create -n env_TT_S7 python=3.11

# Activar el ambiente
conda activate env_TT_S7

# Instalar librerías principales (Pandas, Plotly, Streamlit)
pip install -r requirements.txt
```

### 3. Configuración del motor de Jupyter (Análisis Exploratorio)
Para poder ejecutar nuestra libreta de experimentación (EDA.ipynb) directamente dentro de VS Code usando este mismo entorno, instalamos el motor interactivo (ipykernel) y el paquete de renderizado estricto para que las gráficas de Plotly funcionen en las celdas:
```bash
pip install ipykernel "nbformat>=4.2.0"
```
(Nota en VS Code: Tras la instalación, selecciona el entorno env_TT_S7 como el kernel activo en la esquina superior derecha y presiona el botón de "Restart" ↻).

### ▶️ Cómo ejecutar la aplicación web
Una vez que tu entorno esté activado y la base de datos descargada, asegúrate de estar en la carpeta raíz del proyecto y levanta el servidor local con el siguiente comando:
```bash
streamlit run app.py
```

Tu navegador predeterminado se abrirá automáticamente en http://localhost:8501 mostrando la interfaz interactiva.
Desarrollado con ☕, Bash y Python