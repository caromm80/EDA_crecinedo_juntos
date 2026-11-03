# 🌟 Momento 1: Aplicación en Consola - Lumi Mood & Gratitude Tracker

Este módulo corresponde a la entrega del **Momento 1**, evidenciando la aplicación de fundamentos de lógica de programación en Python, estructuras de datos nativas y buenas prácticas de versionamiento con Git.

---

## 🎯 Requerimientos Cumplidos

1. **Menú Interactivo (`while True`)**:
   - Menú continuo en consola que no se cierra hasta que el usuario elija explícitamente la opción de salir.
   - Manejo de excepciones con `try/except` para prevenir caídas por datos no numéricos o vacíos.

2. **Estructuras de Datos (Listas y Diccionarios)**:
   - **Diccionario:** Representa cada entrada individual del diario con claves semánticas (`id`, `usuario`, `fecha`, `nivel_animo`, `emocion`, `gratitud`, `aprobado_dia_positivo`).
   - **Lista:** Colección ordenada en memoria (`registros_diario`) que almacena todas las entradas generadas durante la sesión.

3. **Separación de Lógica en Funciones**:
   - `mostrar_banner()`: Interfaz visual amigable y presentación de la mascota Lumi.
   - `registrar_ingreso(registros)`: Captura de datos, validación y almacenamiento.
   - `mostrar_todas_las_entradas(registros)`: Formateo tabular de los registros.
   - `calcular_promedio_animo(registros)`: Cálculo de promedios generales e individuales.
   - `evaluar_dias_aprobados(registros)`: Segmentación y análisis de días positivos vs días por atender (incorporado en `feature/aprueba`).

4. **Versionamiento Git**:
   - Ramas implementadas: `main`, `develop`, `feature/notas`, `feature/aprueba`.
   - Historial de commits descriptivos siguiendo la convención de Git Flow.

---

## 🚀 Cómo Ejecutar

Desde la terminal en la raíz del proyecto o dentro de la carpeta:

```bash
# Opción 1: Desde la raíz del proyecto
python python_momento1/app_consola.py

# Opción 2: Dentro de la carpeta python_momento1
cd python_momento1
python app_consola.py
```

---

## 💡 Guía para la Defensa Oral
- **¿Por qué usar diccionarios?** Porque permiten asociar información con claves claras (`usuario`, `nivel_animo`, `gratitud`) facilitando el acceso directo y la legibilidad del código.
- **¿Por qué usar una lista?** Porque permite acumular dinámicamente un número indefinido de registros secuenciales.
- **¿Por qué separar en funciones?** Facilita la reutilización de código, el mantenimiento, las pruebas unitarias y evita la duplicación de lógica.
