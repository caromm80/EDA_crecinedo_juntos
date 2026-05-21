# 📋 Guía: Configurar y Conectar MockAPI.io con Creciendo Juntos

Esta guía te explica paso a paso cómo subir los datos educativos de **Creciendo Juntos** en la nube usando **MockAPI.io** para tu sustentación académica.

---

## ☁️ Paso 1: Crear tu API en MockAPI.io

1. Abre tu navegador e ingresa a [mockapi.io](https://mockapi.io).
2. Regístrate gratis o inicia sesión con tu cuenta.
3. Haz clic en **"+ New Project"** (Nuevo Proyecto):
   - **Project Name:** `Creciendo Juntos`
   - **API Prefix:** (Déjalo en blanco)
   - Haz clic en **"Create"**.
4. Verás la URL base de tu proyecto, que tiene un formato como este:
   `https://69f350d4bd2396bf530fbde8.mockapi.io` (los números de tu ID serán diferentes).

---

## 📊 Paso 2: Crear los Recursos (Entidades) en MockAPI

Debes crear los recursos que la aplicación va a consultar. Haz clic en **"+ New Resource"** para cada uno de estos:

### 1. Entidad: `estudiantes`
* **Resource Name (Nombre exacto en minúsculas):** `estudiantes`
* Agrega los siguientes campos con sus tipos:
  * `id`: **Number** (Autogenerado)
  * `Nombre`: **String**
  * `Edad`: **Number**
  * `Genero`: **String**
  * `Ciudad`: **String**
  * `Promedio`: **Number**
  * `Estado`: **String**
  * `Materias_Inscritas`: **Number**
  * `Creditos_Aprobados`: **Number**
  * `Estrato`: **Number**
  * `Asistencia_%`: **Number**
* Haz clic en **"Create"**.

### 2. Entidad: `cursos`
* **Resource Name:** `cursos`
* Campos:
  * `id`: **Number**
  * `Nombre`: **String**
  * `Código`: **String**
  * `Docente`: **String**
  * `Créditos`: **Number**
  * `Alumnos_Inscritos`: **Number**

### 3. Entidad: `calificaciones`
* **Resource Name:** `calificaciones`
* Campos:
  * `id`: **Number**
  * `Estudiante`: **String**
  * `Curso`: **String**
  * `Docente`: **String**
  * `Nota_Parcial`: **Number**
  * `Nota_Final`: **Number**
  * `Resultado`: **String**

### 4. Entidad: `inscripciones`
* **Resource Name:** `inscripciones`
* Campos:
  * `id`: **Number**
  * `Estudiante`: **String**
  * `Curso`: **String**
  * `Fecha_Inscripcion`: **String**
  * `Progreso_%`: **Number**

---

## 📥 Paso 3: Subir los Datos de Ejemplo (Importar)

Puedes autogenerar registros directamente en MockAPI o cargarlos rápidamente:
1. En tu recurso (por ejemplo, `estudiantes`), haz clic en el botón de la fila que dice **"Data"** o usa la opción de **"Bulk Add / Import"**.
2. Puedes usar el botón **"Generate"** en MockAPI para crear 50 registros aleatorios al instante.
3. Para la entidad `estudiantes`, si quieres usar exactamente los 100 registros realistas del archivo local `estudiantes_creciendo_juntos.csv`:
   - Abre el archivo `estudiantes_creciendo_juntos.csv` en Excel o Bloc de notas.
   - Súbelo usando la herramienta de importación masiva de MockAPI.

---

## 🔌 Paso 4: Conectar MockAPI con el Dashboard

1. Copia el **ID de tu proyecto** desde la URL de MockAPI (son los 24 caracteres alfanuméricos después de `https://` y antes de `.mockapi.io`). Por ejemplo, en `https://69f350d4bd2396bf530fbde8.mockapi.io`, tu ID es `69f350d4bd2396bf530fbde8`.
2. Ejecuta tu aplicación en la terminal:
   ```bash
   streamlit run Inicio.py
   ```
3. En el menú de la aplicación, ve a la sección **"Consumo de API"**.
4. En la barra lateral izquierda, en **Selector de Origen de Datos**, selecciona:
   * **`☁️ API Cloud REST (MockAPI.io)`**
5. Pega el **ID de tu proyecto** en el campo de texto correspondiente.
6. ¡Listo! El sistema descargará e indexará dinámicamente toda la información académica desde los servidores en la nube de MockAPI, actualizando los gráficos interactivos al instante.

---

## 💡 Ventajas de usar MockAPI para la Presentación:
- **Es 100% Nube:** Los datos no están locales en tu disco; se descargan en tiempo real usando el protocolo seguro HTTPS.
- **Acceso REST API Real:** La aplicación Python realiza peticiones `GET` HTTP verdaderas a los servidores en la nube de MockAPI, simulando con precisión extrema un entorno de producción profesional.
