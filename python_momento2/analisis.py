"""
=============================================================================
PROYECTO: Diario de Gratitud y Estado de Ánimo (Mood Tracker) - Lumi
MOMENTO 2: Script Principal de Análisis Exploratorio de Datos (analisis.py)
=============================================================================
Este script ejecuta el flujo completo de análisis:
1. Carga de los 2 datasets relacionados desde la carpeta 'data/'.
2. Preprocesamiento y limpieza utilizando las funciones de 'data_cleaner.py'.
3. Combinación (merge) de las tablas de Usuarios y Registros de Gratitud.
4. Operaciones analíticas con Pandas:
   - Frecuencia
   - Agregación (groupby)
   - Filtrado y Conteo
5. Respuestas detalladas e impresas en consola a las preguntas clave del proyecto.
=============================================================================
"""

import os
import sys
import pandas as pd

# Asegurar codificación UTF-8 en consolas Windows (cp1252)
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# Asegurar importación del módulo de limpieza hermano
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from data_cleaner import (
    cargar_datos,
    manejar_valores_nulos,
    estandarizar_texto,
    limpieza_especifica_proyecto
)


def banner_analisis():
    print("=" * 76)
    print("   📊 SCRIPT DE ANÁLISIS DE DATOS - LUMI MOOD & GRATITUDE TRACKER 📊   ")
    print("=" * 76)
    print("           (\\__/)  ")
    print("           (•ㅅ•)  ¡Hola! Soy Lumi. Vamos a inspeccionar los datos")
    print("          / づ📊づ  de bienestar de nuestra comunidad con Pandas.")
    print("=" * 76)


