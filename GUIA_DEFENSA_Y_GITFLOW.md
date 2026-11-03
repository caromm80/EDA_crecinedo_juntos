# 🎓 Guía Maestra para la Defensa Oral y Comandos Git Flow
> **Proyecto: Lumi - Diario de Gratitud y Estado de Ánimo (Mood Tracker)**  
> **Institución: CESDE 2026 • Asignatura: Desarrollo de Software & Analítica**

Esta guía está diseñada para que respondas con absoluta seguridad, solvencia técnica y dominio conceptual ante cualquier pregunta de los evaluadores.

---

## 📌 PARTE 1: DEFENSA MOMENTO 1 (Fundamentos de Python y Git)

### 1. ¿Cómo crear y clonar un repositorio en Git?
- **Crear un repo local:**
  ```bash
  git init
  git branch -M main
  ```
- **Conectar con GitHub:**
  ```bash
  git remote add origin https://github.com/caromm80/EDA_crecinedo_juntos.git
  git push -u origin main
  ```
- **Clonar un repositorio existente:**
  ```bash
  git clone https://github.com/caromm80/EDA_crecinedo_juntos.git
  cd EDA_crecinedo_juntos
  ```

---

### 2. ¿Qué ramas existen en el proyecto y qué contiene cada una?
1. **`main`**: Rama de producción con código estable.
2. **`develop` / `dev`**: Rama central de integración continua.
3. **`feature/notas`**: Implementó el menú interactivo, la estructura de listas y diccionarios y la captura de notas/ánimo con cálculo de promedios.
4. **`feature/aprueba`**: Implementó la lógica de aprobación emocional (`evaluar_dias_aprobados`), segmentando días con ánimo $\ge 3$ frente a días por atender.
5. **`release/analisis-v1`**: Implementó el módulo de analítica con Pandas (`data_cleaner.py` y `analisis.py`).
6. **`feature/web-spa`**: Implementó la aplicación web completa en React con Vite y Context API.

---

### 3. ¿Por qué usamos un ciclo `while` en el menú y cómo evitamos un bucle infinito?
- Usamos `while True` para que la aplicación en consola se mantenga en ejecución continua mientras el usuario interactúa.
- Se evita el bucle infinito porque existe una opción explícita de salida (`opcion == "6": break`), la cual rompe el ciclo y finaliza el programa de manera controlada.

---

### 4. ¿Cuál es la diferencia entre una lista y un diccionario en Python?
- **Diccionario (`dict`)**: Colección de pares clave-valor (`{"usuario": "Carolina", "nivel_animo": 5}`). Permite acceder a los datos por nombre semántico en tiempo $O(1)$. Lo usamos para modelar cada **registro individual**.
- **Lista (`list`)**: Colección indexada y ordenada de elementos (`registros_diario = [...]`). Permite agregar (`append`), iterar y acumular un número dinámico de registros en memoria.

---

