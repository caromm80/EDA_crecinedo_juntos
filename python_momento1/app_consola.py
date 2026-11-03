"""
=============================================================================
PROYECTO: Diario de Gratitud y Estado de Ánimo (Mood Tracker) - Lumi
MOMENTO 1: Aplicación Interactiva en Consola (Estructuras de Datos y Funciones)
RAMA: feature/aprueba
=============================================================================
Requerimientos cumplidos:
1. Menú interactivo continuo utilizando ciclo while con opciones claras.
2. Uso de Listas (historial en memoria) y Diccionarios (cada registro individual).
3. Separación de lógica modular en funciones específicas (def registrar_..., def calcular_...).
4. Módulo de evaluación de estados aprobados (días positivos vs días de apapacho)
   y filtrado por emoción.
5. Validaciones robustas ante entradas erróneas del usuario (try/except, rangos).
=============================================================================
"""

import datetime
import sys

# Asegurar codificación UTF-8 en consolas Windows (cp1252)
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# --- Estructura de Datos Inicial (Lista de Diccionarios) ---
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
    },
    {
        "id": 5,
        "usuario": "Andrés",
        "fecha": "2026-11-03",
        "nivel_animo": 1,
        "emocion": "Desanimado",
        "gratitud": "Por haber tenido un momento de silencio para respirar.",
        "aprobado_dia_positivo": False
    }
]


def mostrar_banner():
    """Imprime el encabezado artístico y amigable de Lumi el monstruito de la gratitud."""
    print("=" * 70)
    print("   🌟 DIARIO DE GRATITUD Y ESTADO DE ÁNIMO - LUMI (MOOD TRACKER) 🌟   ")
    print("=" * 70)
    print("          (\\__/)  ")
    print("          (•ㅅ•)  ¡Hola! Soy Lumi, tu monstrico guardián del bienestar.")
    print("         / づ♥づ   Recuerda: agradecer transforma los días comunes.")
    print("=" * 70)


def registrar_ingreso(registros):
    """
    Solicita datos al usuario y almacena un nuevo registro como diccionario en la lista.
    """
    print("\n📝 --- REGISTRAR NUEVA ENTRADA EN EL DIARIO ---")
    
    usuario = input("👉 Ingresa tu nombre: ").strip()
    while not usuario:
        print("⚠️ El nombre no puede estar vacío.")
        usuario = input("👉 Ingresa tu nombre: ").strip()

    while True:
        try:
            animo = int(input("👉 ¿Cómo te sientes hoy? (Escala 1 al 5, donde 5 es Excelente): "))
            if 1 <= animo <= 5:
                break
            else:
                print("⚠️ Por favor ingresa un número entero entre 1 y 5.")
        except ValueError:
            print("⚠️ Entrada inválida. Debes ingresar un número entero.")

    emociones_guia = {
        1: "Desanimado",
        2: "Pensativo",
        3: "Estable",
        4: "Calmado",
        5: "Radiante"
    }
    emocion_sugerida = emociones_guia.get(animo, "Estable")
    print(f"✨ Emoción detectada: [{emocion_sugerida}]")

    gratitud = input("🌸 Escribe al menos una cosa por la que estés agradecido(a) hoy: ").strip()
    while not gratitud:
        print("⚠️ No olvides escribir tu motivo de gratitud; es fundamental para tu bienestar.")
        gratitud = input("🌸 ¿Por qué estás agradecido(a) hoy?: ").strip()

    fecha_hoy = datetime.date.today().strftime("%Y-%m-%d")
    nuevo_id = len(registros) + 1
    # Criterio de aprobación: ánimo >= 3 se considera día satisfactorio/positivo
    es_aprobado = animo >= 3

    nueva_entrada = {
        "id": nuevo_id,
        "usuario": usuario.capitalize(),
        "fecha": fecha_hoy,
        "nivel_animo": animo,
        "emocion": emocion_sugerida,
        "gratitud": gratitud,
        "aprobado_dia_positivo": es_aprobado
    }

    registros.append(nueva_entrada)
    print(f"\n✅ ¡Entrada guardada con éxito! (ID asignado: #{nuevo_id})")
    if es_aprobado:
        print(f"🎉 Lumi dice: ¡Excelente, un día positivo registrado para {usuario.capitalize()}!")
    else:
        print(f"💙 Lumi te manda un abrazo cálido. Mañana será una nueva oportunidad.")


def mostrar_todas_las_entradas(registros):
    """Muestra todas las entradas guardadas en memoria en formato de tabla limpia."""
    print("\n📖 --- HISTORIAL DE ENTRADAS REGISTRADAS ---")
    if not registros:
        print("ℹ️ Aún no hay entradas registradas.")
        return

    print(f"{'ID':<4} | {'Fecha':<10} | {'Usuario':<12} | {'Ánimo':<6} | {'Estado':<12} | {'Gratitud'}")
    print("-" * 85)
    for r in registros:
        estado_str = "Aprobado ⭐" if r["aprobado_dia_positivo"] else "Por Cuidar 💙"
        print(f"#{r['id']:<3} | {r['fecha']:<10} | {r['usuario']:<12} | {r['nivel_animo']}/5    | {estado_str:<12} | {r['gratitud']}")
    print("-" * 85)
    print(f"Total de registros: {len(registros)}\n")


