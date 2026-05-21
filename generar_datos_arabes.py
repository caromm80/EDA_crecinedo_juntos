import pandas as pd
import random

# Seed para consistencia
random.seed(99)

# Nombres árabes muy tradicionales y hermosos (Masculino y Femenino)
nombres_m = ["Youssef Al-Fayed", "Amir El-Amin", "Zayd Ibn-Harith", "Omar Al-Khattab", "Tareq Bin-Ziyad", 
             "Mustafa Al-Hassan", "Karim Al-Mansour", "Hassan El-Saad", "Ali Ben-Youssef", "Farid Al-Farsi",
             "Ziad Al-Ghazali", "Rami El-Khoury", "Hamza Al-Sayed", "Idris Al-Hadi", "Samir Al-Jamil"]

nombres_f = ["Fatima Al-Zahra", "Layla Bint-Khalid", "Mariam Al-Mansour", "Aisha Al-Hassan", "Yasmin Al-Farsi",
             "Salma Al-Otaibi", "Rania Al-Abdullah", "Noor Al-Huda", "Amira El-Fadhel", "Habiba Al-Masri",
             "Khadija El-Shamy", "Basma Al-Taji", "Farida Al-Sabah", "Zainab Al-Harbi", "Hala Al-Rashed"]

ciudades_arabes = ["Dubái", "El Cairo", "Riad", "Doha", "Abu Dabi", "Amán", "Casablanca", "Mascate"]

cursos_arabes = [
    ("Ciencia de Datos Aplicada", "CD501", "Dr. Yasser Al-Mansoori", 4),
    ("Inteligencia Artificial Avanzada", "IA502", "Dra. Fatma Al-Saeed", 4),
    ("Machine Learning y Modelos", "ML503", "Dr. Hisham Al-Ghamdi", 3),
    ("Visualización e Historias de Datos", "VD504", "Ing. Rania El-Sherbiny", 3),
    ("Bases de Datos NoSQL y Cloud", "BD505", "Dr. Khaled Al-Mutairi", 4)
]

# 1. GENERAR ESTUDIANTES ÁRABES (30 registros)
datos_estudiantes = []
for i in range(1, 31):
    genero = "Masculino" if i % 2 == 0 else "Femenino"
    nombre = random.choice(nombres_m if genero == "Masculino" else nombres_f)
    # Evitar nombres repetidos
    nombres_m = [n for n in nombres_m if n != nombre]
    nombres_f = [n for n in nombres_f if n != nombre]
    
    edad = random.randint(18, 29)
    ciudad = random.choice(ciudades_arabes)
    promedio = round(random.uniform(2.5, 5.0), 2)
    
    if promedio < 3.0:
        estado = "En Riesgo"
    elif edad >= 25 and promedio >= 4.2:
        estado = "Egresado"
    else:
        estado = "Activo"
        
    materias = random.randint(3, 8)
    creditos = random.randint(12, 90)
    estrato = random.randint(1, 4)
    asistencia = random.randint(75, 100)
    
    datos_estudiantes.append({
        "id": i,
        "Nombre": nombre,
        "Edad": edad,
        "Genero": genero,
        "Ciudad": ciudad,
        "Promedio": promedio,
        "Estado": estado,
        "Materias_Inscritas": materias,
        "Creditos_Aprobados": creditos,
        "Estrato": estrato,
        "Asistencia": asistencia
    })

df_estudiantes = pd.DataFrame(datos_estudiantes)
df_estudiantes.to_csv("c:/Users/carol/cesde_ntp_EDA/datos_hoja_estudiantes.csv", index=False, encoding="utf-8")

# 2. GENERAR CURSOS ÁRABES
datos_cursos = []
for idx, (nombre, codigo, docente, creditos) in enumerate(cursos_arabes):
    datos_cursos.append({
        "ID": 501 + idx,
        "Nombre": nombre,
        "Código": codigo,
        "Docente": docente,
        "Créditos": creditos,
        "Alumnos_Inscritos": random.randint(10, 25)
    })

df_cursos = pd.DataFrame(datos_cursos)
df_cursos.to_csv("c:/Users/carol/cesde_ntp_EDA/datos_hoja_cursos.csv", index=False, encoding="utf-8")

# 3. GENERAR CALIFICACIONES ÁRABES
datos_calificaciones = []
for idx, est in enumerate(datos_estudiantes):
    curso = random.choice(datos_cursos)
    nota_parcial = round(random.uniform(2.0, 5.0), 1)
    nota_final = round(min(5.0, max(0.0, nota_parcial + random.uniform(-0.5, 0.7))), 1)
    resultado = "Aprobado" if nota_final >= 3.0 else "Reprobado"
    
    datos_calificaciones.append({
        "ID": idx + 1,
        "Estudiante": est["Nombre"],
        "Curso": curso["Nombre"],
        "Docente": curso["Docente"],
        "Nota_Parcial": nota_parcial,
        "Nota_Final": nota_final,
        "Resultado": resultado
    })

df_calificaciones = pd.DataFrame(datos_calificaciones)
df_calificaciones.to_csv("c:/Users/carol/cesde_ntp_EDA/datos_hoja_calificaciones.csv", index=False, encoding="utf-8")

# 4. GENERAR INSCRIPCIONES ÁRABES
datos_inscripciones = []
for idx, est in enumerate(datos_estudiantes):
    curso = random.choice(datos_cursos)
    progreso = random.randint(40, 100)
    fecha = f"2026-03-{random.randint(1, 28):02d}"
    
    datos_inscripciones.append({
        "ID": idx + 1,
        "Estudiante": est["Nombre"],
        "Curso": curso["Nombre"],
        "Fecha_Inscripcion": fecha,
        "Progreso_%": progreso
    })

df_inscripciones = pd.DataFrame(datos_inscripciones)
df_inscripciones.to_csv("c:/Users/carol/cesde_ntp_EDA/datos_hoja_inscripciones.csv", index=False, encoding="utf-8")

print("¡Datos árabes generados con éxito!")