### 5. ¿Por qué modularizar el código en funciones?
- **Reutilización:** Evita duplicar código (principio DRY: *Don't Repeat Yourself*).
- **Mantenibilidad:** Si hay un error en el cálculo de promedios, solo modificamos `calcular_promedio_animo()` sin alterar el menú ni el registro.
- **Legibilidad:** El script principal se vuelve autoexplicativo y fácil de depurar.

---

## 📌 PARTE 2: DEFENSA MOMENTO 2 (Pandas, EDA y Entornos Virtuales)

### 1. ¿Qué es un DataFrame y en qué se diferencia de una matriz o un diccionario?
- Un **DataFrame** es una estructura de datos bidimensional (filas y columnas) de la librería Pandas.
- A diferencia de una matriz clásica (que suele ser homogénea, solo números), un DataFrame es **heterogéneo**: cada columna puede tener un tipo de dato distinto (cadenas de texto, números enteros, flotantes, fechas y booleanos).
- A diferencia de un diccionario simple, el DataFrame implementa operaciones vectorizadas de álgebra de datos a nivel de lenguaje C (filtrado booleano, agrupaciones `groupby` y uniones relacionales `merge`) con altísimo rendimiento.

---

### 2. ¿Por qué usamos Entornos Virtuales (`venv`)?
- **Aislamiento:** Permite que las librerías de este proyecto (ej: `pandas 2.3`) no entren en conflicto con otros proyectos que requieran versiones distintas.
- **Portabilidad y Reproducibilidad:** Cualquier compañero puede clonar el proyecto y reconstruir el entorno exacto ejecutando `pip install -r requirements.txt`.
- **Limpieza:** No se contamina la instalación global de Python del sistema operativo.

---

### 3. ¿Por qué `.venv` debe estar en el archivo `.gitignore`?
- El entorno virtual contiene miles de archivos binarios compilados específicamente para la arquitectura y sistema operativo de tu máquina local.
- No es portable entre Windows, Mac o Linux.
- Pesa cientos de megabytes innecesarios en el repositorio. La buena práctica universal es versionar el código y el archivo de especificaciones `requirements.txt`.

---

### 4. ¿Qué funciones contiene `data_cleaner.py` y qué problemas corrigieron?
1. **`cargar_datos(ruta)`**: Valida la existencia física del CSV y lo lee con codificación UTF-8.
2. **`manejar_valores_nulos(df, estrategia='auto')`**: Detecta celdas vacías (`NaN`). Imputa valores numéricos con la **mediana** (más robusta que el promedio ante valores atípicos) y columnas categóricas con la **moda**.
3. **`estandarizar_texto(df, columnas)`**: Elimina espacios sobrantes (`strip()`) y unifica a minúsculas (`lower()`), corrigiendo inconsistencias como `"  BOGOTA "` vs `"bogota"`.
4. **`limpieza_especifica_proyecto(df)`**: Remueve caracteres de formato como `$` y `%` en `nivel_energia` (ej: transformando `"$85%"` en el número flotante `85.0`) y castea fechas a `datetime`.

---

### 5. ¿Qué preguntas responde `analisis.py`?
1. **Frecuencia:** Identifica al usuario líder con más entradas registradas en la plataforma (`groupby(['id_usuario', 'nombre_completo']).size()`).
2. **Agregación (`groupby`):** Calcula el promedio de ánimo, horas de sueño y nivel de energía agrupado por categoría de ocupación.
3. **Filtrado y Conteo:** Segmenta los registros que cumplen simultáneamente la condición de bienestar: `(nivel_animo >= 4) & (horas_sueno >= 7.0)`.

---

## 📌 PARTE 3: DEFENSA MOMENTO WEB (React, Vite, SPA, Context API)

### 1. ¿Por qué usamos Vite en lugar de herramientas tradicionales?
- **Vite** utiliza los módulos ES nativos del navegador (*ES Modules*) y un empaquetador en Rust/Go (*esbuild*), lo que hace que el servidor de desarrollo inicie en milisegundos y el Hot Module Replacement (HMR) sea instantáneo.

---

### 2. ¿Qué es un Componente Reutilizable y cómo está estructurada la app?
- Un componente es una función de JavaScript que retorna JSX (interfaz de usuario) y encapsula su propia lógica y estilo.
- En nuestra app tenemos componentes especializados desacoplados:
  - `<Navbar />` y `<Footer />` (Navegación y pie)
  - `<MainLayout />` y `<AuthLayout />` (Estructura base)
  - `<LumiMonster />` (Mascota SVG interactiva)
  - `<MoodSelector />` (Selector de emociones)
  - `<MoodCard />` (Tarjeta individual de nota con botones de editar y borrar)
  - `<GratitudeForm />` (Formulario controlado)
  - `<MoodChart />` (Gráficos con Chart.js)
  - `<ListaUsuarios />` (Directorio con 24 usuarios quemados en código)

---

### 3. ¿Qué es un Formulario Controlado en React?
- Es un formulario donde el valor de cada input está enlazado directamente a un estado de React (`value={motivoGratitud}`) y cualquier modificación dispara una función actualizadora (`onChange={(e) => setMotivoGratitud(e.target.value)}`).
- **Ventaja:** React tiene el control absoluto del dato en todo momento, permitiendo validaciones en tiempo real, deshabilitar botones si el formulario es inválido y prevenir envíos con campos vacíos.

---

### 4. ¿Qué es "Prop Drilling" y cómo lo resolviste con Context API?
- **Prop Drilling:** Ocurre cuando necesitas pasar datos a través de múltiples niveles de componentes anidados que no necesitan esa información, solo para hacérsela llegar a un componente hijo en lo profundo del árbol.
- **Solución implementada:** Usamos **Context API** (`createContext`, `Provider` y `useContext`) mediante dos proveedores globales:
  - `ThemeContext`: Maneja el tema claro/oscuro en toda la jerarquía.
  - `MoodContext`: Centraliza las operaciones CRUD (crear, leer, actualizar, borrar notas de gratitud) accesibles desde cualquier componente sin pasar props manualmente.

---

### 5. ¿Por qué la aplicación web no usa emojis estándar clásicos?
- Para cumplir el requerimiento de diseño cálido y ameno, creamos a **Lumi**, un simpático monstruito vectorial SVG propio, con expresiones personalizadas adaptativas según el nivel de ánimo (Radiante, Calmado, Estable, Pensativo y Apapacho), acompañado de bocadillos de diálogo interactivos y tarjetas ilustradas.
