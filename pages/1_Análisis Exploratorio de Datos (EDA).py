import streamlit as st
import pandas as pd
import requests
import json
import os
import altair as alt


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
def map_custom_labels(df):
    if df is not None:
        # Map GRAVEDAD if present to human-readable labels
        if 'GRAVEDAD' in df.columns:
            gravity_mapping = {
                'h': 'Con Heridos 👤',
                'd': 'Solo Daños 🚗',
                'm': 'Con Muertos 💀',
                'H': 'Con Heridos 👤',
                'D': 'Solo Daños 🚗',
                'M': 'Con Muertos 💀'
            }
            df['GRAVEDAD'] = df['GRAVEDAD'].replace(gravity_mapping)
    return df

@st.cache_data
def load_data_from_file(file_path):
    try:
        df = pd.read_csv(file_path)
        df.columns = [col.strip() for col in df.columns]
        df = map_custom_labels(df)
        return df
    except Exception as e:
        st.error(f"Error al cargar {file_path}: {e}")
        return None

@st.cache_data
def load_data_from_upload(file):
    try:
        df = pd.read_csv(file)
        df.columns = [col.strip() for col in df.columns]
        df = map_custom_labels(df)
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
        df = map_custom_labels(df)
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
            df = map_custom_labels(df)
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
    
    col_cal1, col_cal2 = st.columns(2)
    
    missing_data = df.isnull().sum()
    missing_percent = (df.isnull().sum() / len(df)) * 100
    duplicados_count = df.duplicated().sum()
    
    with col_cal1:
        st.metric("Total de Celdas Nulas", missing_data.sum())
    with col_cal2:
        st.metric("Total de Filas Duplicadas", duplicados_count)
        
    if duplicados_count > 0:
        st.warning(f"Se detectaron {duplicados_count} filas duplicadas en el conjunto de datos.")
        eliminar_dups = st.checkbox("Aplicar Limpieza Avanzada (Eliminar duplicados automáticamente con drop_duplicates)", value=True)
        if eliminar_dups:
            df = df.drop_duplicates()
            st.success("¡Filas duplicadas eliminadas con éxito en el DataFrame de análisis!")
            
    if missing_data.sum() > 0:
        st.subheader("Atributos con Valores Nulos Detectados")
        missing_df = pd.DataFrame({
            'Columna': missing_data.index,
            'Nulos': missing_data.values,
            'Porcentaje Nulos': missing_percent.values.round(2)
        })
        missing_df = missing_df[missing_df['Nulos'] > 0].sort_values('Porcentaje Nulos', ascending=False)
        st.dataframe(missing_df, use_container_width=True)
        
        limpiar_nulos = st.checkbox("Rellenar valores nulos automáticamente (Limpieza con fillna)", value=True)
        if limpiar_nulos:
            for col in df.columns:
                if df[col].dtype in ['int64', 'float64']:
                    df[col] = df[col].fillna(df[col].median())
                else:
                    df[col] = df[col].fillna("Sin Registro")
            st.success("¡Valores nulos rellenados automáticamente con la mediana/texto por defecto usando fillna!")
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

    # --- Paso 5: Visualización Exploratoria Dinámica y Gráficos Premium ---
    st.divider()
    st.markdown("""
    <h2 class="tech-header">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#A78BFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 6px #A78BFA); vertical-align: middle; margin-right: 12px;">
            <path d="M21.21 15.89A10 10 0 1 1 8 2.83"/>
            <path d="M22 12A10 10 0 0 0 12 2v10z"/>
        </svg>Visualización Exploratoria Dinámica y Gráficos Premium
    </h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    Explora relaciones, distribuciones y conteos de forma interactiva. Selecciona qué variables del dataset deseas cruzar y graficar:
    """)
    
    tab_chart1, tab_chart2, tab_chart3, tab_chart4 = st.tabs([
        "📊 Gráfico de Frecuencias (Categóricas)", 
        "🍩 Proporciones y Distribución Circular",
        "📈 Relación y Dispersión (Numéricas)",
        "🔔 Distribución / Histograma"
    ])
    
    with tab_chart1:
        cat_cols_chart = df.select_dtypes(exclude=['number']).columns.tolist()
        if len(cat_cols_chart) > 0:
            col_chart_c1, col_chart_c2 = st.columns([1, 3])
            with col_chart_c1:
                selected_cat_col = st.selectbox(
                    "Selecciona una variable categórica:", 
                    options=cat_cols_chart, 
                    key="eda_cat_selectbox"
                )
                limite_elementos = st.slider(
                    "Número máximo de categorías a mostrar:", 
                    min_value=5, 
                    max_value=30, 
                    value=10,
                    key="eda_cat_slider"
                )
            
            with col_chart_c2:
                # Calculate counts - Renamed to standard clean columns to avoid issues with spaces/accents in Vega-Lite
                counts_df = df[selected_cat_col].value_counts().head(limite_elementos).reset_index()
                counts_df.columns = ["Categoria", "Cantidad"]
                
                # Plot beautiful bar chart with linear gradient
                bar_chart = alt.Chart(counts_df).mark_bar(
                    cornerRadiusTopLeft=8,
                    cornerRadiusTopRight=8,
                    fill=alt.Gradient(
                        gradient='linear',
                        stops=[
                            alt.GradientStop(color='#C084FC', offset=0),
                            alt.GradientStop(color='#EC4899', offset=0.5),
                            alt.GradientStop(color='#22D3EE', offset=1)
                        ]
                    )
                ).encode(
                    x=alt.X("Categoria:N", sort=None, title=selected_cat_col, axis=alt.Axis(labelAngle=-45, labelColor='#94A3B8', titleColor='#CBD5E1')),
                    y=alt.Y("Cantidad:Q", title="Frecuencia Absoluta", axis=alt.Axis(labelColor='#94A3B8', titleColor='#CBD5E1')),
                    tooltip=["Categoria", "Cantidad"]
                ).properties(
                    height=380
                ).configure_axis(
                    gridColor='rgba(255, 255, 255, 0.05)'
                ).configure_view(
                    strokeOpacity=0
                )
                st.altair_chart(bar_chart, use_container_width=True)
        else:
            st.info("El dataset no contiene variables categóricas para graficar frecuencias.")
            
    with tab_chart2:
        cat_cols_chart = df.select_dtypes(exclude=['number']).columns.tolist()
        if len(cat_cols_chart) > 0:
            col_chart_p1, col_chart_p2 = st.columns([1, 2])
            with col_chart_p1:
                st.markdown("<h3 style='font-family:\"Space Grotesk\"; color:#22D3EE; margin-bottom:15px; font-size:1.4rem;'>🎛️ Panel de Telemetría</h3>", unsafe_allow_html=True)
                selected_pie_col = st.selectbox(
                    "Selecciona variable para distribución circular:", 
                    options=cat_cols_chart, 
                    key="eda_pie_selectbox"
                )
                limite_pie = st.slider(
                    "Mostrar top N categorías:", 
                    min_value=3, 
                    max_value=12, 
                    value=6,
                    key="eda_pie_slider"
                )
                tipo_grafico_circular = st.radio(
                    "Estilo del Gráfico Circular:",
                    options=[
                        "🍩 Dona Cibernética (Recomendado)", 
                        "🍕 Pie Tradicional", 
                        "🌹 Rosa de Nightingale (Rose Chart)", 
                        "🌀 Anillos Concéntricos (Radial Bar Chart)"
                    ],
                    key="eda_pie_style"
                )
                paleta_opcion = st.selectbox(
                    "Paleta de Color Futurista:",
                    options=["Cyberpunk Eléctrico", "Aurora Boreal", "Lava Solar", "Orquídea Galáctica"],
                    key="eda_pie_palette"
                )
            
            with col_chart_p2:
                # Calculate percentages - Renamed to standard clean columns to avoid issues with spaces/accents in Vega-Lite
                pie_counts = df[selected_pie_col].value_counts().head(limite_pie).reset_index()
                pie_counts.columns = ["Categoria", "Cantidad"]
                total_pie = df[selected_pie_col].value_counts().sum()
                pie_counts["Porcentaje"] = ((pie_counts["Cantidad"] / total_pie) * 100).round(1)
                
                # Colors based on selected palette
                domain_vals = [str(v) for v in pie_counts["Categoria"].unique()]
                if paleta_opcion == "Cyberpunk Eléctrico":
                    range_colors = ['#EC4899', '#22D3EE', '#C084FC', '#3B82F6', '#8B5CF6', '#F472B6', '#06B6D4', '#6366F1', '#A855F7', '#1E40AF']
                elif paleta_opcion == "Aurora Boreal":
                    range_colors = ['#10B981', '#14B8A6', '#06B6D4', '#22C55E', '#84CC16', '#34D399', '#2DD4BF', '#0891B2', '#15803D', '#4D7C0F']
                elif paleta_opcion == "Lava Solar":
                    range_colors = ['#F59E0B', '#EF4444', '#F97316', '#D97706', '#DC2626', '#EA580C', '#EC4899', '#F472B6', '#E11D48', '#B91C1C']
                else: # Orquídea Galáctica
                    range_colors = ['#8B5CF6', '#EC4899', '#C084FC', '#6366F1', '#D946EF', '#A78BFA', '#818CF8', '#E9D5FF', '#F472B6', '#4F46E5']
                
                range_colors = range_colors[:len(domain_vals)]
                
                # Interactive selections (Legend click + Mouseover Hover Glow)
                legend_selection = alt.selection_point(fields=["Categoria"], bind='legend')
                hover_selection = alt.selection_point(on='mouseover', clear='mouseout')
                
                if "Dona" in tipo_grafico_circular:
                    pie_chart = alt.Chart(pie_counts).mark_arc(
                        innerRadius=120, 
                        outerRadius=180
                    ).encode(
                        theta=alt.Theta("Cantidad:Q", stack=True),
                        color=alt.Color(
                            "Categoria:N", 
                            scale=alt.Scale(domain=domain_vals, range=range_colors),
                            legend=alt.Legend(title=selected_pie_col, labelColor='#94A3B8', titleColor='#CBD5E1')
                        ),
                        stroke=alt.condition(hover_selection, alt.value('#FFFFFF'), alt.value('rgba(255, 255, 255, 0.15)')),
                        strokeWidth=alt.condition(hover_selection, alt.value(3.5), alt.value(1.2)),
                        opacity=alt.condition(legend_selection, alt.value(0.9), alt.value(0.25)),
                        tooltip=["Categoria", "Cantidad", alt.Tooltip("Porcentaje:Q", format=".1f", title="Porcentaje (%)")]
                    ).add_params(
                        legend_selection,
                        hover_selection
                    ).properties(
                        height=500
                    ).configure_view(
                        strokeOpacity=0
                    )
                    
                elif "Pie" in tipo_grafico_circular:
                    pie_chart = alt.Chart(pie_counts).mark_arc(
                        innerRadius=0, 
                        outerRadius=180
                    ).encode(
                        theta=alt.Theta("Cantidad:Q", stack=True),
                        color=alt.Color(
                            "Categoria:N", 
                            scale=alt.Scale(domain=domain_vals, range=range_colors),
                            legend=alt.Legend(title=selected_pie_col, labelColor='#94A3B8', titleColor='#CBD5E1')
                        ),
                        stroke=alt.condition(hover_selection, alt.value('#FFFFFF'), alt.value('rgba(255, 255, 255, 0.15)')),
                        strokeWidth=alt.condition(hover_selection, alt.value(3.5), alt.value(1.2)),
                        opacity=alt.condition(legend_selection, alt.value(0.9), alt.value(0.25)),
                        tooltip=["Categoria", "Cantidad", alt.Tooltip("Porcentaje:Q", format=".1f", title="Porcentaje (%)")]
                    ).add_params(
                        legend_selection,
                        hover_selection
                    ).properties(
                        height=500
                    ).configure_view(
                        strokeOpacity=0
                    )
                    
                elif "Rosa" in tipo_grafico_circular:
                    pie_counts["Angulo"] = 1
                    pie_chart = alt.Chart(pie_counts).mark_arc(
                        innerRadius=35
                    ).encode(
                        theta=alt.Theta("Angulo:Q", stack=True),
                        radius=alt.Radius("Cantidad:Q", scale=alt.Scale(type="sqrt", range=[60, 200])),
                        color=alt.Color(
                            "Categoria:N", 
                            scale=alt.Scale(domain=domain_vals, range=range_colors),
                            legend=alt.Legend(title=selected_pie_col, labelColor='#94A3B8', titleColor='#CBD5E1')
                        ),
                        stroke=alt.condition(hover_selection, alt.value('#FFFFFF'), alt.value('rgba(255, 255, 255, 0.15)')),
                        strokeWidth=alt.condition(hover_selection, alt.value(3.5), alt.value(1.2)),
                        opacity=alt.condition(legend_selection, alt.value(0.9), alt.value(0.25)),
                        tooltip=["Categoria", "Cantidad", alt.Tooltip("Porcentaje:Q", format=".1f", title="Porcentaje (%)")]
                    ).add_params(
                        legend_selection,
                        hover_selection
                    ).properties(
                        height=500
                    ).configure_view(
                        strokeOpacity=0
                    )
                    
                else: # Anillos Concéntricos (Radial Bar Chart)
                    pie_counts = pie_counts.reset_index(drop=True)
                    pie_counts["r_inner"] = 60 + pie_counts.index * 22
                    pie_counts["r_outer"] = 78 + pie_counts.index * 22
                    
                    pie_chart = alt.Chart(pie_counts).mark_arc(
                        strokeOpacity=0.5
                    ).encode(
                        theta=alt.Theta("Porcentaje:Q", scale=alt.Scale(domain=[0, 100], range=[0, 270])),
                        radius=alt.Radius("r_outer:Q", scale=alt.Scale(zero=False)),
                        radius2=alt.Radius2("r_inner:Q"),
                        color=alt.Color(
                            "Categoria:N", 
                            scale=alt.Scale(domain=domain_vals, range=range_colors),
                            legend=alt.Legend(title=selected_pie_col, labelColor='#94A3B8', titleColor='#CBD5E1')
                        ),
                        stroke=alt.condition(hover_selection, alt.value('#FFFFFF'), alt.value('rgba(255, 255, 255, 0.08)')),
                        strokeWidth=alt.condition(hover_selection, alt.value(3.5), alt.value(1.2)),
                        opacity=alt.condition(legend_selection, alt.value(0.9), alt.value(0.25)),
                        tooltip=["Categoria", "Cantidad", alt.Tooltip("Porcentaje:Q", format=".1f", title="Porcentaje (%)")]
                    ).add_params(
                        legend_selection,
                        hover_selection
                    ).properties(
                        height=500
                    ).configure_view(
                        strokeOpacity=0
                    )
                
                # Render the high-end circular chart
                st.altair_chart(pie_chart, use_container_width=True)
                
            # Render a gorgeous HUD metrics overlay inside the control panel
            with col_chart_p1:
                st.markdown("<h4 style='font-family:\"Space Grotesk\"; color:#E2E8F0; margin-top:20px; font-size:1.1rem; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom:6px;'>📊 Telemetría de Proporciones</h4>", unsafe_allow_html=True)
                for i, row in pie_counts.iterrows():
                    color = range_colors[i % len(range_colors)]
                    st.markdown(f"""
                    <div style="
                        background: rgba(11, 15, 25, 0.45);
                        border-left: 4px solid {color};
                        border-radius: 8px;
                        padding: 10px 14px;
                        margin-bottom: 8px;
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
                        border: 1px solid rgba(255,255,255,0.02);
                        transition: transform 0.2s ease-in-out;
                    ">
                        <span style="font-family: 'Outfit'; color: #CBD5E1; font-size: 0.9rem; font-weight: 500;">{row['Categoria']}</span>
                        <span style="font-family: 'Outfit'; color: {color}; font-size: 0.95rem; font-weight: 700;">{row['Porcentaje']}% <span style='color:#64748B; font-size:0.8rem; font-weight:400;'>({row['Cantidad']})</span></span>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.info("El dataset no contiene variables categóricas para graficar proporciones circulares.")
            
    with tab_chart3:
        num_cols_chart = df.select_dtypes(include=['number']).columns.tolist()
        cat_cols_chart = df.select_dtypes(exclude=['number']).columns.tolist()
        
        if len(num_cols_chart) >= 2:
            col_chart_s1, col_chart_s2 = st.columns([1, 3])
            with col_chart_s1:
                selected_x_col = st.selectbox(
                    "Selecciona variable para el eje X:", 
                    options=num_cols_chart, 
                    index=0,
                    key="eda_x_selectbox"
                )
                selected_y_col = st.selectbox(
                    "Selecciona variable para el eje Y:", 
                    options=num_cols_chart, 
                    index=min(1, len(num_cols_chart)-1),
                    key="eda_y_selectbox"
                )
                color_opt = ["Ninguno"] + cat_cols_chart
                selected_color_col = st.selectbox(
                    "Colorizar puntos por (Categoría):", 
                    options=color_opt, 
                    key="eda_color_selectbox"
                )
                
            with col_chart_s2:
                # Color encoding
                if selected_color_col != "Ninguno":
                    domain_vals = [str(v) for v in df[selected_color_col].dropna().unique()][:10]
                    range_colors = ['#EC4899', '#22D3EE', '#C084FC', '#F59E0B', '#10B981', '#EF4444', '#6366F1', '#8B5CF6', '#EC4899', '#3B82F6'][:len(domain_vals)]
                    color_encoding = alt.Color(
                        field=selected_color_col,
                        type="nominal",
                        scale=alt.Scale(domain=domain_vals, range=range_colors),
                        legend=alt.Legend(title=selected_color_col, labelColor='#94A3B8', titleColor='#CBD5E1')
                    )
                else:
                    color_encoding = alt.value('#22D3EE')
                    
                scatter_chart = alt.Chart(df).mark_circle(size=100, opacity=0.75).encode(
                    x=alt.X(field=selected_x_col, type="quantitative", scale=alt.Scale(zero=False), title=selected_x_col, axis=alt.Axis(labelColor='#94A3B8', titleColor='#CBD5E1')),
                    y=alt.Y(field=selected_y_col, type="quantitative", scale=alt.Scale(zero=False), title=selected_y_col, axis=alt.Axis(labelColor='#94A3B8', titleColor='#CBD5E1')),
                    color=color_encoding,
                    tooltip=[c for c in df.columns[:8]]
                ).properties(
                    height=380
                ).configure_axis(
                    gridColor='rgba(255, 255, 255, 0.05)'
                ).configure_view(
                    strokeOpacity=0
                )
                st.altair_chart(scatter_chart, use_container_width=True)
        else:
            st.info("Se requieren al menos 2 variables numéricas en el dataset para realizar cruces de dispersión.")
            
    with tab_chart4:
        num_cols_chart = df.select_dtypes(include=['number']).columns.tolist()
        if len(num_cols_chart) > 0:
            col_chart_h1, col_chart_h2 = st.columns([1, 3])
            with col_chart_h1:
                selected_dist_col = st.selectbox(
                    "Selecciona una variable numérica:", 
                    options=num_cols_chart, 
                    key="eda_dist_selectbox"
                )
                num_bins = st.slider(
                    "Número de intervalos (Bins):", 
                    min_value=5, 
                    max_value=50, 
                    value=15,
                    key="eda_dist_slider"
                )
                
            with col_chart_h2:
                hist_chart = alt.Chart(df).mark_bar(
                    cornerRadiusTopLeft=6,
                    cornerRadiusTopRight=6,
                    fill=alt.Gradient(
                        gradient='linear',
                        stops=[
                            alt.GradientStop(color='#22D3EE', offset=0),
                            alt.GradientStop(color='#EC4899', offset=1)
                        ]
                    )
                ).encode(
                    x=alt.X(field=selected_dist_col, type="quantitative", bin=alt.Bin(maxbins=num_bins), title=selected_dist_col, axis=alt.Axis(labelColor='#94A3B8', titleColor='#CBD5E1')),
                    y=alt.Y("count()", title="Frecuencia (Registros)", axis=alt.Axis(labelColor='#94A3B8', titleColor='#CBD5E1')),
                    tooltip=[alt.Tooltip(field=selected_dist_col, type="quantitative", bin=True, title="Rango"), alt.Tooltip("count()", title="Cantidad")]
                ).properties(
                    height=380
                ).configure_axis(
                    gridColor='rgba(255, 255, 255, 0.05)'
                ).configure_view(
                    strokeOpacity=0
                )
                st.altair_chart(hist_chart, use_container_width=True)
        else:
            st.info("El dataset no contiene variables numéricas para graficar distribuciones.")

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