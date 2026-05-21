import json
import random

# Seed para consistencia
random.seed(42)

# Cargar estudiantes existentes para usar sus nombres
with open("c:/Users/carol/cesde_ntp_EDA/datos_mockapi_50_estudiantes.json", "r", encoding="utf-8") as f:
    estudiantes = json.load(f)

nombres_estudiantes = [est["Nombre"] for est in estudiantes]

# 1. GENERAR CURSOS
cursos_nombres = [
    ("Programación Python", "PY101", "Ing. Carlos Pérez", 4),
    ("Bases de Datos", "BD102", "Dra. Martha Gómez", 3),
    ("Introducción a la IA", "IA103", "Msc. Juan Díaz", 4),
    ("Desarrollo Web", "DW104", "Ing. Luis Ruiz", 3),
    ("Ingeniería de Requisitos", "IR105", "Dra. Sandra Castro", 3),
    ("Arquitectura de Software", "AS106", "Ing. Andrés Torres", 4)
]

datos_cursos = []
for idx, (nombre, codigo, docente, creditos) in enumerate(cursos_nombres):
    datos_cursos.append({
        "id": str(idx + 1),
        "Nombre": nombre,
        "Codigo": codigo,
        "Docente": docente,
        "Creditos": creditos,
        "Alumnos_Inscritos": random.randint(15, 30)
    })

with open("c:/Users/carol/cesde_ntp_EDA/datos_mockapi_cursos.json", "w", encoding="utf-8") as f:
    json.dump(datos_cursos, f, indent=2, ensure_ascii=False)

# 2. GENERAR CALIFICACIONES (1 por estudiante)
datos_calificaciones = []
for idx, nombre in enumerate(nombres_estudiantes):
    curso_elegido = random.choice(datos_cursos)
    nota_parcial = round(random.uniform(1.5, 5.0), 1)
    # Nota final correlacionada con la parcial
    nota_final = round(min(5.0, max(0.0, nota_parcial + random.uniform(-0.6, 0.8))), 1)
    resultado = "Aprobado" if nota_final >= 3.0 else "Reprobado"
    
    datos_calificaciones.append({
        "id": str(idx + 1),
        "Estudiante": nombre,
        "Curso": curso_elegido["Nombre"],
        "Docente": curso_elegido["Docente"],
        "Nota_Parcial": nota_parcial,
        "Nota_Final": nota_final,
        "Resultado": resultado
    })

with open("c:/Users/carol/cesde_ntp_EDA/datos_mockapi_calificaciones.json", "w", encoding="utf-8") as f:
    json.dump(datos_calificaciones, f, indent=2, ensure_ascii=False)

# 3. GENERAR INSCRIPCIONES (1 por estudiante)
datos_inscripciones = []
for idx, nombre in enumerate(nombres_estudiantes):
    curso_elegido = random.choice(datos_cursos)
    progreso = random.randint(30, 100)
    fecha = f"2026-02-{random.randint(1, 28):02d}"
    
    datos_inscripciones.append({
        "id": str(idx + 1),
        "Estudiante": nombre,
        "Curso": curso_elegido["Nombre"],
        "Fecha_Inscripcion": fecha,
        "Progreso": progreso
    })

with open("c:/Users/carol/cesde_ntp_EDA/datos_mockapi_inscripciones.json", "w", encoding="utf-8") as f:
    json.dump(datos_inscripciones, f, indent=2, ensure_ascii=False)

print("¡Archivos generados con éxito!")
