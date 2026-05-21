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
    page_title="Creciendo Juntos - Dashboard y API",
    page_icon="🎓",
    layout="wide"
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
    
    /* Estilo de Tarjetas de Métricas de Streamlit */
    div[data-testid="metric-container"] {
        background: rgba(11, 15, 25, 0.85) !important;
        border: 1px solid rgba(167, 139, 250, 0.25) !important;
        border-radius: 12px !important;
        padding: 15px 20px !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6) !important;
        backdrop-filter: blur(10px) !important;
        transition: all 0.3s ease !important;
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
    <svg width="54" height="54" viewBox="0 0 24 24" fill="none" stroke="#C084FC" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 10px #7C3AED); vertical-align: middle; margin-right: 15px;">
        <rect x="2" y="2" width="20" height="8" rx="2" ry="2"/>
        <rect x="2" y="14" width="20" height="8" rx="2" ry="2"/>
        <line x1="6" y1="6" x2="6.01" y2="6"/>
        <line x1="6" y1="18" x2="6.01" y2="18"/>
        <path d="M20 6h2v12h-2"/>
    </svg>
    <span class="tech-title">Dashboard & Consumo de API</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
### Panel de Analítica Institucional
Esta plataforma permite monitorear y analizar el desempeño académico en tiempo real. 
Consume información de manera flexible mediante conexiones en vivo a nuestra API Java o a través de nuestro simulador local de respaldo.
""")

# =====================================================================
# GENERADOR DINÁMICO DE DATOS (50 ESTUDIANTES, CURSOS Y PROFESORES)
# =====================================================================
random.seed(42)  # Mantiene los datos consistentes

nombres_m = ["Juan", "Carlos", "Luis", "Pedro", "Diego", "Andrés", "Mateo", "Santiago", "Sebastián", "Daniel", "Felipe", "Alejandro", "Nicolás", "David", "José", "Manuel"]
nombres_f = ["María", "Ana", "Sofía", "Laura", "Paula", "Camila", "Valeria", "Isabella", "Gabriela", "Mariana", "Valentina", "Daniela", "Sara", "Andrea", "Natalia", "Lucía"]
apellidos = ["Pérez", "Gómez", "Ruiz", "Martínez", "Hernández", "Díaz", "Álvarez", "Torres", "Ramos", "Castro", "Rodríguez", "López", "González", "Sánchez", "Ramírez", "Muñoz"]
ciudades = ["Bogotá", "Medellín", "Cali", "Barranquilla", "Bucaramanga", "Pereira", "Manizales", "Cartagena"]

cursos_nombres = [
    ("Programación Python", "PY101", "Ing. Carlos Pérez", 4),
    ("Bases de Datos", "BD102", "Dra. Martha Gómez", 3),
    ("Introducción a la IA", "IA103", "Msc. Juan Díaz", 4),
    ("Desarrollo Web", "DW104", "Ing. Luis Ruiz", 3),
    ("Ingeniería de Requisitos", "IR105", "Dra. Sandra Castro", 3),
    ("Arquitectura de Software", "AS106", "Ing. Andrés Torres", 4)
]

# 1. Generar Cursos
DATOS_CURSOS = []
for idx, (nombre, codigo, docente, creditos) in enumerate(cursos_nombres):
    DATOS_CURSOS.append({
        "ID": 101 + idx,
        "Nombre": nombre,
        "Código": codigo,
        "Docente": docente,
        "Créditos": creditos,
        "Alumnos_Inscritos": random.randint(15, 30)
    })

# 2. Generar Estudiantes, Calificaciones e Inscripciones Relacionadas
DATOS_ESTUDIANTES = []
DATOS_CALIFICACIONES = []
DATOS_INSCRIPCIONES = []

for i in range(1, 51):
    genero = random.choice(["M", "F"])
    nombre = random.choice(nombres_m if genero == "M" else nombres_f) + " " + random.choice(apellidos)
    edad = random.randint(17, 28)
    ciudad = random.choice(ciudades)
    promedio = round(random.uniform(1.8, 5.0), 2)
    
    if promedio < 3.0:
        estado = "En Riesgo"
    elif edad >= 24 and promedio >= 4.0:
        estado = "Egresado"
    else:
        estado = "Activo"
        
    DATOS_ESTUDIANTES.append({
        "ID": i,
        "Nombre": nombre,
        "Edad": edad,
        "Género": genero,
        "Ciudad": ciudad,
        "Promedio": promedio,
        "Estado": estado
    })
    
    # Asociar a un curso aleatorio
    curso = random.choice(DATOS_CURSOS)
    
    # Generar Calificación Relacionada
    nota_parcial = round(random.uniform(1.5, 5.0), 1)
    nota_final = round(min(5.0, max(0.0, nota_parcial + random.uniform(-0.6, 0.8))), 1)
    resultado = "Aprobado" if nota_final >= 3.0 else "Reprobado"
    
    DATOS_CALIFICACIONES.append({
        "ID": i,
        "Estudiante": nombre,
        "Curso": curso["Nombre"],
        "Docente": curso["Docente"],
        "Nota_Parcial": nota_parcial,
        "Nota_Final": nota_final,
        "Resultado": resultado
    })
    
    # Generar Inscripción Relacionada
    progreso = random.randint(30, 100)
    DATOS_INSCRIPCIONES.append({
        "ID": i,
        "Estudiante": nombre,
        "Curso": curso["Nombre"],
        "Fecha_Inscripcion": f"2026-02-{random.randint(1, 28):02d}",
        "Progreso_%": progreso
    })

# --- Sincronización del Simulador Local con los Datos de MockAPI ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def cargar_json_sincronizado(nombre_archivo, datos_originales):
    ruta_completa = os.path.join(BASE_DIR, nombre_archivo)
    if os.path.exists(ruta_completa):
        try:
            with open(ruta_completa, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return datos_originales
    return datos_originales

DATOS_ESTUDIANTES = cargar_json_sincronizado("datos_mockapi_50_estudiantes.json", DATOS_ESTUDIANTES)
DATOS_CURSOS = cargar_json_sincronizado("datos_mockapi_cursos.json", DATOS_CURSOS)
DATOS_CALIFICACIONES = cargar_json_sincronizado("datos_mockapi_calificaciones.json", DATOS_CALIFICACIONES)
DATOS_INSCRIPCIONES = cargar_json_sincronizado("datos_mockapi_inscripciones.json", DATOS_INSCRIPCIONES)

# =====================================================================
# INTERFAZ DE CONFIGURACIÓN (BARRA LATERAL / SIDEBAR)
# =====================================================================
with st.sidebar:
    st.markdown("### Origen de los Datos")
    
    origen_datos = st.radio(
        "Selecciona la fuente de datos:",
        options=[
            "Cloud REST API (MockAPI.io)",
            "Local Java REST API",
            "Cloud Database (Google Sheets)",
            "Local Backup Simulator"
        ],
        index=3, # Por defecto en Local Backup Simulator
        help="Elige de dónde se obtendrán los datos académicos en tiempo real."
    )
    
    # 1. Configuración de API Cloud REST (MockAPI.io)
    if origen_datos == "Cloud REST API (MockAPI.io)":
        st.divider()
        st.subheader("Conexión a MockAPI.io")
        mockapi_id = st.text_input(
            "ID de tu Proyecto MockAPI:",
            value="69f350d4bd2396bf530fbde8",
            help="Ingresa el identificador de tu proyecto en mockapi.io"
        )
        config_url = f"https://{mockapi_id}.mockapi.io"
        
    # 2. Configuración de API Java Real
    elif origen_datos == "Local Java REST API":
        st.divider()
        st.subheader("Servidor API Java")
        api_url_base = st.text_input(
            "URL del Servidor API:",
            value="http://localhost:8080",
            help="Dirección del backend Java (ej. http://localhost:8080)"
        )
        config_url = api_url_base
        
    # 3. Configuración de Base de Datos Cloud
    elif origen_datos == "Cloud Database (Google Sheets)":
        st.divider()
        st.subheader("Base de Datos en la Nube")
        sheet_url_base = st.text_input(
            "URL de Google Sheets en la Nube:",
            value="https://docs.google.com/spreadsheets/d/1b82s4wYd6tVp064tTz7lJ78vA1U4W7Y8h4rMhJ5Q2E0/edit?usp=sharing",
            help="Pega el enlace compartido de tu Google Sheets. La hoja debe tener pestañas llamadas: Estudiantes, Cursos, Calificaciones, Inscripciones."
        )
        config_url = sheet_url_base
        
    else:
        config_url = ""
        
    # Selección de Entidad
    st.divider()
    st.subheader("Selecciona la Entidad:")
    entidad_seleccionada = st.radio(
        "Elige una opción:",
        options=["Estudiantes", "Cursos", "Calificaciones", "Inscripciones"]
    )
    
    st.divider()
    # Botón para limpiar caché y recargar datos en tiempo real
    if st.button("Refrescar e Importar Datos", use_container_width=True, help="Limpia la memoria caché temporal de Streamlit y fuerza una nueva conexión con la API en la nube."):
        st.cache_data.clear()
        st.rerun()

# =====================================================================
# FUNCIÓN PARA OBTENER DATOS (API, CLOUD O SIMULADOR)
# =====================================================================
@st.cache_data
def obtener_datos(origen: str, config_url: str, entidad: str):
    nombre_entidad = entidad.lower()
    
    # 1. Modo Local Backup Simulator
    if origen == "Local Backup Simulator":
        if nombre_entidad == "estudiantes":
            return pd.DataFrame(DATOS_ESTUDIANTES), None
        elif nombre_entidad == "cursos":
            return pd.DataFrame(DATOS_CURSOS), None
        elif nombre_entidad == "calificaciones":
            return pd.DataFrame(DATOS_CALIFICACIONES), None
        elif nombre_entidad == "inscripciones":
            return pd.DataFrame(DATOS_INSCRIPCIONES), None
            
    # 2. Modo Cloud Database (Google Sheets)
    elif origen == "Cloud Database (Google Sheets)":
        try:
            sheet_url = config_url
            if "docs.google.com/spreadsheets" in sheet_url:
                if "/d/" in sheet_url:
                    id_completo = sheet_url.split("/d/")[1]
                    spreadsheet_id = id_completo.split("/")[0]
                    sheet_url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/gviz/tq?tqx=out:csv&sheet={entidad}"
                else:
                    if "/edit" in sheet_url:
                        sheet_url = sheet_url.split("/edit")[0] + f"/export?format=csv&sheet={entidad}"
                    elif "?" in sheet_url:
                        sheet_url = sheet_url.split("?")[0] + f"/export?format=csv&sheet={entidad}"
                    else:
                        sheet_url = sheet_url.rstrip("/") + f"/export?format=csv&sheet={entidad}"
            
            df_cloud = pd.read_csv(sheet_url)
            return df_cloud, None
        except Exception as e:
            return None, f"Error al conectar con la Base de Datos Cloud en Google Sheets: {str(e)}. Verifica que el archivo de Google Sheets tenga una pestaña llamada '{entidad}' y esté compartido de forma pública."
            
    # 3. Modo Cloud REST API (MockAPI.io)
    elif origen == "Cloud REST API (MockAPI.io)":
        url_completa = f"{config_url}/{nombre_entidad}"
        try:
            respuesta = requests.get(url_completa, timeout=5)
            if respuesta.status_code == 200:
                return pd.DataFrame(respuesta.json()), None
            elif respuesta.status_code == 404:
                return None, f"Error 404: El endpoint '{nombre_entidad}' no existe en tu MockAPI."
            else:
                return None, f"Error del servidor HTTP {respuesta.status_code}"
        except requests.exceptions.ConnectionError:
            return None, "No se pudo conectar a los servidores de MockAPI. Revisa tu conexión a internet."
        except Exception as e:
            return None, f"Error inesperado al conectar con MockAPI: {str(e)}"
            
    # 4. Conexión Real a API Java (Local)
    else:
        url_completa = f"{config_url}/api/{nombre_entidad}"
        try:
            respuesta = requests.get(url_completa, timeout=5)
            if respuesta.status_code == 200:
                return pd.DataFrame(respuesta.json()), None
            else:
                return None, f"Error del servidor HTTP {respuesta.status_code}"
        except requests.exceptions.ConnectionError:
            return None, "No se pudo conectar al servidor. ¿El backend de Java está encendido localmente?"
        except Exception as e:
            return None, f"Error inesperado: {str(e)}"

# Carga de datos
with st.spinner(f"Cargando datos de {entidad_seleccionada}..."):
    df_datos, error_conexion = obtener_datos(origen_datos, config_url, entidad_seleccionada)

# Control de errores
if error_conexion is not None:
    st.error("Error al Obtener Datos")
    st.warning(f"**Detalle del error:** {error_conexion}")
    st.info("""
    **Sugerencia de contingencia:** 
    Si estás intentando conectarte a la API Java local o a MockAPI y no responden, o si la hoja de Google Sheets no está accesible, puedes seleccionar **'Local Backup Simulator'** en la barra lateral izquierda para explorar y evaluar el sistema sin interrupciones de red.
    """)
    st.stop()

# --- Normalización y Limpieza de Datos (Robustez para MockAPI) ---
if df_datos is not None and not df_datos.empty:
    df_datos = df_datos.drop_duplicates()
    df_datos.columns = [col.strip() for col in df_datos.columns]
    
    rename_dict = {}
    for col in df_datos.columns:
        col_lower = col.lower()
        if col_lower in ["genero", "género", "gender"]:
            rename_dict[col] = "Género"
        elif col_lower in ["ciudad", "city"]:
            rename_dict[col] = "Ciudad"
        elif col_lower in ["estado", "status"]:
            rename_dict[col] = "Estado"
        elif col_lower in ["edad", "age"]:
            rename_dict[col] = "Edad"
        elif col_lower in ["promedio", "average", "gpa"]:
            rename_dict[col] = "Promedio"
        elif col_lower in ["codigo", "código", "code"]:
            rename_dict[col] = "Código"
        elif col_lower in ["creditos", "créditos", "credits"]:
            rename_dict[col] = "Créditos"
        elif col_lower in ["progreso_%", "progreso", "progreso_porcentaje", "progress"]:
            rename_dict[col] = "Progreso_%"
        elif col_lower in ["asistencia", "asistencia_%", "asistencia_porcentaje", "attendance"]:
            rename_dict[col] = "Asistencia_%"
        elif col_lower in ["materias_inscritas", "materias", "cursos_inscritos", "courses"]:
            rename_dict[col] = "Materias_Inscritas"
        elif col_lower in ["creditos_aprobados", "creditos_aprob"]:
            rename_dict[col] = "Creditos_Aprobados"
        elif col_lower in ["estrato", "stratum"]:
            rename_dict[col] = "Estrato"
            
    if rename_dict:
        df_datos = df_datos.rename(columns=rename_dict)
        
    if "Edad" in df_datos.columns:
        df_datos["Edad"] = pd.to_numeric(df_datos["Edad"], errors="coerce").fillna(20).astype(int)
        
    if "Promedio" in df_datos.columns:
        df_datos["Promedio"] = pd.to_numeric(df_datos["Promedio"], errors="coerce").fillna(3.0)
        if df_datos["Promedio"].max() > 5.0:
            df_datos["Promedio"] = (df_datos["Promedio"] / 100 * 5.0).round(2)
            
    if "Estrato" in df_datos.columns:
        df_datos["Estrato"] = pd.to_numeric(df_datos["Estrato"], errors="coerce").fillna(1).astype(int)
        
    if "Materias_Inscritas" in df_datos.columns:
        df_datos["Materias_Inscritas"] = pd.to_numeric(df_datos["Materias_Inscritas"], errors="coerce").fillna(5).astype(int)
        if df_datos["Materias_Inscritas"].max() > 10:
            df_datos["Materias_Inscritas"] = df_datos["Materias_Inscritas"].apply(lambda x: (x % 6) + 3)

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
    if entidad_seleccionada == "Estudiantes":
        ciudades_disponibles = ["Todas"] + list(df_datos["Ciudad"].unique())
        ciudad_elegida = st.selectbox("Filtrar estudiantes por Ciudad:", ciudades_disponibles)
        if ciudad_elegida != "Todas":
            df_filtrado = df_datos[df_datos["Ciudad"] == ciudad_elegida]
            
    elif entidad_seleccionada == "Calificaciones":
        cursos_disponibles = ["Todos"] + list(df_datos["Curso"].unique())
        curso_elegido = st.selectbox("Filtrar calificaciones por Curso:", cursos_disponibles)
        if curso_elegido != "Todos":
            df_filtrado = df_datos[df_datos["Curso"] == curso_elegido]
            
    elif entidad_seleccionada == "Inscripciones":
        cursos_disponibles = ["Todos"] + list(df_datos["Curso"].unique())
        curso_elegido = st.selectbox("Filtrar inscripciones por Curso:", cursos_disponibles)
        if curso_elegido != "Todos":
            df_filtrado = df_datos[df_datos["Curso"] == curso_elegido]
            
    elif entidad_seleccionada == "Cursos":
        st.info("Mostrando catálogo de asignaturas institucional. Sin filtros aplicados.")

with col_filtro2:
    if entidad_seleccionada == "Estudiantes":
        estados_disponibles = ["Todos"] + list(df_datos["Estado"].unique())
        estado_elegido = st.selectbox("Filtrar por Estado Académico:", estados_disponibles)
        if estado_elegido != "Todos":
            df_filtrado = df_filtrado[df_filtrado["Estado"] == estado_elegido]
            
    elif entidad_seleccionada == "Calificaciones":
        resultados_disponibles = ["Todos"] + list(df_datos["Resultado"].unique())
        resultado_elegido = st.selectbox("Filtrar por Resultado final:", resultados_disponibles)
        if resultado_elegido != "Todos":
            df_filtrado = df_filtrado[df_filtrado["Resultado"] == resultado_elegido]
            
    elif entidad_seleccionada == "Inscripciones":
        progreso_minimo = st.slider("Avance Mínimo del Estudiante (%):", min_value=0, max_value=100, value=0)
        df_filtrado = df_filtrado[df_filtrado["Progreso_%"] >= progreso_minimo]

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
            El profesor puede evaluar cómo seleccionamos porciones del DataFrame según su posición numérica exacta usando <code>.iloc</code>.
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
        label=f"Exportar listado completo ({entidad_seleccionada}) como CSV",
        data=csv_data,
        file_name=f"{entidad_seleccionada.lower()}_creciendo_juntos.csv",
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
        col_m1, col_m2, col_m3, col_m4 = st.columns(4)
        
        if entidad_seleccionada == "Estudiantes":
            with col_m1:
                st.metric("Total Estudiantes", len(df_filtrado))
            with col_m2:
                st.metric("Edad Promedio", f"{df_filtrado['Edad'].mean():.1f} años")
            with col_m3:
                st.metric("Promedio Académico", f"{df_filtrado['Promedio'].mean():.2f} / 5.0")
            with col_m4:
                en_riesgo = len(df_filtrado[df_filtrado["Estado"] == "En Riesgo"])
                st.metric("Alumnos en Alerta", en_riesgo)
                
        elif entidad_seleccionada == "Cursos":
            with col_m1:
                st.metric("Asignaturas Ofertadas", len(df_filtrado))
            with col_m2:
                st.metric("Cuerpo Docente Activo", df_filtrado["Docente"].nunique())
            with col_m3:
                st.metric("Total Créditos Académicos", df_filtrado["Créditos"].sum())
            with col_m4:
                curso_max = df_filtrado.loc[df_filtrado["Alumnos_Inscritos"].idxmax()]["Nombre"]
                st.metric("Curso con Mayor Matrícula", curso_max)
                
        elif entidad_seleccionada == "Calificaciones":
            with col_m1:
                st.metric("Exámenes Registrados", len(df_filtrado))
            with col_m2:
                st.metric("Nota Definitiva Promedio", f"{df_filtrado['Nota_Final'].mean():.2f}")
            with col_m3:
                st.metric("Calificación Máxima", f"{df_filtrado['Nota_Final'].max():.1f}")
            with col_m4:
                total_aprobados = len(df_filtrado[df_filtrado["Resultado"] == "Aprobado"])
                st.metric("Tasa de Aprobación", f"{(total_aprobados / len(df_filtrado)) * 100:.1f}%")
                
        elif entidad_seleccionada == "Inscripciones":
            with col_m1:
                st.metric("Matrículas de Cursos", len(df_filtrado))
            with col_m2:
                st.metric("Progreso Promedio General", f"{df_filtrado['Progreso_%'].mean():.1f}%")
            with col_m3:
                st.metric("Módulos Completados (100%)", len(df_filtrado[df_filtrado["Progreso_%"] == 100]))
            with col_m4:
                st.metric("Avance Mínimo Registrado", f"{df_filtrado['Progreso_%'].min()}%")

        # SECCIÓN B: GRÁFICOS INTERACTIVOS
        st.markdown("---")
        st.subheader("Modelos de Visualización de Datos")

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
            
            if color_col and color_col.lower() in ["resultado", "status", "estado"]:
                domain = list(data[color_col].unique())
                range_ = []
                for val in domain:
                    val_l = str(val).lower()
                    if "aprob" in val_l or "activ" in val_l or "egres" in val_l:
                        range_.append('#22D3EE') # cyan/azul
                    else:
                        range_.append('#EC4899') # rosado/pink
            
            color_encoding = alt.Color(f"{color_col}:N", scale=alt.Scale(domain=domain, range=range_), legend=alt.Legend(title=color_col, labelColor='#94A3B8', titleColor='#CBD5E1')) if color_col else alt.value('#EC4899')

            chart = alt.Chart(data).mark_circle(size=140, opacity=0.85).encode(
                x=alt.X(f"{x_col}:Q", scale=alt.Scale(zero=False), title=x_col, axis=alt.Axis(labelColor='#94A3B8', titleColor='#CBD5E1')),
                y=alt.Y(f"{y_col}:Q", scale=alt.Scale(zero=False), title=y_col, axis=alt.Axis(labelColor='#94A3B8', titleColor='#CBD5E1')),
                color=color_encoding,
                tooltip=[c for c in data.columns if c in [x_col, y_col, color_col, 'Nombre', 'Estudiante', 'Curso']]
            ).properties(
                height=350
            ).configure_axis(
                gridColor='rgba(255, 255, 255, 0.05)'
            ).configure_view(
                strokeOpacity=0
            )
            st.altair_chart(chart, use_container_width=True)

        col_g1, col_g2 = st.columns(2)
        
        if entidad_seleccionada == "Estudiantes":
            with col_g1:
                st.markdown("#### Cantidad de Estudiantes por Estado Académico")
                if "Estado" in df_filtrado.columns:
                    estado_counts = df_filtrado["Estado"].value_counts().reset_index()
                    estado_counts.columns = ["Estado", "Cantidad"]
                    draw_unicorn_bar_chart(estado_counts, "Estado", "Cantidad")
                else:
                    st.info("Columna 'Estado' no encontrada.")
                
            with col_g2:
                st.markdown("#### Relación de Edad vs Promedio Académico")
                if "Edad" in df_filtrado.columns and "Promedio" in df_filtrado.columns:
                    color_col = None
                    for c in ["Género", "Genero", "genero"]:
                        if c in df_filtrado.columns:
                            color_col = c
                            break
                    draw_gender_scatter_chart(df_filtrado, "Edad", "Promedio", color_col)
                else:
                    st.info("Columnas 'Edad' o 'Promedio' no encontradas para graficar.")
                
        elif entidad_seleccionada == "Cursos":
            with col_g1:
                st.markdown("#### Estudiantes Matriculados por Curso")
                if "Nombre" in df_filtrado.columns and "Alumnos_Inscritos" in df_filtrado.columns:
                    draw_unicorn_bar_chart(df_filtrado, "Nombre", "Alumnos_Inscritos")
                else:
                    st.info("Columnas necesarias no encontradas.")
                
            with col_g2:
                st.markdown("#### Distribución de Créditos por Asignatura")
                if "Nombre" in df_filtrado.columns and "Créditos" in df_filtrado.columns:
                    draw_unicorn_bar_chart(df_filtrado, "Nombre", "Créditos")
                else:
                    st.info("Columnas necesarias no encontradas.")
                
        elif entidad_seleccionada == "Calificaciones":
            with col_g1:
                st.markdown("#### Rendimiento por Curso (Nota Final Promedio)")
                if "Curso" in df_filtrado.columns and "Nota_Final" in df_filtrado.columns:
                    calif_por_curso = df_filtrado.groupby("Curso")["Nota_Final"].mean().reset_index()
                    draw_unicorn_bar_chart(calif_por_curso, "Curso", "Nota_Final")
                else:
                    st.info("Columnas necesarias no encontradas.")
                
            with col_g2:
                st.markdown("#### Correlación entre Nota Parcial y Nota Final")
                if "Nota_Parcial" in df_filtrado.columns and "Nota_Final" in df_filtrado.columns:
                    color_col = None
                    for c in ["Resultado", "resultado"]:
                        if c in df_filtrado.columns:
                            color_col = c
                            break
                    draw_gender_scatter_chart(df_filtrado, "Nota_Parcial", "Nota_Final", color_col)
                else:
                    st.info("Columnas necesarias no encontradas.")
                
        elif entidad_seleccionada == "Inscripciones":
            with col_g1:
                st.markdown("#### Avance Académico Individual (%)")
                if "Estudiante" in df_filtrado.columns and "Progreso_%" in df_filtrado.columns:
                    draw_unicorn_bar_chart(df_filtrado, "Estudiante", "Progreso_%")
                else:
                    st.info("Columnas necesarias no encontradas.")
                
            with col_g2:
                st.markdown("#### Distribución de Alumnos por Materias Inscritas")
                if "Curso" in df_filtrado.columns:
                    curso_counts = df_filtrado["Curso"].value_counts().reset_index()
                    curso_counts.columns = ["Curso", "Cantidad"]
                    draw_unicorn_bar_chart(curso_counts, "Curso", "Cantidad")
                else:
                    st.info("Columna 'Curso' no encontrada.")
