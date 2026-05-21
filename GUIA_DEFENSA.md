# 📖 Guía de Defensa del Proyecto: Creciendo Juntos

¡Hola! Esta guía ha sido creada especialmente para ayudarte a **sustentar y defender tu proyecto de analítica con la máxima calificación**. Aquí tienes las explicaciones sencillas y las respuestas exactas que tu evaluador o profesor esperará escuchar.

---

## 🎯 1. Conceptos Básicos que Debes Dominar (¡Memoriza esto!)

Cuando el profesor te pregunte por términos técnicos, respóndele con estas frases sencillas:

*   **¿Qué es una API?**
    > *"Profesor, una API (Interfaz de Programación de Aplicaciones) es como un mensajero o puente que permite a dos programas comunicarse. En nuestro caso, conecta nuestra interfaz visual en Streamlit con el servidor backend (hecho en Java) para pedirle datos."*
*   **¿Qué es un formato JSON?**
    > *"JSON es el formato estándar en la web para enviar y recibir datos en texto plano. Es muy liviano y se organiza con llaves y corchetes `{ } [ ]`, lo que facilita que tanto humanos como computadores lo lean fácilmente."*
*   **¿Qué es Pandas y qué es un DataFrame?**
    > *"Pandas es la biblioteca de Python más famosa para analizar datos. Un **DataFrame** es la estructura principal de Pandas: imagínelo como una tabla de Excel inteligente, con filas y columnas, que nos permite filtrar, agrupar y calcular promedios en milisegundos."*
*   **¿Qué es Streamlit?**
    > *"Es un framework moderno de Python que nos permite crear aplicaciones web interactivas para ciencia de datos de forma rápida, sin necesidad de saber lenguajes complejos de frontend como HTML, CSS o JavaScript."*

---

## 🔌 2. ¿Cómo funciona la conexión a la API en tu código?

En tu archivo [3_Consumo_de_API.py](file:///c:/Users/carol/cesde_ntp_EDA/pages/3_Consumo_de_API.py), la conexión se explica en tres partes sencillas:

1.  **La Petición HTTP (`requests.get`):**
    Usamos la librería `requests` de Python para llamar al servidor:
    ```python
    respuesta = requests.get(url_completa, timeout=5)
    ```
    *Explicación:* *"Enviamos una solicitud 'GET' (obtener) a la URL de la API. Si el servidor responde exitosamente (código HTTP 200), convertimos ese JSON en una tabla de Pandas usando `pd.DataFrame(respuesta.json())`"*.

2.  **El Plan de Contingencia (El Simulador):**
    Esta es tu mejor arma en la sustentación. Si la API Java no está encendida, el código no se cae. En su lugar, el checkbox de la barra lateral carga datos de prueba que definiste localmente:
    *Explicación:* *"Para garantizar que la aplicación web siempre esté disponible e independiente, agregué un interruptor en la barra lateral. Si la API Java real está apagada, la aplicación cambia al **modo simulador local**, cargando una lista de diccionarios en memoria. Así la experiencia del usuario y la analítica de gráficos no se interrumpen"*.

3.  **El Caché Inteligente (`@st.cache_data`):**
    Encima de la función de cargar datos verás esto: `@st.cache_data`.
    *Explicación:* *"Esto sirve para optimizar el rendimiento. Streamlit guarda los datos en memoria caché. Así, si el usuario navega o filtra, no tenemos que volver a hacer peticiones HTTP repetitivas a la API por internet, ahorrando red y tiempo de carga"*.

---

## 📊 3. ¿Cómo se crean los Estadísticas y Gráficos?

El profesor querrá saber cómo calculas los datos del Dashboard:

1.  **Las Métricas / KPIs (`st.metric`):**
    Usa operaciones básicas de Pandas:
    *   **Promedio General:** `df_filtrado["Promedio"].mean()` calcula la media aritmética de las notas automáticamente.
    *   **Conteo de Alumnos:** `len(df_filtrado)` nos da el número total de filas.
    *   **Alumnos en Riesgo:** `len(df_filtrado[df_filtrado["Estado"] == "En Riesgo"])` hace un filtro y cuenta cuántos cumplen esa condición.

2.  **Los Gráficos Dinámicos (`st.bar_chart` y `st.scatter_chart`):**
    Streamlit hace todo el trabajo pesado. Solo le pasamos los datos:
    *   *Ejemplo de Estado:* `df_filtrado["Estado"].value_counts()` agrupa y cuenta cuántos alumnos hay por estado, y `st.bar_chart` dibuja las barras al instante.
    *   *Ejemplo de Dispersión:* Con `st.scatter_chart(df, x="Edad", y="Promedio")` cruzamos dos variables numéricas en un gráfico interactivo donde cada punto es un estudiante.

---

## 👩‍🏫 4. Preguntas Incómodas de los Profesores y Cómo Responderlas

*   **P: "¿Por qué utilizas Pandas en lugar de ciclos `for` tradicionales de Python para filtrar?"**
    *   *R:* *"Porque Pandas está optimizado en lenguaje C. Filtrar usando `df[df['Ciudad'] == 'Medellín']` es mucho más rápido, requiere menos líneas de código y es la práctica estándar en la industria de la Ciencia de Datos"*.
*   **P: "¿Cómo manejas los errores de conexión de la API?"**
    *   *R:* *"Utilizo un bloque `try-except` para capturar excepciones como `requests.exceptions.ConnectionError`. Si la conexión falla, el código captura el error de forma segura, muestra una alerta amigable en color rojo usando `st.error` y le ofrece al usuario la opción de cambiar al modo simulador"*.
*   **P: "¿Qué hace la función `df_datos.copy()` en los filtros?"**
    *   *R:* *"Hacemos una copia limpia de los datos originales cargados para que, cuando el usuario aplique o cambie filtros, siempre operemos sobre la base de datos original sin modificar ni dañar la memoria del caché"*.

---

## 💡 5. Consejos Finales para el Día del Examen
1.  **Empieza en modo simulador:** Inicia la presentación con el checkbox **"Usar Datos de Prueba (Simulador)"** activo. Muestra lo bonito que se ve, cómo cambian los gráficos al filtrar por ciudades, y resalta las tarjetas de promedios.
2.  **Muestra tu destreza:** Luego, explícale al profesor que tu código también está listo para conectar con un servidor real. Desmarca la casilla, muestra la alerta roja de "No se pudo conectar" y explica el bloque de control de errores. **¡Esto demostrará que pensaste en todo!**
3.  **Mantén la calma:** El código es muy directo y limpio. Si te preguntan por alguna línea que no recuerdes, busca los comentarios del código; te guiarán de inmediato.

¡Muchos éxitos! Tienes un proyecto muy estético, funcional y sumamente fácil de explicar. ¡Vas a brillar! 🎓🌟
