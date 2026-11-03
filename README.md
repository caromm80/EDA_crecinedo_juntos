# 🌸 Lumi: Diario de Gratitud y Estado de Ánimo (Mood Tracker)
> **Proyecto Integrador CESDE 2026 • Creciendo Juntos**

Bienvenido(a) a **Lumi**, una plataforma integral y acogedora diseñada para registrar diariamente cómo te sientes, cultivar la gratitud consciente y reflexionar sobre tu evolución emocional.

El proyecto incorpora a **Lumi**, un simpático monstruito guardián diseñado vectorialmente de manera exclusiva para la aplicación, quien cambia sus expresiones (Radiante, Calmado, Estable, Pensativo, Apapacho) según tus estados de ánimo y te brinda mensajes de aliento y cariño.

---

## 🎯 Arquitectura de Momentos Evaluativos

Este repositorio contiene la evidencia completa del ciclo de desarrollo de software estructurado en tres grandes momentos:

```
cesde_ntp_EDA/
├── data/                                 # 📂 Momento 2: Datasets relacionados (>50 registros c/u)
│   ├── usuarios_mood.csv                 # 55 usuarios con datos demográficos
│   └── registros_gratitud.csv            # 85 registros de diario y métricas
│
├── python_momento1/                      # 🐍 Momento 1: Lógica en Python por Consola
│   ├── app_consola.py                    # Menú continuo (while), listas, diccionarios y funciones
│   └── README.md                         # Guía y documentación específica Momento 1
│
├── python_momento2/                      # 📊 Momento 2: Análisis de Datos con Pandas (EDA)
│   ├── data_cleaner.py                   # Módulo de funciones: carga, nulos, estandarización y tipos
│   ├── analisis.py                       # Script principal con merge, groupby y respuestas clave
│   ├── requirements.txt                  # Dependencias de Python (pandas, numpy)
│   └── README.md                         # Documentación teórica (DataFrames, venv)
│
├── frontend_web/                         # ⚛️ Momento Web 1 & 2: Single Page Application (SPA)
│   ├── public/
│   │   └── favicon.svg                   # Favicon vectorial de Lumi
│   ├── src/
│   │   ├── assets/                       # Gráficos y recursos visuales
│   │   ├── components/                   # Componentes modulares reutilizables
│   │   │   ├── LumiMonster.jsx           # Mascota interactiva SVG con micro-animaciones
│   │   │   ├── MoodSelector.jsx          # Selector de ánimo 1 al 5 sin emojis clásicos
│   │   │   ├── MoodChart.jsx             # Gráficos temporales con Chart.js
│   │   │   ├── StatWidget.jsx            # Widgets de estadísticas de bienestar
│   │   │   ├── MoodCard.jsx              # Tarjeta de nota de gratitud con acciones CRUD
│   │   │   ├── GratitudeForm.jsx         # Formulario controlado (Semana 9)
│   │   │   ├── ListaUsuarios.jsx         # Componente con 20+ usuarios quemados en código
│   │   │   ├── TeamCredits.jsx           # Asignación de componente por persona
│   │   │   ├── Navbar.jsx                # Barra superior con toggle de tema claro/oscuro
│   │   │   └── Footer.jsx                # Pie de página reflexivo y créditos
│   │   ├── context/                      # Context API (Semana 11 - Sin Prop Drilling)
│   │   │   ├── ThemeContext.jsx          # Tema cálido (claro) y tema noche (oscuro)
│   │   │   ├── MoodContext.jsx           # CRUD Global con 22 registros mock iniciales
│   │   │   └── AuthContext.jsx           # Simulación de sesión de usuario
│   │   ├── layouts/
│   │   │   ├── MainLayout.jsx            # Layout principal con firma de página
│   │   │   └── AuthLayout.jsx            # Layout acogedor de autenticación
│   │   ├── routes/
│   │   │   └── routes.jsx                # Enrutamiento SPA con React Router DOM
│   │   ├── views/                        # Vistas de la aplicación
│   │   ├── App.jsx                       # Conexión de providers globales
│   │   ├── main.jsx                      # Entrada Vite
│   │   └── index.css                     # Sistema de diseño ameno y responsivo
│   ├── package.json                      # Dependencias de npm
│   └── vite.config.js                    # Configuración de Vite
│
├── GUIA_DEFENSA_Y_GITFLOW.md             # 🎓 Preguntas de examen, comandos y defensa oral
├── .gitignore                            # Exclusión de entornos virtuales y compilados
└── README.md                             # Este archivo
```

