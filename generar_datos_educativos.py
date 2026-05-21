import pandas as pd
import random

# Semilla para que los datos siempre sean los mismos al generar
random.seed(42)

nombres_m = ["Juan", "Carlos", "Luis", "Pedro", "Diego", "Andrés", "Mateo", "Santiago", "Sebastián", "Daniel", "Felipe", "Alejandro", "Nicolás", "David", "José", "Manuel"]
nombres_f = ["María", "Ana", "Sofía", "Laura", "Paula", "Camila", "Valeria", "Isabella", "Gabriela", "Mariana", "Valentina", "Daniela", "Sara", "Andrea", "Natalia", "Lucía"]
apellidos = ["Pérez", "Gómez", "Ruiz", "Martínez", "Hernández", "Díaz", "Álvarez", "Torres", "Ramos", "Castro", "Rodríguez", "López", "González", "Sánchez", "Ramírez", "Muñoz"]
ciudades = ["Bogotá", "Medellín", "Cali", "Barranquilla", "Bucaramanga", "Pereira", "Manizales", "Cartagena"]
generos = ["M", "F"]

data = []
for i in range(1, 101):
    genero = random.choice(generos)
    nombre = random.choice(nombres_m if genero == "M" else nombres_f) + " " + random.choice(apellidos)
    edad = random.randint(17, 28)
    ciudad = random.choice(ciudades)
    estrato = random.choice([1, 2, 3, 4])
    
    # Simular correlación: Mayor asistencia tiende a dar mejor promedio académico
    asistencia = round(random.uniform(70, 100), 1)
    if asistencia > 90:
        promedio = round(random.uniform(3.8, 5.0), 2)
    elif asistencia > 80:
        promedio = round(random.uniform(3.0, 4.2), 2)
    else:
        promedio = round(random.uniform(1.8, 3.2), 2)
        
    # Asignar estado según rendimiento
    if promedio < 3.0:
        estado = "En Riesgo"
    elif edad >= 24 and promedio >= 4.0:
        estado = "Egresado"
    else:
        estado = "Activo"
        
    materias = random.randint(3, 6)
    creditos = materias * 3
    
    data.append({
        "ID": i,
        "Nombre": nombre,
        "Edad": edad,
        "Genero": genero,
        "Ciudad": ciudad,
        "Promedio": promedio,
        "Estado": estado,
        "Materias_Inscritas": materias,
        "Creditos_Aprobados": creditos if estado != "En Riesgo" else int(creditos * 0.6),
        "Estrato": estrato,
        "Asistencia_%": asistencia
    })

# Convertir a DataFrame y guardar como archivo CSV
df = pd.DataFrame(data)
df.to_csv("estudiantes_creciendo_juntos.csv", index=False)
print("¡Archivo CSV 'estudiantes_creciendo_juntos.csv' generado correctamente con 100 registros!")
