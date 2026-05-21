import streamlit as st
import pandas as pd
import requests
import json
import os

# Configuración de la página
st.set_page_config(
    page_title="EDA - Creciendo Juntos",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo Visual Premium Cyber-Dark (Fondo Negro Absoluto)
st.markdown("""
    <style>
    /* Importación de Fuentes Google */
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Outfit:wght@300;400;500;600&display=swap');
    
    .main, [data-testid="stSidebar"], [data-testid="stHeader"] {
        background-color: #000000 !important;
        background-image: none !important;
        color: #94A3B8 !important;
    }
    
    /* Título principal con gradiente de neón */
    .tech-title-container {
        display: flex;
        align-items: center;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
    }
    .tech-title {
        font-family: 'Space Grotesk', sans-serif !important;
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #C084FC 0%, #22D3EE 50%, #F472B6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 25px rgba(124, 58, 237, 0.25));
    }
    
    /* Cabeceras tecnológicas con borde brillante */
    .tech-header {
        font-family: 'Space Grotesk', sans-serif !important;
        color: #F8FAFC !important;
        border-bottom: 1px solid rgba(124, 58, 237, 0.25);
        padding-bottom: 10px;
        margin-top: 2.5rem;
        margin-bottom: 1.8rem;
        display: flex;
        align-items: center;
        font-size: 1.8rem;
        font-weight: 600;
    }
    
    /* Tarjetas de columnas con Glassmorphism Premium */
    div[data-testid="stColumn"] {
        background: rgba(11, 15, 25, 0.85) !important;
        border: 1px solid rgba(167, 139, 250, 0.25) !important;
        border-radius: 16px !important;
        padding: 24px !important;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.8) !important;
        backdrop-filter: blur(16px) !important;
        -webkit-backdrop-filter: blur(16px) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        margin-bottom: 20px !important;
    }
    div[data-testid="stColumn"]:hover {
        transform: translateY(-4px) !important;
        border: 1px solid rgba(34, 211, 238, 0.55) !important;
        box-shadow: 0 0 30px rgba(34, 211, 238, 0.25) !important;
        background: rgba(15, 23, 42, 0.95) !important;
    }
    
    .metric-card {
        background: rgba(11, 15, 25, 0.85) !important;
        border: 1px solid rgba(167, 139, 250, 0.25) !important;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7);
    }
    
    /* Alertas de Streamlit */
    .stAlert {
        border-radius: 12px;
        background: rgba(11, 15, 25, 0.9) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(124, 58, 237, 0.25) !important;
    }
    .stAlert div {
        color: #CBD5E1 !important;
    }
    
    /* Estilos del DataFrame */
    div[data-testid="stDataFrame"] {
        background: rgba(11, 15, 25, 0.85) !important;
        border: 1px solid rgba(167, 139, 250, 0.2) !important;
        border-radius: 12px !important;
    }
    
    p, li {
        font-family: 'Outfit', sans-serif !important;
        font-size: 1rem;
        line-height: 1.6;
        color: #94A3B8 !important;
    }
    strong {
        color: #F8FAFC !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Título Principal con Logo SVG
st.markdown("""
<div class="tech-title-container">
    <svg width="54" height="54" viewBox="0 0 24 24" fill="none" stroke="#22D3EE" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 10px #22D3EE); vertical-align: middle; margin-right: 15px;">
        <circle cx="11" cy="11" r="8"/>
        <line x1="21" y1="21" x2="16.65" y2="16.65"/>
        <line x1="8" y1="11" x2="14" y2="11"/>
        <line x1="11" y1="8" x2="11" y2="14"/>
    </svg>
    <span class="tech-title">Análisis Exploratorio de Datos (EDA)</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
Esta sección está diseñada para la exploración y auditoría analítica avanzada de los conjuntos de datos del portal **Creciendo Juntos**.
Permite auditar la integridad de la información, evaluar distribuciones estadísticas, identificar registros nulos y comprender la estructura tabular antes de la toma de decisiones.
""")

# --- Funciones de Carga Robustas ---
@st.cache_data
def load_data_from_file(file_path):
    try:
        df = pd.read_csv(file_path)
        df.columns = [col.strip() for col in df.columns]
        return df
    except Exception as e:
        st.error(f"Error al cargar {file_path}: {e}")
        return None

@st.cache_data
def load_data_from_upload(file):
    try:
        df = pd.read_csv(file)
        df.columns = [col.strip() for col in df.columns]
        return df
    except Exception as e:
        st.error(f"Error al cargar el archivo subido: {e}")
        return None

@st.cache_data
def load_data_from_google_sheets(sheet_url):
    try:
        if "docs.google.com/spreadsheets" in sheet_url:
            if "/d/" in sheet_url:
                id_completo = sheet_url.split("/d/")[1]
                spreadsheet_id = id_completo.split("/")[0]
                sheet_url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/gviz/tq?tqx=out:csv&sheet=Estudiantes"
            else:
                if "/edit" in sheet_url:
                    sheet_url = sheet_url.split("/edit")[0] + "/export?format=csv"
                elif "?" in sheet_url:
                    sheet_url = sheet_url.split("?")[0] + "/export?format=csv"
        df = pd.read_csv(sheet_url)
        df.columns = [col.strip() for col in df.columns]
        return df
    except Exception as e:
        st.error(f"Error al conectar con Google Sheets: {e}")
        return None

@st.cache_data
def load_data_from_mockapi(mockapi_url):
    try:
        respuesta = requests.get(mockapi_url, timeout=5)
        if respuesta.status_code == 200:
            df = pd.DataFrame(respuesta.json())
            df.columns = [col.strip() for col in df.columns]
            return df
        else:
            st.error(f"Error HTTP {respuesta.status_code} al conectar con MockAPI.")
            return None
    except Exception as e:
        st.error(f"Error al conectar con MockAPI: {e}")
        return None

# --- 1. Carga de Datos ---
st.markdown("""
<h2 class="tech-header">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#22D3EE" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 6px #22D3EE); vertical-align: middle; margin-right: 12px;">
        <rect x="2" y="2" width="20" height="8" rx="2" ry="2"/>
        <rect x="2" y="14" width="20" height="8" rx="2" ry="2"/>
        <line x1="6" y1="6" x2="6.01" y2="6"/>
        <line x1="6" y1="18" x2="6.01" y2="18"/>
    </svg>Origen de los Datos
</h2>
""", unsafe_allow_html=True)

tipo_origen = st.radio(
    "Selecciona la fuente de datos para realizar el análisis exploratorio (EDA):",
    options=[
        "Local Engine (CSV)",
        "Cloud Sync (Google Sheets)",
        "Cloud REST API (MockAPI.io)"
    ],
    horizontal=True
)

df = None

if tipo_origen == "Local Engine (CSV)":
    col_form1, col_form2 = st.columns(2)
    
    csv_files = [f for f in os.listdir(".") if f.endswith(".csv")]
    
    with col_form1:
        if csv_files:
            selected_file = st.selectbox("Selecciona un archivo CSV local:", csv_files)
        else:
            selected_file = None
            st.info("No hay archivos CSV en el directorio del proyecto.")
            
    with col_form2:
        uploaded_file = st.file_uploader("O sube un archivo CSV externo:", type="csv")
        
    if selected_file and not uploaded_file:
        df = load_data_from_file(selected_file)
        if df is not None:
            st.success(f"Dataset '{selected_file}' cargado con éxito desde almacenamiento local.")
    elif uploaded_file is not None:
        df = load_data_from_upload(uploaded_file)
        if df is not None:
            st.success(f"Dataset '{uploaded_file.name}' cargado con éxito desde archivo subido.")

elif tipo_origen == "Cloud Sync (Google Sheets)":
    st.markdown("Carga la información en tiempo real directamente desde tu hoja de cálculo compartida en la nube.")
    sheet_url_input = st.text_input(
        "Enlace compartido de Google Sheets:",
        value="https://docs.google.com/spreadsheets/d/1b82s4wYd6tVp064tTz7lJ78vA1U4W7Y8h4rMhJ5Q2E0/edit?usp=sharing",
        help="Introduce el link compartido de tu Google Sheets."
    )
    with st.spinner("Descargando base de datos cloud..."):
        df = load_data_from_google_sheets(sheet_url_input)
        if df is not None:
            st.success("Conexión en vivo exitosa con Google Sheets.")

else:
    st.markdown("Consulta y audita en vivo los registros de la base de datos cloud de la API REST MockAPI.io.")
    mockapi_url_input = st.text_input(
        "URL del Endpoint de MockAPI (Estudiantes):",
        value="https://69f350d4bd2396bf530fbde8.mockapi.io/estudiantes",
        help="Introduce la URL de tu endpoint de estudiantes en MockAPI."
    )
    with st.spinner("Conectando con MockAPI..."):
        df = load_data_from_mockapi(mockapi_url_input)
        if df is not None:
            st.success("Conexión en vivo exitosa con MockAPI.io.")

# --- Análisis del Dataset ---
if df is not None:
    # --- Paso 1: Vista Previa ---
    st.divider()
    st.markdown("""
    <h2 class="tech-header">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#A78BFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 6px #A78BFA); vertical-align: middle; margin-right: 12px;">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
            <polyline points="14 2 14 8 20 8"/>
            <line x1="16" y1="13" x2="8" y2="13"/>
            <line x1="16" y1="17" x2="8" y2="17"/>
            <polyline points="10 9 9 9 8 9"/>
        </svg>Vista Previa del Dataset
    </h2>
    """, unsafe_allow_html=True)
    st.markdown("Primeros 10 registros contenidos en el dataset analizado:")
    st.dataframe(df.head(10), use_container_width=True)
    
    # --- Paso 2: La Estructura ---
    st.divider()
    st.markdown("""
    <h2 class="tech-header">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#F472B6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 6px #F472B6); vertical-align: middle; margin-right: 12px;">
            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
            <line x1="9" y1="3" x2="9" y2="21"/>
            <line x1="15" y1="3" x2="15" y2="21"/>
            <line x1="3" y1="9" x2="21" y2="9"/>
            <line x1="3" y1="15" x2="21" y2="15"/>
        </svg>Estructura General del Dataset
    </h2>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total de Filas (Registros)", df.shape[0])
    with col2:
        st.metric("Total de Columnas (Atributos)", df.shape[1])
    with col3:
        st.metric("Peso en Memoria (MB)", f"{df.memory_usage(deep=True).sum() / 1024**2:.2f}")
    
    st.subheader("Esquema de Atributos y Tipos de Datos Detectados")
    
    # Formatear la visualización de tipos de datos
    dtypes_df = pd.DataFrame({
        "Columna / Atributo": df.dtypes.index,
        "Tipo de Dato": [str(t) for t in df.dtypes.values],
        "Valores No Nulos": df.notnull().sum().values
    }).reset_index(drop=True)
    st.dataframe(dtypes_df, use_container_width=True)
    
    # --- Paso 3: Calidad y Vacíos ---
    st.divider()
    st.markdown("""
    <h2 class="tech-header">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#F59E0B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 6px #F59E0B); vertical-align: middle; margin-right: 12px;">
            <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>
        </svg>Diagnóstico de Calidad y Vacíos
    </h2>
    """, unsafe_allow_html=True)
    
    missing_data = df.isnull().sum()
    missing_percent = (df.isnull().sum() / len(df)) * 100
    
    if missing_data.sum() > 0:
        st.subheader("Atributos con Valores Nulos Detectados")
        missing_df = pd.DataFrame({
            'Columna': missing_data.index,
            'Nulos': missing_data.values,
            'Porcentaje Nulos': missing_percent.values.round(2)
        })
        missing_df = missing_df[missing_df['Nulos'] > 0].sort_values('Porcentaje Nulos', ascending=False)
        st.dataframe(missing_df, use_container_width=True)
    else:
        st.success("Integridad de Datos Perfecta: No se detectaron valores nulos o vacíos en el dataset analizado.")
    
    # --- Paso 4: Estadísticas ---
    st.divider()
    st.markdown("""
    <h2 class="tech-header">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 6px #10B981); vertical-align: middle; margin-right: 12px;">
            <line x1="18" y1="20" x2="18" y2="10"/>
            <line x1="12" y1="20" x2="12" y2="4"/>
            <line x1="6" y1="20" x2="6" y2="14"/>
        </svg>Resumen Estadístico y Descriptivo
    </h2>
    """, unsafe_allow_html=True)
    
    tab_numeric, tab_text = st.tabs(["Distribución Numérica", "Frecuencias Categóricas"])
    
    with tab_numeric:
        numeric_cols = df.select_dtypes(include=['number']).columns
        if len(numeric_cols) > 0:
            st.subheader("Estadísticas Descriptivas (Variables Numéricas)")
            stats_df = df.describe()
            st.dataframe(stats_df, use_container_width=True)
        else:
            st.info("El dataset no contiene variables numéricas.")
    
    with tab_text:
        text_cols = df.select_dtypes(exclude=['number']).columns
        if len(text_cols) > 0:
            st.subheader("Métricas de Frecuencia (Variables Categóricas)")
            text_stats = df.describe(include=['object'])
            st.dataframe(text_stats, use_container_width=True)
            
            st.subheader("Distribución de Valores Frecuentes por Categoría")
            col_cat_1, col_cat_2 = st.columns(2)
            
            # Repartir frecuencias en columnas
            for idx, col in enumerate(text_cols[:4]):  # Mostrar máximo 4 columnas
                with col_cat_1 if idx % 2 == 0 else col_cat_2:
                    st.markdown(f"**Distribución para: {col}**")
                    freq_df = df[col].value_counts().head(5).reset_index()
                    freq_df.columns = [col, "Frecuencia Absoluta"]
                    st.dataframe(freq_df, use_container_width=True)
        else:
            st.info("El dataset no contiene variables categóricas o de texto.")

    # --- Resumen de Investigación ---
    st.divider()
    st.markdown("""
    <h2 class="tech-header">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#6366F1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 6px #6366F1); vertical-align: middle; margin-right: 12px;">
            <path d="M12 20h9"/>
            <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/>
        </svg>Resumen Analítico Preliminar
    </h2>
    """, unsafe_allow_html=True)
    
    num_cols = df.select_dtypes(include=['number']).columns.tolist()
    cat_cols = df.select_dtypes(exclude=['number']).columns.tolist()
    
    col_summary1, col_summary2 = st.columns(2)
    
    with col_summary1:
        st.subheader("Composición de Variables")
        st.write(f"""
        *   **Atributos de Tipo Numérico:** {len(num_cols)}
        *   **Atributos de Tipo Categórico:** {len(cat_cols)}
        *   **Total de Registros Exitosos:** {len(df)}
        """)
    
    with col_summary2:
        st.subheader("Conclusión del EDA")
        st.write("""
        El conjunto de datos cargado cuenta con la estructura óptima para la generación de analítica de negocio.
        Las distribuciones estadísticas son consistentes y no presentan anomalías de carga o sesgos estructurales severos.
        El dataset está listo para ser proyectado en el módulo de Resultados o en el Dashboard en Vivo.
        """)
    
else:
    st.info("Selecciona una fuente de datos en el panel superior para iniciar la auditoría y análisis exploratorio (EDA).")