---

## 🚀 Guía de Instalación y Ejecución Rápida

### 1. Clonar el Repositorio
```bash
git clone https://github.com/caromm80/EDA_crecinedo_juntos.git
cd EDA_crecinedo_juntos
```

---

### 2. Ejecutar Momento 1 (Python Consola)
```bash
python python_momento1/app_consola.py
```
- **Opciones disponibles:** Registrar Entrada, Ver Historial Tabular, Promedios Generales e Individuales, Evaluación de Días Aprobados (Ánimo ≥ 3) y Filtrado por Emoción.

---

### 3. Ejecutar Momento 2 (Análisis de Datos con Pandas)
Configurar el entorno virtual e instalar dependencias:
```bash
# Windows
python -m venv .venv
.\.venv\Scripts\activate

# Mac / Linux
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependencias
pip install -r python_momento2/requirements.txt

# Ejecutar el script de análisis
python python_momento2/analisis.py
```

#### Respuestas obtenidas en el análisis:
1. **Análisis de Frecuencia:** Identifica al usuario líder con mayor cantidad de registros en la plataforma.
2. **Análisis de Agregación (`groupby`):** Promedio de ánimo y horas de sueño agrupado por categoría de ocupación.
3. **Análisis con Filtrado y Conteo:** Conteo de días de alto bienestar (ánimo ≥ 4 y horas de sueño ≥ 7.0 hrs).

---

### 4. Ejecutar Momento Web (Frontend React + Vite)
```bash
cd frontend_web
npm install
npm run dev
```
La aplicación web estará disponible de inmediato en: **`http://localhost:5173`**

---

## 🌿 Estructura de Ramas en Git Flow

Para cumplir con todos los requerimientos de versionamiento, el proyecto cuenta con las siguientes ramas:

| Rama | Propósito | Estado |
| :--- | :--- | :--- |
| `main` | Código de producción final y estable | Integrada |
| `develop` / `dev` | Rama base de integración continua | Activa |
| `feature/notas` | Momento 1: Registro de entradas, notas y promedios | Fusionada con PR |
| `feature/aprueba` | Momento 1: Función de evaluación de días aprobados y filtros | Fusionada con PR |
| `release/analisis-v1` | Momento 2: Módulo `data_cleaner.py`, datasets y `analisis.py` | Versionada |
| `feature/web-spa` | Momento Web: React, Vite, Context API, Chart.js y UI de Lumi | Fusionada en `dev` |

---

## 👥 Equipo de Trabajo & Asignación de Componentes

| Integrante | Rol | Componente Asignado |
| :--- | :--- | :--- |
| **Carolina Morales** | Líder de Frontend & UX | `<LumiMonster />` y `<MoodSelector />` |
| **Mateo Restrepo** | Arquitectura SPA & Layouts | `<MainLayout />`, `<AuthLayout />` y `routes.jsx` |
| **Valentina Gómez** | Estado Global & Temas | `<MoodContext />` y `<ThemeContext />` |
| **Andrés Felipe** | Formularios & Validaciones | `<GratitudeForm />` y `<MoodCard />` |
| **Sofía Ramírez** | Analítica & Comunidad | `<ListaUsuarios />` y `<MoodChart />` |

---

## 📚 Soporte para la Defensa Oral
Consulta el archivo [GUIA_DEFENSA_Y_GITFLOW.md](file:///c:/Users/carol/cesde_ntp_EDA/GUIA_DEFENSA_Y_GITFLOW.md) para repasar las respuestas a preguntas teóricas del evaluador (DataFrames, entornos virtuales, prop drilling, ciclos de vida y comandos Git).
