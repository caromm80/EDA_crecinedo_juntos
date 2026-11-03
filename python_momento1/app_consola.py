"""
=============================================================================
PROYECTO: Diario de Gratitud y Estado de Ánimo (Mood Tracker) - Lumi
MOMENTO 1: Aplicación Interactiva en Consola (Estructuras de Datos y Funciones)
=============================================================================
Requerimientos cumplidos:
1. Menú interactivo continuo utilizando ciclo while con opciones claras.
2. Uso de Listas (historial en memoria) y Diccionarios (cada registro individual).
3. Separación de lógica modular en funciones específicas (def registrar_..., def calcular_...).
4. Validaciones ante entradas erróneas del usuario (try/except, verificación de rangos).
=============================================================================
"""

import datetime

# --- Estructura de Datos Inicial (Lista de Diccionarios) ---
# Pre-cargamos algunos registros representativos para que el docente pueda probar de inmediato
# las funciones de visualización y promedios sin tener que escribir todo desde cero.
registros_diario = [
    {
        "id": 1,
        "usuario": "Carolina",
        "fecha": "2026-11-01",
        "nivel_animo": 5,
        "emocion": "Radiante",
        "gratitud": "Agradecida por el apoyo incondicional de mi familia en el semestre.",
        "aprobado_dia_positivo": True
    },
    {
        "id": 2,
        "usuario": "Mateo",
        "fecha": "2026-11-01",
        "nivel_animo": 4,
        "emocion": "Calmado",
        "gratitud": "Por una rica taza de café en la mañana y buen clima.",
        "aprobado_dia_positivo": True
    },
    {
        "id": 3,
        "usuario": "Valentina",
        "fecha": "2026-11-02",
        "nivel_animo": 2,
        "emocion": "Pensativo",
        "gratitud": "Por tener un techo seguro a pesar del cansancio del día.",
        "aprobado_dia_positivo": False
    },
    {
        "id": 4,
        "usuario": "Carolina",
        "fecha": "2026-11-02",
        "nivel_animo": 4,
        "emocion": "Motivado",
        "gratitud": "Avanzar en los proyectos de programación con mi equipo.",
        "aprobado_dia_positivo": True
    }
]


def mostrar_banner():
    """Imprime el encabezado artístico y amigable de Lumi el monstruito de la gratitud."""
    print("=" * 68)
    print("   🌟 DIARIO DE GRATITUD Y ESTADO DE ÁNIMO - LUMI (MOOD TRACKER) 🌟   ")
    print("=" * 68)
    print("          (\\__/)  ")
    print("          (•ㅅ•)  Hola, soy Lumi! Tu monstrico guardián del ánimo.")
    print("         / づ♥づ   Recuerda: agradecer transforma los días comunes.")
    print("=" * 68)


def registrar_ingreso(registros):
    """
    Solicita los datos al usuario y añade un nuevo diccionario a la lista de registros.
    Cumple con el requerimiento de registrar ingreso / datos usando diccionarios.
    """
    print("\n📝 --- REGISTRAR NUEVA ENTRADA EN EL DIARIO ---")
    
    usuario = input("👉 Ingresa tu nombre: ").strip()
    while not usuario:
        print("⚠️ El nombre no puede estar vacío.")
        usuario = input("👉 Ingresa tu nombre: ").strip()

    # Validación de escala del ánimo (1 al 5)
    while True:
        try:
            animo = int(input("👉 ¿Cómo te sientes hoy? (Escala 1 al 5, donde 5 es Excelente): "))
            if 1 <= animo <= 5:
                break
            else:
                print("⚠️ Por favor ingresa un número válido entre 1 y 5.")
        except ValueError:
            print("⚠️ Entrada inválida. Debes ingresar un número entero.")

    # Mapeo descriptivo según la calificación
    emociones_guia = {
        1: "Desanimado / Requiere Apapacho",
        2: "Pensativo / Cansado",
        3: "Neutro / Estable",
        4: "Calmado / Satisfecho",
        5: "Radiante / Muy Feliz"
    }
    emocion_sugerida = emociones_guia.get(animo, "Normal")
    print(f"✨ Emoción detectada: [{emocion_sugerida}]")

    gratitud = input("🌸 Escribe al menos una cosa por la que estés agradecido(a) hoy: ").strip()
    while not gratitud:
        print("⚠️ No olvides escribir tu motivo de gratitud; es el corazón del diario.")
        gratitud = input("🌸 ¿Por qué estás agradecido(a) hoy?: ").strip()

    fecha_hoy = datetime.date.today().strftime("%Y-%m-%d")
    nuevo_id = len(registros) + 1
    es_positivo = animo >= 3  # Criterio base de día positivo / aprobado

    # Construcción del diccionario del registro
    nueva_entrada = {
        "id": nuevo_id,
        "usuario": usuario.capitalize(),
        "fecha": fecha_hoy,
        "nivel_animo": animo,
        "emocion": emocion_sugerida,
        "gratitud": gratitud,
        "aprobado_dia_positivo": es_positivo
    }

    # Añadir a la lista en memoria
    registros.append(nueva_entrada)
    print(f"\n✅ ¡Entrada guardada con éxito! (ID asignado: #{nuevo_id})")
    print(f"🐾 Lumi dice: ¡Gracias {usuario.capitalize()} por cuidar tu bienestar emocional hoy!\n")


