import streamlit as st
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="Resultados - Creciendo Juntos",
    page_icon="📝",
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
    
    .stSubheader {
        font-family: 'Outfit', sans-serif !important;
        color: #E2E8F0 !important;
        font-weight: 400;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
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
    
    /* Formularios */
    div[data-testid="stForm"] {
        background: rgba(11, 15, 25, 0.85) !important;
        border: 1px solid rgba(167, 139, 250, 0.25) !important;
        border-radius: 16px !important;
        padding: 30px !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7) !important;
        backdrop-filter: blur(10px);
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
    <svg width="54" height="54" viewBox="0 0 24 24" fill="none" stroke="#F472B6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 10px #F472B6); vertical-align: middle; margin-right: 15px;">
        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
        <polyline points="14 2 14 8 20 8"/>
        <line x1="16" y1="13" x2="8" y2="13"/>
        <line x1="16" y1="17" x2="8" y2="17"/>
        <polyline points="10 9 9 9 8 9"/>
    </svg>
    <span class="tech-title">Resultados del Análisis</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
Este módulo permite consolidar y documentar formalmente las observaciones y hallazgos clave identificados durante el **Análisis Exploratorio de Datos (EDA)**.
Al diligenciar las secciones del formulario, podrá generar y descargar un reporte estructurado en formato Markdown.
""")

st.divider()

# --- Formulario de Resultados ---
st.markdown("""
<h2 class="tech-header">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#A78BFA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 6px #A78BFA); vertical-align: middle; margin-right: 12px;">
        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
        <polyline points="14 2 14 8 20 8"/>
    </svg>Formulario de Reporte Académico
</h2>
""", unsafe_allow_html=True)

with st.form("form_resultados"):
    st.subheader("1. Identificación y Contexto")
    contexto = st.text_area(
        "¿De qué se trata el dataset? ¿Cuál es su origen y propósito?",
        value="El dataset de 'Creciendo Juntos' está compuesto por 50 registros académicos del periodo 2026. Su propósito es auditar e identificar el comportamiento académico, la tasa de aprobación y la deserción en asignaturas clave como Programación Python, Bases de Datos, Introducción a la IA, Desarrollo Web, Ingeniería de Requisitos y Arquitectura de Software. Permite correlacionar variables demográficas (edad, género, ciudad de origen) con el promedio acumulado y el progreso en las asignaturas.",
        placeholder="Ej: El dataset contiene información de 150 estudiantes inscritos en programas educativos...",
        height=120
    )

    st.subheader("2. Calidad de los Datos")
    calidad = st.text_area(
        "¿Qué encontraste sobre datos faltantes y limpieza?",
        value="La auditoría de calidad de datos revela una integridad y completitud del 100%. No se detectaron valores nulos o vacíos en las columnas clave como ID, Nombre, Edad, Género, Ciudad, Promedio y Estado. Los tipos de datos fueron normalizados correctamente (Edad como entero, Promedio como flotante en escala colombiana de 0.0 a 5.0, y variables categóricas limpias de espacios en blanco). Los nombres de los estudiantes se corresponden exactamente en las tablas transaccionales de Calificaciones e Inscripciones, asegurando una consistencia referencial y relacional perfecta.",
        placeholder="Ej: El dataset está 95% completo. Se observaron valores nulos...",
        height=120
    )

    st.subheader("3. Hallazgos Estadísticos Clave")
    estadisticas = st.text_area(
        "¿Cuáles son los números y categorías más relevantes?",
        value="El promedio académico general de los estudiantes es de 3.82 sobre 5.0. La edad promedio de la cohorte es de 22.4 años, con un rango entre 17 y 28 años. El 68% de la población estudiantil se encuentra en estado 'Activo', el 18% como 'Egresado' y un 14% en estado 'En Riesgo' debido a promedios acumulados inferiores a 3.0. La asignatura con mayor número de matrículas y mejor rendimiento promedio es 'Programación Python', mientras que 'Bases de Datos' registra la tasa de aprobación más ajustada (promedio de 3.2). La correlación muestra que a mayor edad se observa una ligera tendencia de mejora en el promedio acumulado.",
        placeholder="Ej: El promedio de calificación es 3.8/5.0. El 70% de estudiantes están activos...",
        height=120
    )

    st.subheader("4. Conclusión Final y Recomendaciones")
    conclusion = st.text_area(
        "¿Cuál es el mensaje principal de los datos y qué se puede mejorar?",
        value="Los datos demuestran una alta retención y un desempeño académico sobresaliente en la mayoría de los cursos de tecnología del programa. Sin embargo, se recomienda implementar tutorías y acompañamiento académico focalizado para el 14% de estudiantes catalogados 'En Riesgo', principalmente en las áreas complejas de Bases de Datos y Arquitectura de Software. Se aconseja utilizar el módulo de alertas tempranas del dashboard en vivo para automatizar la detección de promedios inferiores a 3.0 antes de los exámenes finales, mejorando así la tasa de éxito institucional general.",
        placeholder="Ej: Los datos indican que hay un 85% de retención estudiantil...",
        height=120
    )
    
    # Botón de envío
    enviado = st.form_submit_button("Generar Reporte Analítico", use_container_width=True)

# --- Generación de Reporte ---
if enviado:
    if contexto and calidad and estadisticas and conclusion:
        st.divider()
        st.success("Reporte consolidado generado exitosamente.")
        
        fecha_reporte = datetime.now().strftime("%d/%m/%Y %H:%M")
        
        reporte_md = f"""# Reporte de Análisis Exploratorio de Datos (EDA)
## Proyecto: Creciendo Juntos - Plataforma Educativa

**Fecha de Generación:** {fecha_reporte}

---

## 1️⃣ Identificación y Contexto

{contexto}

---

## 2️⃣ Calidad de los Datos

{calidad}

---

## 3️⃣ Hallazgos Estadísticos Clave

{estadisticas}

---

## 4️⃣ Conclusión Final y Recomendaciones

{conclusion}

---

**Generado por:** Creciendo Juntos - Plataforma de Analítica Educativa
"""
        
        # Mostrar reporte
        st.markdown(reporte_md)
        
        # Descargar reporte
        st.download_button(
            label="Descargar Reporte (Markdown)",
            data=reporte_md,
            file_name=f"reporte_eda_creciendo_juntos_{fecha_reporte.replace('/', '-').replace(':', '')}.md",
            mime="text/markdown"
        )
    else:
        st.error("Por favor completa todas las secciones antes de generar el reporte.")


# --- Barra Lateral ---
with st.sidebar:
    st.markdown("---")
    st.subheader("Recomendaciones de Análisis")
    st.markdown("""
    - Sé específico con números y porcentajes
    - Relaciona hallazgos entre secciones
    - Interpreta más allá de la estadística simple
    - Proporciona el valor de negocio de los datos
    """)
    
    st.markdown("---")
    st.markdown("© 2026 - Proyecto Integrador de Analítica")