def calcular_promedio_animo(registros):
    """Calcula promedios de ánimo globales e individuales."""
    print("\n📊 --- REPORTE DE PROMEDIOS DE ESTADO DE ÁNIMO ---")
    if not registros:
        print("⚠️ No hay suficientes datos para calcular promedios.")
        return 0.0

    suma_general = sum(r["nivel_animo"] for r in registros)
    promedio_general = suma_general / len(registros)

    print(f"📈 Promedio General de Ánimo: {promedio_general:.2f} / 5.0")
    
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


def evaluar_dias_aprobados(registros):
    """
    Función de evaluación de aprobación emocional (feature/aprueba):
    Calcula cuántos registros cumplen con la condición de 'Día Aprobado' (ánimo >= 3)
    y el porcentaje de satisfacción general.
    """
    print("\n⭐ --- EVALUACIÓN DE DÍAS APROBADOS (BIENESTAR EMOCIONAL) ---")
    if not registros:
        print("⚠️ No hay registros para evaluar.")
        return

    aprobados = [r for r in registros if r["aprobado_dia_positivo"]]
    no_aprobados = [r for r in registros if not r["aprobado_dia_positivo"]]
    total = len(registros)
    tasa_aprobacion = (len(aprobados) / total) * 100

    print(f"Total de días evaluados: {total}")
    print(f"✅ Días Positivos / Aprobados (Ánimo >= 3): {len(aprobados)} ({tasa_aprobacion:.1f}%)")
    print(f"💙 Días para Autocuidado / Apapacho (Ánimo < 3): {len(no_aprobados)} ({100 - tasa_aprobacion:.1f}%)")
    
    print("\n📋 Listado de Días Aprobados (Bienestar Óptimo):")
    for r in aprobados:
        print(f"  • [ID #{r['id']}] {r['usuario']} el {r['fecha']} (Ánimo {r['nivel_animo']}/5) -> \"{r['gratitud']}\"")

    if tasa_aprobacion >= 70:
        print("\n🎉 Mensaje de Lumi: ¡Tu comunidad tiene un índice de bienestar sobresaliente! Sigan así.")
    else:
        print("\n🤗 Mensaje de Lumi: Hay días difíciles, pero cada momento de gratitud cuenta. ¡Abrazo grupal!")


def filtrar_por_emocion(registros):
    """Permite filtrar entradas específicas por palabra clave en la emoción o gratitud."""
    print("\n🔍 --- FILTRAR ENTRADAS POR PALABRA CLAVE ---")
    filtro = input("👉 Ingresa la emoción o palabra a buscar (ej: Radiante, Calmado, familia): ").strip().lower()
    
    resultados = [
        r for r in registros 
        if filtro in r["emocion"].lower() or filtro in r["gratitud"].lower() or filtro in r["usuario"].lower()
    ]
    
    if not resultados:
        print(f"ℹ️ No se encontraron coincidencias para '{filtro}'.")
        return
        
    print(f"\nSe encontraron {len(resultados)} resultado(s):")
    for r in resultados:
        print(f"  • #{r['id']} | {r['usuario']} ({r['fecha']}) - Ánimo {r['nivel_animo']}/5 [{r['emocion']}]: {r['gratitud']}")


def menu_principal():
    """Bucle interactivo principal con opciones completas de los requerimientos."""
    mostrar_banner()
    
    while True:
        print("\n🎛️  --- MENÚ PRINCIPAL ---")
        print("1. 📝 Registrar Nueva Entrada (Ánimo & Gratitud)")
        print("2. 📖 Ver Todas las Entradas Registradas")
        print("3. 📊 Ver Promedio y Estadísticas de Ánimo")
        print("4. ⭐ Evaluar Días Aprobados (Métrica de Bienestar)")
        print("5. 🔍 Filtrar Entradas por Emoción o Palabra Clave")
        print("6. 🚪 Salir")
        
        opcion = input("👉 Selecciona una opción (1-6): ").strip()
        
        if opcion == "1":
            registrar_ingreso(registros_diario)
        elif opcion == "2":
            mostrar_todas_las_entradas(registros_diario)
        elif opcion == "3":
            calcular_promedio_animo(registros_diario)
        elif opcion == "4":
            evaluar_dias_aprobados(registros_diario)
        elif opcion == "5":
            filtrar_por_emocion(registros_diario)
        elif opcion == "6":
            print("\n👋 ¡Gracias por usar Lumi Mood Tracker! Recuerda agradecer cada día. ¡Hasta pronto!")
            break
        else:
            print("⚠️ Opción no válida. Por favor digita un número del 1 al 6.")


if __name__ == "__main__":
    menu_principal()