def mostrar_todas_las_entradas(registros):
    """Recorre la lista de registros e imprime cada diccionario en formato legible."""
    print("\n📖 --- HISTORIAL DE ENTRADAS REGISTRADAS ---")
    if not registros:
        print("ℹ️ Aún no hay entradas registradas en el diario.")
        return

    print(f"{'ID':<4} | {'Fecha':<10} | {'Usuario':<12} | {'Ánimo':<6} | {'Estado':<10} | {'Gratitud'}")
    print("-" * 80)
    for r in registros:
        estado_str = "Aprobado ⭐" if r["aprobado_dia_positivo"] else "Por Cuidar 💙"
        print(f"#{r['id']:<3} | {r['fecha']:<10} | {r['usuario']:<12} | {r['nivel_animo']}/5    | {estado_str:<10} | {r['gratitud']}")
    print("-" * 80)
    print(f"Total de registros: {len(registros)}\n")


def calcular_promedio_animo(registros):
    """
    Calcula el promedio general de ánimo y el promedio por usuario individual.
    Cumple con el requerimiento de cálculo de métricas/promedios.
    """
    print("\n📊 --- REPORTE DE PROMEDIOS DE ESTADO DE ÁNIMO ---")
    if not registros:
        print("⚠️ No hay suficientes datos para calcular promedios.")
        return 0.0

    suma_general = sum(r["nivel_animo"] for r in registros)
    promedio_general = suma_general / len(registros)

    print(f"📈 Promedio General de Ánimo: {promedio_general:.2f} / 5.0")
    
    # Cálculo agrupado por usuario usando un diccionario acumulador
    usuarios_metricas = {}
    for r in registros:
        u = r["usuario"]
        if u not in usuarios_metricas:
            usuarios_metricas[u] = {"suma": 0, "conteo": 0}
        usuarios_metricas[u]["suma"] += r["nivel_animo"]
        usuarios_metricas[u]["conteo"] += 1

    print("\n👤 Promedio Individual por Usuario:")
    print(f"{'Usuario':<15} | {'Registros':<10} | {'Promedio':<10}")
    print("-" * 42)
    for u, data in usuarios_metricas.items():
        prom_u = data["suma"] / data["conteo"]
        print(f"{u:<15} | {data['conteo']:<10} | {prom_u:.2f} / 5.0")
    print("-" * 42)
    return promedio_general


def menu_principal():
    """Bucle principal (while) de la aplicación de consola interactiva."""
    mostrar_banner()
    
    while True:
        print("\n🎛️  --- MENÚ PRINCIPAL ---")
        print("1. 📝 Registrar Nueva Entrada (Ánimo & Gratitud)")
        print("2. 📖 Ver Todas las Entradas Registradas")
        print("3. 📊 Ver Promedio y Estadísticas de Ánimo")
        print("4. 🚪 Salir")
        
        opcion = input("👉 Selecciona una opción (1-4): ").strip()
        
        if opcion == "1":
            registrar_ingreso(registros_diario)
        elif opcion == "2":
            mostrar_todas_las_entradas(registros_diario)
        elif opcion == "3":
            calcular_promedio_animo(registros_diario)
        elif opcion == "4":
            print("\n👋 ¡Gracias por usar Lumi Mood Tracker! Recuerda agradecer cada día. ¡Hasta pronto!")
            break
        else:
            print("⚠️ Opción no válida. Por favor digita un número del 1 al 4.")


if __name__ == "__main__":
    menu_principal()
