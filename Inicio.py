import streamlit as st
from config import PROJECT_INFO, API_CONFIG

# Configuración de la página
st.set_page_config(
    page_title="Creciendo Juntos - Plataforma Educativa",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Estilo Personalizado Premium (Mesh Gradient Cyber-Dark & Glassmorphism) ---
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
        font-size: 3.2rem;
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
    
    .stSubheader {
        font-family: 'Outfit', sans-serif !important;
        color: #CBD5E1 !important;
        font-weight: 300;
        margin-bottom: 2rem;
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
        transform: translateY(-5px) !important;
        border: 1px solid rgba(34, 211, 238, 0.55) !important;
        box-shadow: 0 0 30px rgba(34, 211, 238, 0.25) !important;
        background: rgba(15, 23, 42, 0.95) !important;
    }
    
    /* Badges de rol para integrantes */
    .role-badge {
        display: inline-block;
        font-size: 0.72rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        padding: 4px 10px;
        border-radius: 20px;
        margin-bottom: 12px;
        font-family: 'Space Grotesk', sans-serif;
    }
    .member-name {
        font-family: 'Space Grotesk', sans-serif;
        color: #F8FAFC !important;
        font-size: 1.3rem;
        font-weight: 600;
        margin: 0;
    }
    
    /* Características e Iconos */
    .feat-title {
        font-family: 'Space Grotesk', sans-serif;
        color: #F8FAFC !important;
        font-size: 1.35rem;
        font-weight: 600;
        margin-top: 12px;
        margin-bottom: 8px;
    }
    .feat-desc {
        font-family: 'Outfit', sans-serif;
        color: #94A3B8;
        font-size: 0.92rem;
        line-height: 1.5;
        margin: 0;
    }
    
    /* Tarjetas de tecnología */
    .tech-card-title {
        font-family: 'Space Grotesk', sans-serif;
        color: #F8FAFC !important;
        font-size: 1.2rem;
        font-weight: 600;
        margin-top: 6px;
        margin-bottom: 4px;
    }
    .tech-card-desc {
        font-family: 'Outfit', sans-serif;
        color: #64748B;
        font-size: 0.85rem;
        margin: 0;
    }
    
    /* Alertas de Streamlit y Controles */
    .stAlert {
        border-radius: 12px;
        background: rgba(10, 15, 30, 0.85) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(124, 58, 237, 0.25) !important;
    }
    
    .stAlert div {
        color: #CBD5E1 !important;
    }
    
    /* Modificar el color de los divisores */
    hr {
        border-color: rgba(124, 58, 237, 0.15) !important;
    }
    
    /* Texto plano */
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

# --- Título Principal con Logo SVG ---
st.markdown("""
<div class="tech-title-container">
    <svg width="54" height="54" viewBox="0 0 24 24" fill="none" stroke="#C084FC" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 10px #7C3AED); vertical-align: middle; margin-right: 15px;">
        <path d="M22 10v6M2 10l10-5 10 5-10 5z"/>
        <path d="M6 12v5c0 2 2 3 6 3s6-1 6-3v-5"/>
    </svg>
    <span class="tech-title">Creciendo Juntos</span>
</div>
""", unsafe_allow_html=True)
st.subheader("Transformando la Educación a través de Analítica de Datos")

st.divider()

# --- 1. Introducción ---
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <h2 class="tech-header">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#A78BFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 6px #7C3AED); vertical-align: middle; margin-right: 12px;">
            <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/>
            <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>
        </svg>Introducción
    </h2>
    """, unsafe_allow_html=True)
    st.write("""
    **Creciendo Juntos** es una plataforma educativa que integra analítica de datos para mejorar continuamente la experiencia de aprendizaje. 
    A través de este tablero interactivo, exploraremos cómo la ciencia de datos puede revelar patrones en el desempeño estudiantil, 
    identificar oportunidades de mejora y personalizar estrategias educativas.
    
    Nuestro enfoque se centra en la **Exploración de Datos (EDA)**, análisis de inscripciones, calificaciones y progreso académico 
    para generar conocimiento de negocio accionable que optimice los procesos educativos de forma directa.
    """)

with col2:
    st.info("⚡ **Dato Analítico:** Las instituciones que integran modelos avanzados de analítica de datos mejoran de media el rendimiento y retención estudiantil entre un 15% y un 20%.")

# --- 2. Objetivos ---
st.markdown("""
<h2 class="tech-header">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#F43F5E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 6px #F43F5E); vertical-align: middle; margin-right: 12px;">
        <circle cx="12" cy="12" r="10"/>
        <circle cx="12" cy="12" r="6"/>
        <circle cx="12" cy="12" r="2"/>
    </svg>Objetivos de Creciendo Juntos
</h2>
""", unsafe_allow_html=True)

obj_gen, obj_esp = st.columns(2)

with obj_gen:
    st.subheader("Objetivo General")
    st.markdown("""
    - Crear un sistema integral de analítica educativa que permita visualizar, analizar y mejorar continuamente los procesos de enseñanza-aprendizaje a través de datos.
    """)

with obj_esp:
    st.subheader("Objetivos Específicos")
    st.markdown("""
    - Integrar datos reales y fluidos desde nuestra API Java para monitorear estudiantes, cursos y desempeño.
    - Identificar patrones clave en el rendimiento académico y deserción estudiantil de forma preventiva.
    - Personalizar las recomendaciones educativas basadas en la analítica de comportamiento.
    - Generar reportes analíticos consolidados de alta fidelidad para la toma de decisiones directivas.
    """)

st.divider()

# --- 3. Equipo de Trabajo ---
st.markdown("""
<h2 class="tech-header">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#06B6D4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 6px #06B6D4); vertical-align: middle; margin-right: 12px;">
        <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
        <circle cx="9" cy="7" r="4"/>
        <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
        <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
    </svg>Equipo de Trabajo
</h2>
""", unsafe_allow_html=True)

integrantes = [
    {"nombre": "Daniel Martinez", "rol": "Líder de Proyecto", "color": "#A78BFA"},
    {"nombre": "Brandon Ciro", "rol": "Desarrollo Backend (Java)", "color": "#F59E0B"},
    {"nombre": "Carolina Martinez", "rol": "Analítica de Datos", "color": "#06B6D4"},
    {"nombre": "Britany Montoya", "rol": "Analítica de Datos", "color": "#06B6D4"},
]

cols = st.columns(len(integrantes))

for i, persona in enumerate(integrantes):
    with cols[i]:
        st.markdown(f"""
        <div style="text-align: center; padding: 5px 0;">
            <div class="role-badge" style="background-color: {persona['color']}18; color: {persona['color']}; border: 1px solid {persona['color']}50;">
                {persona['rol']}
            </div>
            <h4 class="member-name">{persona['nombre']}</h4>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# --- 4. Características del Proyecto ---
st.markdown("""
<h2 class="tech-header">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#EC4899" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 6px #EC4899); vertical-align: middle; margin-right: 12px;">
        <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
    </svg>Características Principales
</h2>
""", unsafe_allow_html=True)

feat_col1, feat_col2, feat_col3 = st.columns(3)

with feat_col1:
    st.markdown("""
    <div style="min-height: 220px;">
        <svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#A78BFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 5px #7C3AED); margin-bottom: 12px;">
            <circle cx="11" cy="11" r="8"/>
            <line x1="21" y1="21" x2="16.65" y2="16.65"/>
            <line x1="8" y1="11" x2="14" y2="11"/>
            <line x1="11" y1="8" x2="11" y2="14"/>
        </svg>
        <h3 class="feat-title">Análisis Exploratorio (EDA)</h3>
        <p class="feat-desc">Herramienta interactiva para explorar datos educativos con estadísticas descriptivas detalladas, análisis de calidad y detección de vacíos.</p>
    </div>
    """, unsafe_allow_html=True)

with feat_col2:
    st.markdown("""
    <div style="min-height: 220px;">
        <svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#06B6D4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 5px #06B6D4); margin-bottom: 12px;">
            <rect x="2" y="2" width="20" height="8" rx="2" ry="2"/>
            <rect x="2" y="14" width="20" height="8" rx="2" ry="2"/>
            <line x1="6" y1="6" x2="6.01" y2="6"/>
            <line x1="6" y1="18" x2="6.01" y2="18"/>
        </svg>
        <h3 class="feat-title">Integración API y Simulador</h3>
        <p class="feat-desc">Conexión flexible en tiempo real con una API Java real, o con un simulador local de contingencia de alta disponibilidad.</p>
    </div>
    """, unsafe_allow_html=True)

with feat_col3:
    st.markdown("""
    <div style="min-height: 220px;">
        <svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#EC4899" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 5px #EC4899); margin-bottom: 12px;">
            <line x1="18" y1="20" x2="18" y2="10"/>
            <line x1="12" y1="20" x2="12" y2="4"/>
            <line x1="6" y1="20" x2="6" y2="14"/>
        </svg>
        <h3 class="feat-title">Dashboard y Gráficos</h3>
        <p class="feat-desc">Visualizaciones dinámicas e interactivas de promedios, tasas de deserción, popularidad de cursos y avance estudiantil en tiempo real.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 5. Tecnologías Utilizadas ---
st.markdown("""
<h2 class="tech-header">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#F59E0B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 6px #F59E0B); vertical-align: middle; margin-right: 12px;">
        <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>
    </svg>Tecnologías Utilizadas
</h2>
""", unsafe_allow_html=True)

tech_col1, tech_col2, tech_col3, tech_col4 = st.columns(4)

with tech_col1:
    st.markdown("""
    <div style="min-height: 120px;">
        <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#3B82F6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 5px #3B82F6); margin-bottom: 8px;">
            <path d="M12 2v20"/>
            <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>
        </svg>
        <h4 class="tech-card-title">Python</h4>
        <p class="tech-card-desc">Procesamiento de datos y modelado descriptivo.</p>
    </div>
    """, unsafe_allow_html=True)

with tech_col2:
    st.markdown("""
    <div style="min-height: 120px;">
        <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#EF4444" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 5px #EF4444); margin-bottom: 8px;">
            <polygon points="12 2 22 8.5 22 15.5 12 22 2 15.5 2 8.5 12 2"/>
        </svg>
        <h4 class="tech-card-title">Streamlit</h4>
        <p class="tech-card-desc">Construcción de la interfaz y renderizado web.</p>
    </div>
    """, unsafe_allow_html=True)

with tech_col3:
    st.markdown("""
    <div style="min-height: 120px;">
        <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#F59E0B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 5px #F59E0B); margin-bottom: 8px;">
            <path d="M18 8h1a4 4 0 0 1 0 8h-1"/>
            <path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/>
            <line x1="6" y1="1" x2="6" y2="4"/>
            <line x1="10" y1="1" x2="10" y2="4"/>
            <line x1="14" y1="1" x2="14" y2="4"/>
        </svg>
        <h4 class="tech-card-title">Java REST API</h4>
        <p class="tech-card-desc">Backend robusto y almacenamiento de persistencia.</p>
    </div>
    """, unsafe_allow_html=True)

with tech_col4:
    st.markdown("""
    <div style="min-height: 120px;">
        <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 5px #10B981); margin-bottom: 8px;">
            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
            <line x1="9" y1="3" x2="9" y2="21"/>
            <line x1="15" y1="3" x2="15" y2="21"/>
            <line x1="3" y1="9" x2="21" y2="9"/>
            <line x1="3" y1="15" x2="21" y2="15"/>
        </svg>
        <h4 class="tech-card-title">Pandas Engine</h4>
        <p class="tech-card-desc">Manipulación de matrices e ingeniería de variables.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 6. Navegación ---
st.markdown("""
<h2 class="tech-header">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 5px #10B981); vertical-align: middle; margin-right: 12px;">
        <polygon points="3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21"/>
        <line x1="9" y1="3" x2="9" y2="18"/>
        <line x1="15" y1="6" x2="15" y2="21"/>
    </svg>Guía de Navegación
</h2>
""", unsafe_allow_html=True)

nav_col1, nav_col2 = st.columns(2)

with nav_col1:
    st.markdown("""
    #### 📋 Módulos del Sistema:
    1. **Análisis Exploratorio de Datos (EDA)**
       - Conexión e importación desde archivos locales o Google Sheets.
       - Evaluación analítica de tipos, pesos de memoria y estructura.
       - Diagnóstico automatizado de integridad de nulos y vacíos.
    """)

with nav_col2:
    st.markdown("""
    2. **Consumo de API y Dashboard**
       - Conexión REST en vivo a MockAPI o Servidor Java Local.
       - Sincronización transparente con Google Sheets Cloud.
       - Panel interactivo de KPI, gráficos de barras y diagramas de correlación.
    
    3. **Resultados del Análisis**
       - Formulario integrado con conclusiones pre-cargadas.
       - Generador instantáneo y descarga del reporte final.
    """)

st.divider()

# --- Pie de página ---
st.sidebar.info("Navegación: Utiliza el menú lateral para explorar los diferentes módulos del sistema.")
st.sidebar.markdown("---")
st.sidebar.write("© 2026 - Creciendo Juntos | Plataforma Educativa")
