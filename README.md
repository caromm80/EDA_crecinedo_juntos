# 🚀 Proyecto Integrador: Analítica de Datos.

## 📋 Descripción
Proyecto integrador que implementa un Análisis Exploratorio de Datos (EDA) interactivo usando **Streamlit** y **Pandas**. Permite cargar datasets en formato CSV y explorar sus características, estadísticas y patrones sin necesidad de gráficos, enfocándose en la interpretación numérica y textual.

---

## 🛠️ Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/USUARIO/cesde_ntp_EDA.git
cd cesde_ntp_EDA
```

### 2. Crear entorno virtual
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Mac/Linux
python -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

---

## 🚀 Uso

### Ejecutar la aplicación
```bash
streamlit run Inicio.py
```

La aplicación se abrirá en tu navegador en `http://localhost:8501`

### Navegación
- **Inicio:** Portada con introducción y objetivos
- **Análisis Exploratorio:** Herramienta interactiva para explorar datos
- **Resultados:** Formulario para documentar hallazgos y generar reportes

---

## 📊 Estructura del Proyecto
```
cesde_ntp_EDA/
├── Inicio.py                                 # Página principal
├── pages/
│   ├── 1_Análisis Exploratorio de Datos (EDA).py  # Módulo EDA
│   └── 2_Resultados (EDA).py                      # Formulario de resultados
├── Accidentes_de_tránsito_reportados_en_los_municipios_que_tienen_convenio_con_la_Gerencia_de_Seguridad_Vial_de_Antioquia_20260521.csv  # Dataset ejemplo
├── requirements.txt                          # Dependencias
├── .gitignore                                # Archivos ignorados
└── README.md                                 # Este archivo
```

---

## 🔍 Características Principales

### 🔹 Análisis Exploratorio (EDA)
- Carga de archivos CSV (local o upload)
- Vista previa de datos
- Información de estructura (filas, columnas, tipos)
- Detección de valores faltantes
- Estadísticas descriptivas (numérica y categórica)
- Frecuencia de valores más comunes

### 🔹 Generación de Reportes
- Formulario estructurado para documentar hallazgos
- Descarga de reporte en formato Markdown (.md)
- Timestamp automático en reportes

---

## 📝 Dataset Ejemplo
El proyecto incluye un dataset de **accidentes de tránsito** en Colombia (2023) con:
- 300 registros
- Variables: Fecha, Hora, Ciudad, Tipo de Accidente, Clima, entre otros
- Datos completos sin valores nulos

---

## 👥 Equipo de Trabajo
Completa los nombres en `Inicio.py`:
```python
integrantes = [
    {"nombre": "Integrante 1", "rol": "Rol", "emoji": "👨‍💻"},
    {"nombre": "Integrante 2", "rol": "Rol", "emoji": "👩‍🔬"},
    {"nombre": "Integrante 3", "rol": "Rol", "emoji": "👨‍💼"},
]
```

---

## 📦 Dependencias
- **streamlit** - Framework para apps web de datos
- **pandas** - Análisis y manipulación de datos
- **numpy** - Computación numérica

---

## 📤 Entrega del Proyecto
1. ✅ Subir código a GitHub
2. ✅ Generar reporte desde la aplicación
3. ✅ Documentar conclusiones en Markdown

---

## 📞 Soporte
En caso de errores o preguntas, verifica:
- Python versión 3.8+
- Archivo CSV con formato correcto
- Entorno virtual activado

---

*© 2026 - Proyecto Integrador de Analítica*
