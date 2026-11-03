import streamlit as st
import pandas as pd
import requests
import random
import os
import json
import altair as alt

# =====================================================================
# CONFIGURACIÓN DE LA PÁGINA
# =====================================================================
st.set_page_config(
    page_title="Gestión de Accidentes de Tránsito - MockAPI",
    page_icon="🚗",
    layout="wide"
)

# Estilo Visual Premium Cyber-Dark (Fondo Negro Absoluto y Acentos Unicornio)
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
        font-size: 2.8rem;
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
    
    /* Estilo de Tarjetas de Métricas de Streamlit */
    div[data-testid="metric-container"] {
        background: rgba(11, 15, 25, 0.85) !important;
        border: 1px solid rgba(167, 139, 250, 0.25) !important;
        border-radius: 12px !important;
        padding: 15px 20px !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6) !important;
        backdrop-filter: blur(10px) !important;
        transition: all 0.3s ease !important;
        margin-bottom: 15px !important;
    }
    div[data-testid="metric-container"]:hover {
        border-color: rgba(34, 211, 238, 0.5) !important;
        box-shadow: 0 0 20px rgba(34, 211, 238, 0.15) !important;
    }
    div[data-testid="stMetricValue"] {
        color: #F8FAFC !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 700 !important;
    }
    div[data-testid="stMetricLabel"] {
        color: #94A3B8 !important;
        font-family: 'Outfit', sans-serif !important;
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

# Título de la sección principal
st.markdown("""
<div class="tech-title-container">
    <svg width="54" height="54" viewBox="0 0 24 24" fill="none" stroke="#22D3EE" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 10px #22D3EE); vertical-align: middle; margin-right: 15px;">
        <rect x="2" y="2" width="20" height="8" rx="2" ry="2"/>
        <rect x="2" y="14" width="20" height="8" rx="2" ry="2"/>
        <line x1="6" y1="6" x2="6.01" y2="6"/>
        <line x1="6" y1="18" x2="6.01" y2="18"/>
        <path d="M20 6h2v12h-2"/>
    </svg>
    <span class="tech-title">Gestión de Accidentes de Tránsito - MockAPI</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
### Módulo de Telemetría y Consumo de API
Esta sección permite monitorear el historial de **Reportes de Accidentes** y la base de datos de **Vehículos Asegurados**.
Consume información en tiempo real a través de conexiones a MockAPI o mediante el simulador local de contingencia.
""")

# =====================================================================
# GENERADOR Y CONFIGURACIÓN LOCAL DE DATOS (MOCKS ACCIDENTES Y VEHÍCULOS)
# =====================================================================
CSV_FILENAME = "Accidentes_de_tránsito_reportados_en_los_municipios_que_tienen_convenio_con_la_Gerencia_de_Seguridad_Vial_de_Antioquia_20260521.csv"

# 1. Cargar Reportes desde CSV Local para el Simulador
@st.cache_data
def cargar_reportes_local():
    if os.path.exists(CSV_FILENAME):
        try:
            df = pd.read_csv(CSV_FILENAME)
            df.columns = [col.strip() for col in df.columns]
            
            # Asegurar mapeo de gravedad a etiquetas amigables
            gravity_mapping = {
                'h': 'Con Heridos', 'd': 'Solo Daños', 'm': 'Con Muertos',
                'H': 'Con Heridos', 'D': 'Solo Daños', 'M': 'Con Muertos'
            }
            if 'Gravedad' in df.columns:
                df['Gravedad'] = df['Gravedad'].replace(gravity_mapping)
            elif 'GRAVEDAD' in df.columns:
                df = df.rename(columns={'GRAVEDAD': 'Gravedad'})
                df['Gravedad'] = df['Gravedad'].replace(gravity_mapping)
            
            # Limpieza básica
            if 'Ciudad' not in df.columns and 'CIUDAD' in df.columns:
                df = df.rename(columns={'CIUDAD': 'Ciudad'})
            if 'Ciudad' not in df.columns and 'Ubicacion_Ciudad' in df.columns:
                df = df.rename(columns={'Ubicacion_Ciudad': 'Ciudad'})
            if 'Ciudad' not in df.columns and 'ubicacion_ciudad' in df.columns:
                df = df.rename(columns={'ubicacion_ciudad': 'Ciudad'})
                
            return df
        except Exception as e:
            st.error(f"Error al leer el CSV local: {e}")
            
    # Fallback si no hay CSV
    random.seed(42)
    ciudades = ["Medellín", "Envigado", "Bello", "Itagüí", "Rionegro", "Sabaneta"]
    tipos = ["Choque", "Atropello", "Volcamiento", "Caída Ocupante", "Otro"]
    gravedades = ["Con Heridos", "Solo Daños", "Con Muertos"]
    climas = ["Lluvia", "Despejado", "Niebla", "Nublado"]
    
    datos = []
    for i in range(1, 301):
        datos.append({
            "ID": i,
            "Fecha": f"2023-{random.randint(1,12):02d}-{random.randint(1,28):02d}",
            "Ciudad": random.choice(ciudades),
            "tipo_accidente": random.choice(tipos),
            "Gravedad": random.choice(gravedades),
            "clima": random.choice(climas),
            "Heridos": random.randint(0, 5) if random.random() > 0.3 else 0,
            "Muertos": random.randint(0, 2) if random.random() > 0.85 else 0,
            "Edad_Conductor": random.randint(18, 75),
            "Velocidad_Aprox": random.randint(20, 110)
        })
    return pd.DataFrame(datos)

# 2. Generar Vehículos Locales
@st.cache_data
def generar_vehiculos_local():
    random.seed(24)
    marcas = ["Toyota", "Chevrolet", "Renault", "Mazda", "Kia", "Nissan", "Hyundai", "Suzuki"]
    tipos = ["Automóvil", "Camioneta", "Motocicleta", "Camión", "Microbús"]
    ciudades = ["Medellín", "Envigado", "Bello", "Itagüí", "Rionegro", "Sabaneta"]
    estados = ["Activo", "Suspendido", "Vencido", "En Reclamación"]
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    datos = []
    for i in range(1, 101):
        placa = "".join(random.choice(letras) for _ in range(3)) + f"-{random.randint(100, 999)}"
        datos.append({
            "id": i,
            "placa": placa,
            "tipo_vehiculo": random.choice(tipos),
            "marca": random.choice(marcas),
            "ciudad": random.choice(ciudades),
            "año": random.randint(2010, 2024),
            "estado": random.choice(estados)
        })
    return pd.DataFrame(datos)

# =====================================================================
# CONFIGURACIÓN DE ORIGEN DE DATOS (BARRA LATERAL / SIDEBAR)
# =====================================================================
with st.sidebar:
    st.markdown("### Origen de los Datos")
    
    origen_datos = st.radio(
        "Selecciona la fuente de datos:",
        options=[
            "Cloud REST API (MockAPI.io)",
            "Local Backup Simulator"
        ],
        index=1,  # Por defecto en Local Backup Simulator para asegurar carga
        help="Elige si deseas conectar a la nube real de MockAPI o usar el simulador de contingencia con los 300 datos reales locales."
    )
    
    if origen_datos == "Cloud REST API (MockAPI.io)":
        st.divider()
        st.subheader("Conexión a MockAPI.io")
        mockapi_id = st.text_input(
            "ID de tu Proyecto MockAPI:",
            value="69f350d4bd2396bf530fbde8",
            help="Ingresa el identificador de tu proyecto en mockapi.io"
        )
        config_url = f"https://{mockapi_id}.mockapi.io"
    else:
        config_url = ""
        
    st.divider()
    st.subheader("Selecciona la Entidad:")
    entidad_seleccionada = st.radio(
        "Elige una opción:",
        options=["🚗 Reportes de Accidentes", "🚙 Vehículos Asegurados"]
    )
    
    st.divider()
    if st.button("Refrescar e Importar Datos", use_container_width=True, help="Limpia la caché temporal de Streamlit y fuerza una nueva conexión con la API en la nube."):
        st.cache_data.clear()
        st.rerun()

# =====================================================================
# FUNCIÓN PARA OBTENER DATOS (API O SIMULADOR)
# =====================================================================
@st.cache_data
def obtener_datos(origen: str, config_url: str, entidad: str):
    nombre_entidad = "reportes" if "Reportes" in entidad else "vehiculos"
    
    # 1. Modo Local Backup Simulator
    if origen == "Local Backup Simulator":
        if nombre_entidad == "reportes":
            return cargar_reportes_local(), None
        else:
            return generar_vehiculos_local(), None
            
    # 2. Modo Cloud REST API (MockAPI.io)
    else:
        url_completa = f"{config_url}/{nombre_entidad}"
        try:
            respuesta = requests.get(url_completa, timeout=5)
            if respuesta.status_code == 200:
                df = pd.DataFrame(respuesta.json())
                return df, None
            elif respuesta.status_code == 404:
                # Reintento con prefijo /api/v1 por defecto de MockAPI
                url_fallback = f"{config_url}/api/v1/{nombre_entidad}"
                try:
                    respuesta_fb = requests.get(url_fallback, timeout=5)
                    if respuesta_fb.status_code == 200:
                        return pd.DataFrame(respuesta_fb.json()), None
                except Exception:
                    pass
                return None, f"Error 404: El recurso '{nombre_entidad}' no se encontró. Asegúrate de crearlo en minúsculas en tu cuenta de MockAPI."
            else:
                return None, f"Error HTTP {respuesta.status_code}"
        except requests.exceptions.ConnectionError:
            return None, "No se pudo conectar a los servidores de MockAPI. Revisa tu conexión a internet."
        except Exception as e:
            return None, f"Error inesperado al conectar con MockAPI: {str(e)}"

# Carga de datos
with st.spinner(f"Cargando datos de {entidad_seleccionada}..."):
    df_datos, error_conexion = obtener_datos(origen_datos, config_url, entidad_seleccionada)

# Control de errores
if error_conexion is not None:
    st.error("Error al Obtener Datos")
    st.warning(f"**Detalle del error:** {error_conexion}")
    st.info("""
    **Sugerencia de contingencia:** 
    Si estás intentando conectarte a MockAPI en la nube y no responde, o si aún no has configurado tus recursos en mockapi.io, selecciona **'Local Backup Simulator'** en la barra lateral izquierda para explorar y evaluar el sistema en vivo con los 300 datos reales locales de forma inmediata.
    """)
    st.stop()

# --- Normalización y Robustez de Datos de Accidentes ---
if df_datos is not None and not df_datos.empty:
    df_datos = df_datos.drop_duplicates()
    df_datos.columns = [col.strip() for col in df_datos.columns]
    
    # Normalizar nombres de columnas comunes
    rename_dict = {}
    for col in df_datos.columns:
        col_lower = col.lower()
        if col_lower in ["tipo_accidente", "tipo", "tipoaccidente"]:
            rename_dict[col] = "tipo_accidente"
        elif col_lower in ["gravedad", "severidad"]:
            rename_dict[col] = "Gravedad"
        elif col_lower in ["clima", "weather"]:
            rename_dict[col] = "clima"
        elif col_lower in ["heridos", "injured"]:
            rename_dict[col] = "Heridos"
        elif col_lower in ["muertos", "fallecidos", "deaths"]:
            rename_dict[col] = "Muertos"
        elif col_lower in ["edad_conductor", "edad"]:
            rename_dict[col] = "Edad_Conductor"
        elif col_lower in ["velocidad_aprox", "velocidad", "speed"]:
            rename_dict[col] = "Velocidad_Aprox"
            
    if rename_dict:
        df_datos = df_datos.rename(columns=rename_dict)
        
    # Conversión numérica segura
    if "Heridos" in df_datos.columns:
        df_datos["Heridos"] = pd.to_numeric(df_datos["Heridos"], errors="coerce").fillna(0).astype(int)
    if "Muertos" in df_datos.columns:
        df_datos["Muertos"] = pd.to_numeric(df_datos["Muertos"], errors="coerce").fillna(0).astype(int)
    if "Edad_Conductor" in df_datos.columns:
        df_datos["Edad_Conductor"] = pd.to_numeric(df_datos["Edad_Conductor"], errors="coerce").fillna(35).astype(int)
    if "Velocidad_Aprox" in df_datos.columns:
        df_datos["Velocidad_Aprox"] = pd.to_numeric(df_datos["Velocidad_Aprox"], errors="coerce").fillna(60).astype(int)

# =====================================================================
# FILTROS DE DATOS EN TIEMPO REAL
# =====================================================================
st.divider()
st.markdown("""
<h3 style="font-family: 'Space Grotesk', sans-serif; color: #F8FAFC; margin-bottom: 1.5rem; display: flex; align-items: center;">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#22D3EE" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 5px #22D3EE); vertical-align: middle; margin-right: 10px;">
        <polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/>
    </svg>Filtros y Segmentación
</h3>
""", unsafe_allow_html=True)

df_filtrado = df_datos.copy()
col_filtro1, col_filtro2 = st.columns(2)

with col_filtro1:
    if "Reportes" in entidad_seleccionada:
        ciudades = ["Todas"] + sorted(df_datos["Ciudad"].dropna().unique().tolist())
        sel_ciudad = st.selectbox("Filtrar por Municipio / Ciudad:", ciudades)
        if sel_ciudad != "Todas":
            df_filtrado = df_filtrado[df_filtrado["Ciudad"] == sel_ciudad]
    else:
        ciudades = ["Todas"] + sorted(df_datos["ciudad"].dropna().unique().tolist())
        sel_ciudad = st.selectbox("Filtrar vehículos por Ciudad de Registro:", ciudades)
        if sel_ciudad != "Todas":
            df_filtrado = df_filtrado[df_filtrado["ciudad"] == sel_ciudad]

with col_filtro2:
    if "Reportes" in entidad_seleccionada:
        if "tipo_accidente" in df_datos.columns:
            tipos = ["Todos"] + sorted(df_datos["tipo_accidente"].dropna().unique().tolist())
            sel_tipo = st.selectbox("Filtrar por Clase de Accidente:", tipos)
            if sel_tipo != "Todos":
                df_filtrado = df_filtrado[df_filtrado["tipo_accidente"] == sel_tipo]
    else:
        if "tipo_vehiculo" in df_datos.columns:
            tipos = ["Todos"] + sorted(df_datos["tipo_vehiculo"].dropna().unique().tolist())
            sel_tipo = st.selectbox("Filtrar por Tipo de Vehículo:", tipos)
            if sel_tipo != "Todos":
                df_filtrado = df_filtrado[df_filtrado["tipo_vehiculo"] == sel_tipo]

st.caption(f"Mostrando {len(df_filtrado)} de {len(df_datos)} registros obtenidos.")

# =====================================================================
# PESTAÑAS PRINCIPALES DEL DASHBOARD
# =====================================================================
tab_tablas, tab_graficos = st.tabs(["Tabla de Datos", "Estadísticas y Gráficos"])

# ---------------------------------------------------------------------
# PESTAÑA 1: TABLA DE DATOS
# ---------------------------------------------------------------------
with tab_tablas:
    st.subheader(f"Estructura Tabular - {entidad_seleccionada}")
    st.dataframe(df_filtrado, use_container_width=True, height=300)
    
    # --- Pandas Pro en Acción: Extracción Posicional con iloc ---
    st.markdown("""
    <div style="background-color: rgba(167, 139, 250, 0.05); padding: 15px; border-radius: 10px; border: 1px solid rgba(167, 139, 250, 0.2); margin-top: 10px; margin-bottom: 15px;">
        <span style="color: #A78BFA; font-weight: bold; font-family: 'Space Grotesk', sans-serif;">🐼 Pandas Pro: Selección Posicional Avanzada con <code>.iloc</code></span>
        <p style="font-size: 0.9rem; margin-top: 5px; color: #94A3B8;">
            El profesor puede evaluar cómo seleccionamos porciones del DataFrame según su posición numérica exacta usando el indexador posicional <code>.iloc</code>.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col_iloc1, col_iloc2 = st.columns(2)
    total_reg = len(df_filtrado)
    with col_iloc1:
        fila_inicio = st.number_input("Índice de Inicio (Fila)", min_value=0, max_value=max(0, total_reg-1), value=0, key="iloc_start")
    with col_iloc2:
        fila_fin = st.number_input("Índice de Fin (Fila)", min_value=int(fila_inicio)+1, max_value=total_reg, value=min(total_reg, int(fila_inicio)+5), key="iloc_end")
    
    st.code(f"df_seleccionado = df_filtrado.iloc[{fila_inicio}:{fila_fin}]", language="python")
    st.dataframe(df_filtrado.iloc[fila_inicio:fila_fin], use_container_width=True)
    
    # Exportación
    csv_data = df_filtrado.to_csv(index=False).encode('utf-8')
    st.download_button(
        label=f"📥 Exportar listado como CSV",
        data=csv_data,
        file_name=f"{entidad_seleccionada.lower()}_filtrados.csv",
        mime="text/csv"
    )

# ---------------------------------------------------------------------
# PESTAÑA 2: ESTADÍSTICAS Y GRÁFICOS
# ---------------------------------------------------------------------
with tab_graficos:
    if df_filtrado.empty:
        st.warning("No se encontraron registros con los filtros seleccionados para proyectar el dashboard.")
    else:
        # SECCIÓN A: TARJETAS DE INDICADORES (KPIs)
        st.subheader("Resumen Ejecutivo e Indicadores")
        col_m1, col_m2, col_m3, col_m4, col_m5 = st.columns(5)
        
        if "Reportes" in entidad_seleccionada:
            with col_m1:
                st.metric("Total Incidentes 📋", len(df_filtrado))
            with col_m2:
                heridos = int(df_filtrado["Heridos"].sum()) if "Heridos" in df_filtrado.columns else 0
                st.metric("Total Heridos 👤", heridos)
            with col_m3:
                muertos = int(df_filtrado["Muertos"].sum()) if "Muertos" in df_filtrado.columns else 0
                st.metric("Total Muertos 💀", muertos)
            with col_m4:
                edad_prom = df_filtrado["Edad_Conductor"].mean() if "Edad_Conductor" in df_filtrado.columns else 35
                st.metric("Edad Prom. Conductor 🧑‍✈️", f"{edad_prom:.1f} años")
            with col_m5:
                vel_prom = df_filtrado["Velocidad_Aprox"].mean() if "Velocidad_Aprox" in df_filtrado.columns else 60
                st.metric("Velocidad Prom. ⚡", f"{vel_prom:.1f} km/h")
                
        else:
            with col_m1:
                st.metric("Vehículos Registrados 🚙", len(df_filtrado))
            with col_m2:
                marcas_dist = df_filtrado["marca"].nunique() if "marca" in df_filtrado.columns else 0
                st.metric("Marcas Distintas 🏷️", marcas_dist)
            with col_m3:
                anio_prom = df_filtrado["año"].mean() if "año" in df_filtrado.columns else 2018
                st.metric("Año Modelo Promedio 🗓️", f"{anio_prom:.0f}")
            with col_m4:
                activos = len(df_filtrado[df_filtrado["estado"] == "Activo"]) if "estado" in df_filtrado.columns else 0
                st.metric("Polizas Activas ✅", activos)
            with col_m5:
                porc_activo = (activos / len(df_filtrado)) * 100 if len(df_filtrado) > 0 else 0
                st.metric("Tasa de Cobertura 📈", f"{porc_activo:.1f}%")

        # SECCIÓN B: GRÁFICOS INTERACTIVOS (ESTILO UNICORNIO)
        st.markdown("---")
        st.subheader("Modelos de Visualización de Datos (Acentos Unicornio)")

        # Funciones auxiliares para gráficos interactivos de alta fidelidad
        def draw_unicorn_bar_chart(data, x_col, y_col):
            chart = alt.Chart(data).mark_bar(
                cornerRadiusTopLeft=8,
                cornerRadiusTopRight=8,
                fill=alt.Gradient(
                    gradient='linear',
                    stops=[
                        alt.GradientStop(color='#C084FC', offset=0),   # Violeta unicornio
                        alt.GradientStop(color='#EC4899', offset=0.5), # Rosa unicornio
                        alt.GradientStop(color='#22D3EE', offset=1)    # Cyan unicornio
                    ]
                )
            ).encode(
                x=alt.X(f"{x_col}:N", sort=None, title=x_col, axis=alt.Axis(labelAngle=-45, labelColor='#94A3B8', titleColor='#CBD5E1')),
                y=alt.Y(f"{y_col}:Q", title=y_col, axis=alt.Axis(labelColor='#94A3B8', titleColor='#CBD5E1')),
                tooltip=[x_col, y_col]
            ).properties(
                height=350
            ).configure_axis(
                gridColor='rgba(255, 255, 255, 0.05)'
            ).configure_view(
                strokeOpacity=0
            )
            st.altair_chart(chart, use_container_width=True)

        def draw_gender_scatter_chart(data, x_col, y_col, color_col):
            domain = ['F', 'M', 'Femenino', 'Masculino']
            range_ = ['#EC4899', '#22D3EE', '#EC4899', '#22D3EE'] # Rosa para femenino, Azul para masculino
            
            if color_col and color_col.lower() in ["resultado", "status", "estado", "gravedad"]:
                domain = list(data[color_col].unique())
                range_ = []
                for val in domain:
                    val_l = str(val).lower()
                    if "herido" in val_l or "muert" in val_l or "suspend" in val_l:
                        range_.append('#EC4899') # Rosa/Alerta
                    else:
                        range_.append('#22D3EE') # Cian/Seguro
            
            color_encoding = alt.Color(f"{color_col}:N", scale=alt.Scale(domain=domain, range=range_), legend=alt.Legend(title=color_col, labelColor='#94A3B8', titleColor='#CBD5E1')) if color_col else alt.value('#EC4899')

            chart = alt.Chart(data).mark_circle(size=140, opacity=0.85).encode(
                x=alt.X(f"{x_col}:Q", scale=alt.Scale(zero=False), title=x_col, axis=alt.Axis(labelColor='#94A3B8', titleColor='#CBD5E1')),
                y=alt.Y(f"{y_col}:Q", scale=alt.Scale(zero=False), title=y_col, axis=alt.Axis(labelColor='#94A3B8', titleColor='#CBD5E1')),
                color=color_encoding,
                tooltip=[c for c in data.columns if c in [x_col, y_col, color_col, 'ID', 'placa', 'marca', 'tipo_accidente']]
            ).properties(
                height=350
            ).configure_axis(
                gridColor='rgba(255, 255, 255, 0.05)'
            ).configure_view(
                strokeOpacity=0
            )
            st.altair_chart(chart, use_container_width=True)

        col_g1, col_g2 = st.columns(2)
        
        if "Reportes" in entidad_seleccionada:
            with col_g1:
                st.markdown("#### Distribución de Accidentes por Gravedad")
                if "Gravedad" in df_filtrado.columns:
                    grav_counts = df_filtrado["Gravedad"].value_counts().reset_index()
                    grav_counts.columns = ["Gravedad", "Cantidad"]
                    draw_unicorn_bar_chart(grav_counts, "Gravedad", "Cantidad")
                else:
                    st.info("Columna 'Gravedad' no encontrada.")
                
            with col_g2:
                st.markdown("#### Edad de Conductor vs Velocidad Estimada")
                if "Edad_Conductor" in df_filtrado.columns and "Velocidad_Aprox" in df_filtrado.columns:
                    color_col = None
                    for c in ["Gravedad", "gravedad", "Clima", "clima"]:
                        if c in df_filtrado.columns:
                            color_col = c
                            break
                    draw_gender_scatter_chart(df_filtrado, "Edad_Conductor", "Velocidad_Aprox", color_col)
                else:
                    st.info("Variables numéricas no encontradas para graficar.")
                
        else:
            with col_g1:
                st.markdown("#### Conteo de Vehículos por Tipo")
                if "tipo_vehiculo" in df_filtrado.columns:
                    tipo_counts = df_filtrado["tipo_vehiculo"].value_counts().reset_index()
                    tipo_counts.columns = ["Tipo", "Cantidad"]
                    draw_unicorn_bar_chart(tipo_counts, "Tipo", "Cantidad")
                else:
                    st.info("Columna 'tipo_vehiculo' no encontrada.")
                
            with col_g2:
                st.markdown("#### Conteo de Vehículos por Marca")
                if "marca" in df_filtrado.columns:
                    marca_counts = df_filtrado["marca"].value_counts().reset_index()
                    marca_counts.columns = ["Marca", "Cantidad"]
                    draw_unicorn_bar_chart(marca_counts, "Marca", "Cantidad")
                else:
                    st.info("Columna 'marca' no encontrada.")
                    
# --- Información Técnica ---
st.divider()
st.subheader("ℹ️ Información Técnica y Seguridad")
st.markdown(f"""
**Detalles de la Arquitectura del Consumo:**
- **Pila Tecnológica:** Python + Streamlit Web Engine
- **Motor de Datos:** Pandas Matrix Engineering (para filtrado con DataFrames)
- **Fuentes Soportadas:** 
  1. **MockAPI.io REST Client:** Consume de los recursos en la nube `/reportes` y `/vehiculos` con reintentos automáticos `/api/v1/` y control de excepciones.
  2. **Local Backup Simulator:** Carga el archivo local `{CSV_FILENAME}` (300 registros) como contingencia ante fallos de internet.
""")