def ejecutar_analisis():
    banner_analisis()

    # --- PASO 1: Rutas de los archivos ---
    base_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_usuarios = os.path.join(base_dir, "..", "data", "usuarios_mood.csv")
    ruta_gratitud = os.path.join(base_dir, "..", "data", "registros_gratitud.csv")

    print("\n📂 [PASO 1/4] Carga de datasets con 'cargar_datos'...")
    df_usuarios_raw = cargar_datos(ruta_usuarios)
    df_gratitud_raw = cargar_datos(ruta_gratitud)

    # --- PASO 2: Limpieza y Normalización ---
    print("\n🧹 [PASO 2/4] Preprocesamiento y limpieza de datos...")
    
    print("\n--- Limpiando Dataset de Usuarios ---")
    df_usuarios = estandarizar_texto(df_usuarios_raw, columnas=['ciudad', 'categoria_ocupacion'])
    df_usuarios = manejar_valores_nulos(df_usuarios, estrategia="auto")
    df_usuarios = limpieza_especifica_proyecto(df_usuarios)

    print("\n--- Limpiando Dataset de Registros de Gratitud ---")
    df_gratitud = estandarizar_texto(df_gratitud_raw, columnas=['emocion_principal'])
    df_gratitud = limpieza_especifica_proyecto(df_gratitud)
    df_gratitud = manejar_valores_nulos(df_gratitud, estrategia="auto")

    # --- PASO 3: Combinación de Datos (Merge) ---
    print("\n🔗 [PASO 3/4] Combinación de tablas (pd.merge por 'id_usuario')...")
    df_unificado = pd.merge(
        left=df_gratitud,
        right=df_usuarios,
        on="id_usuario",
        how="inner"
    )
    print(f"✅ Merge completado: {len(df_unificado)} registros combinados con {len(df_unificado.columns)} columnas.")
    print("Columnas combinadas:", list(df_unificado.columns))

    # --- PASO 4: Respuestas a las Preguntas Clave ---
    print("\n" + "=" * 76)
    print("                   🎯 RESPUESTAS A LAS PREGUNTAS CLAVE 🎯                   ")
    print("=" * 76)

    # -------------------------------------------------------------------------
    # PREGUNTA 1: Análisis de Frecuencia
    # ¿Cuál es el elemento (usuario) con la mayor cantidad de registros en los datos?
    # -------------------------------------------------------------------------
    print("\n📌 PREGUNTA 1: ANÁLISIS DE FRECUENCIA")
    print("❓ ¿Cuál es el usuario con la mayor cantidad de registros de gratitud en la plataforma?")
    
    conteo_por_usuario = df_unificado.groupby(['id_usuario', 'nombre_completo']).size().reset_index(name='total_entradas')
    usuario_top = conteo_por_usuario.sort_values(by='total_entradas', ascending=False).iloc[0]

    print("-" * 76)
    print(f"🥇 Usuario Líder en Gratitud:  {usuario_top['nombre_completo']} (ID: #{usuario_top['id_usuario']})")
    print(f"📦 Total de Entradas Registradas: {usuario_top['total_entradas']} registros")
    print("\nTop 5 Usuarios con más entradas registradas:")
    top_5 = conteo_por_usuario.sort_values(by='total_entradas', ascending=False).head(5)
    for idx, (_, fila) in enumerate(top_5.iterrows(), start=1):
        print(f"  {idx}. {fila['nombre_completo']:<22} | ID: #{fila['id_usuario']:<3} | {fila['total_entradas']} entradas")
    print("-" * 76)

    # -------------------------------------------------------------------------
    # PREGUNTA 2: Análisis de Agregación (groupby)
    # Calcular una métrica clave agrupada por una categoría.
    # -------------------------------------------------------------------------
    print("\n📌 PREGUNTA 2: ANÁLISIS DE AGREGACIÓN (GROUPBY)")
    print("❓ ¿Cuál es el promedio del estado de ánimo y horas de sueño agrupado por categoría de ocupación?")
    print("-" * 76)

    agregacion_ocupacion = df_unificado.groupby('categoria_ocupacion').agg(
        total_registros=('id_registro', 'count'),
        promedio_animo=('nivel_animo', 'mean'),
        promedio_sueno=('horas_sueno', 'mean'),
        energia_media=('nivel_energia', 'mean')
    ).reset_index()

    agregacion_ocupacion = agregacion_ocupacion.sort_values(by='promedio_animo', ascending=False)
    
    print(f"{'Ocupación':<16} | {'Registros':<10} | {'Ánimo Promedio':<15} | {'Sueño Promedio (h)':<18} | {'Energía %'}")
    print("-" * 76)
    for _, fila in agregacion_ocupacion.iterrows():
        print(f"{fila['categoria_ocupacion']:<16} | {fila['total_registros']:<10} | {fila['promedio_animo']:.2f} / 5.0        | {fila['promedio_sueno']:.1f} hrs            | {fila['energia_media']:.1f}%")
    print("-" * 76)

    # -------------------------------------------------------------------------
    # PREGUNTA 3: Análisis con Filtrado y Conteo
    # Segmentar los datos y contar cuántos elementos cumplen una condición específica.
    # -------------------------------------------------------------------------
    print("\n📌 PREGUNTA 3: ANÁLISIS CON FILTRADO Y CONTEO")
    print("❓ ¿Cuántos registros corresponden a 'Días Óptimos de Alto Bienestar'?")
    print("   (Condición: Nivel de Ánimo >= 4 Y Horas de Sueño >= 7.0 horas)")
    print("-" * 76)

    # Operación booleana de filtrado
    filtro_alto_bienestar = (df_unificado['nivel_animo'] >= 4) & (df_unificado['horas_sueno'] >= 7.0)
    df_filtrado = df_unificado[filtro_alto_bienestar]
    
    total_total = len(df_unificado)
    total_cumplen = len(df_filtrado)
    porcentaje = (total_cumplen / total_total) * 100

    print(f"✨ Total de registros que CUMPLEN la condición: {total_cumplen} de {total_total} ({porcentaje:.1f}%)")
    print("\nMuestra de registros destacados que cumplen la condición:")
    for _, r in df_filtrado.head(4).iterrows():
        print(f"  • {r['nombre_completo']:<20} | Ánimo: {r['nivel_animo']}/5 | Sueño: {r['horas_sueno']}h | Gratitud: \"{r['motivo_gratitud']}\"")
    print("-" * 76)

    print("\n🎉 ¡Análisis completado exitosamente sin errores!")
    print("🐾 Lumi dice: ¡Los datos demuestran que dormir bien y agradecer potencian el ánimo!")


if __name__ == "__main__":
    ejecutar_analisis()
