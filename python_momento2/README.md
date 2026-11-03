# 📊 Momento 2: Análisis Exploratorio y Limpieza de Datos con Pandas

Este módulo contiene la implementación del **Momento 2**, enfocado en la ingeniería de datos con Python, limpieza programática mediante funciones modulares y análisis estadístico con **Pandas**.

---

## 🎯 Requerimientos y Entregables Cumplidos

### 1. Datos del Proyecto (`data/`)
- Dos archivos CSV relacionados entre sí mediante la clave foránea `id_usuario`:
  - `data/usuarios_mood.csv`: 55 registros de usuarios (nombre, edad, ciudad, ocupación, fecha de registro). Contiene nulos intencionales y textos con mayúsculas/espacios desordenados.
  - `data/registros_gratitud.csv`: 85 registros diarios de bienestar (nivel de ánimo, emoción principal, motivo de gratitud, horas de sueño, nivel de energía con caracteres especiales como `$`, `%` y `pts`).

### 2. Módulo de Preprocesamiento (`python_momento2/data_cleaner.py`)
Contiene 4 funciones esenciales reutilizables:
1. `cargar_datos(ruta_archivo)`: Carga el archivo validando su existencia y capturando excepciones.
2. `manejar_valores_nulos(df, estrategia='auto')`: Detecta valores nulos (`NaN` o vacíos) e imputa numéricos con la mediana y categóricos con la moda.
3. `estandarizar_texto(df, columnas)`: Normaliza texto eliminando espacios sobrantes (`str.strip()`) y convirtiendo a minúsculas (`str.lower()`).
4. `limpieza_especifica_proyecto(df)`: Remueve símbolos de formato (`$`, `%`, `pts`) en el nivel de energía, castea tipos y asegura formatos válidos de fecha.

### 3. Script Principal (`python_momento2/analisis.py`)
Ejecuta la limpieza, combina los datasets con `pd.merge()` y responde en consola las 3 preguntas clave:
1. **Análisis de Frecuencia:** Identifica al usuario con mayor cantidad de registros en la plataforma.
2. **Análisis de Agregación:** Calcula métricas clave (ánimo promedio, horas de sueño y porcentaje de energía) agrupadas por categoría de ocupación con `groupby()`.
3. **Análisis con Filtrado y Conteo:** Segmenta y cuenta los registros correspondientes a "Días Óptimos de Alto Bienestar" (ánimo >= 4 y horas de sueño >= 7.0 hrs).

---

## 🛠️ Configuración del Entorno Virtual (venv)

### 1. Crear el Entorno Virtual
```bash
# Windows
python -m venv .venv

# Mac / Linux
python3 -m venv .venv
```

### 2. Activar el Entorno Virtual
```bash
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# Windows (CMD)
.\.venv\Scripts\activate.bat

# Mac / Linux
source .venv/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install -r python_momento2/requirements.txt
```

### 4. Ejecutar el Script de Análisis
```bash
# Desde la raíz del proyecto
python python_momento2/analisis.py
```

---

## 📚 Preguntas Clave para la Defensa Oral (Conocimiento & Desempeño)

### 1. ¿Qué es un DataFrame?
Un **DataFrame** es la estructura de datos bidimensional fundamental de la biblioteca Pandas, similar a una tabla relacional o una hoja de cálculo en Excel.
- Se compone de filas (observaciones) y columnas (variables o características).
- Cada columna puede tener un tipo de dato diferente (enteros, flotantes, strings, fechas, booleanos).
- Posee índices para filas y columnas, lo cual permite realizar operaciones vectorizadas de indexación, filtrado, transformaciones matemáticas, agrupaciones (`groupby`) y fusiones (`merge`) a alta velocidad y bajo consumo de memoria.

### 2. ¿Por qué usamos Entornos Virtuales (`venv`)?
Los entornos virtuales permiten **aislar** las dependencias y versiones de paquetes que utiliza un proyecto específico del entorno global del sistema operativo.
- **Evita conflictos de versiones:** Si el Proyecto A requiere `pandas 1.5` y el Proyecto B requiere `pandas 2.3`, un entorno virtual garantiza que ambos funcionen en la misma máquina sin interferir entre sí.
- **Reproducibilidad:** Permite que cualquier miembro del equipo o evaluador clone el repositorio y reinstale exactamente las mismas librerías mediante `pip install -r requirements.txt`.
- **Limpieza del sistema:** Mantiene el sistema operativo limpio sin saturar el Python global con librerías innecesarias.

### 3. ¿Por qué se debe incluir `.venv/` en `.gitignore`?
El entorno virtual contiene miles de archivos binarios y dependencias pesadas compiladas para el sistema operativo local. No debe subirse a Git porque:
- Hace el repositorio innecesariamente pesado (cientos de megabytes).
- Los binarios compilados en Windows no funcionan directamente en Linux o Mac.
- La buena práctica universal es versionar únicamente el código fuente y el archivo `requirements.txt`.
