"""
=============================================================================
PROYECTO: Diario de Gratitud y Estado de Ánimo (Mood Tracker) - Lumi
MOMENTO 2: Módulo de Limpieza y Preprocesamiento de Datos (data_cleaner.py)
=============================================================================
Este módulo contiene funciones reutilizables diseñadas para:
1. Carga segura de archivos CSV en DataFrames de Pandas.
2. Detección y tratamiento de valores nulos (imputación con promedio/moda o descarte controlado).
3. Estandarización de cadenas de texto (minúsculas, trim de espacios en blanco, corrección de formato).
4. Limpieza específica del proyecto (eliminación de símbolos especiales '$', '%', 'pts'
   y casteo seguro a tipos numéricos).
=============================================================================
"""

import os
import pandas as pd
import numpy as np


def cargar_datos(ruta_archivo: str) -> pd.DataFrame:
    """
    Función requerida 1: Carga un archivo CSV en un DataFrame de Pandas.
    Valida la existencia del archivo y gestiona posibles errores de lectura.
    
    :param ruta_archivo: Ruta relativa o absoluta del archivo CSV.
    :return: pd.DataFrame con los datos leídos.
    """
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"❌ Error: El archivo no existe en la ruta: {ruta_archivo}")
    
    try:
        df = pd.read_csv(ruta_archivo, encoding='utf-8')
        print(f"✅ Archivo cargado exitosamente: {os.path.basename(ruta_archivo)} ({len(df)} filas, {len(df.columns)} columnas)")
        return df
    except Exception as e:
        raise IOError(f"❌ Error al leer el archivo {ruta_archivo}: {e}")


def manejar_valores_nulos(df: pd.DataFrame, estrategia: str = "auto") -> pd.DataFrame:
    """
    Función requerida 2: Detecta y maneja valores nulos en el DataFrame.
    
    Estrategias:
    - 'auto': Imputa columnas numéricas con la mediana/promedio y columnas de texto
              con la moda o categoría representativa.
    - 'eliminar': Elimina cualquier fila que contenga valores nulos.
    
    :param df: DataFrame de entrada.
    :param estrategia: 'auto' o 'eliminar'.
    :return: DataFrame limpio sin valores nulos.
    """
    df_limpio = df.copy()
    # Reemplazar cadenas vacías, 'nan' o espacios en blanco por np.nan genuino
    df_limpio = df_limpio.replace(r'^\s*$', np.nan, regex=True).replace('nan', np.nan)
    
    conteo_nulos_inicial = df_limpio.isnull().sum().to_dict()
    columnas_con_nulos = {col: n for col, n in conteo_nulos_inicial.items() if n > 0}
    
    if not columnas_con_nulos:
        print("ℹ️ No se detectaron valores nulos en el dataset.")
        return df_limpio

    print(f"🔍 Columnas con valores nulos detectadas: {columnas_con_nulos}")

    if estrategia == "eliminar":
        filas_antes = len(df_limpio)
        df_limpio = df_limpio.dropna()
        print(f"🗑️ Se eliminaron {filas_antes - len(df_limpio)} filas con valores nulos.")
        return df_limpio

    # Estrategia 'auto': Imputación inteligente
    for columna in df_limpio.columns:
        if df_limpio[columna].isnull().any():
            # Si la columna es numérica o convertible a numérica
            if pd.api.types.is_numeric_dtype(df_limpio[columna]):
                mediana_val = df_limpio[columna].median()
                df_limpio[columna] = df_limpio[columna].fillna(mediana_val)
                print(f"  • Imputado valor nulo en '{columna}' con la mediana: {mediana_val:.1f}")
            else:
                # Si la columna es de texto/categórica
                valores_validos = df_limpio[columna].dropna()
                if not valores_validos.empty:
                    moda_val = valores_validos.mode()[0]
                    df_limpio[columna] = df_limpio[columna].fillna(moda_val)
                    print(f"  • Imputado valor nulo en '{columna}' con la moda: '{moda_val}'")
                else:
                    df_limpio[columna] = df_limpio[columna].fillna("no_especificado")

    return df_limpio


def estandarizar_texto(df: pd.DataFrame, columnas: list) -> pd.DataFrame:
    """
    Función requerida 3: Estandariza columnas de texto:
    - Convierte a minúsculas uniformes.
    - Elimina espacios en blanco sobrantes al inicio y al final (.strip()).
    - Reemplaza múltiples espacios internos continuos por uno solo.
    
    :param df: DataFrame de entrada.
    :param columnas: Lista de nombres de columnas a estandarizar.
    :return: DataFrame con las columnas textuales normalizadas.
    """
    df_limpio = df.copy()
    for col in columnas:
        if col in df_limpio.columns:
            # Convertir a string, pasar a minúsculas, limpiar espacios en los extremos y dobles espacios
            df_limpio[col] = (
                df_limpio[col]
                .astype(str)
                .str.lower()
                .str.strip()
                .str.replace(r'\s+', ' ', regex=True)
            )
            print(f"  ✨ Columna textual estandarizada (minúsculas y trim): '{col}'")
        else:
            print(f"  ⚠️ Advertencia: Columna '{col}' no encontrada en el DataFrame.")
    return df_limpio


def limpieza_especifica_proyecto(df: pd.DataFrame) -> pd.DataFrame:
    """
    Función requerida 4: Limpieza específica del proyecto de Gratitud y Mood Tracker:
    - En 'registros_gratitud.csv': Limpia la columna 'nivel_energia' que viene con
      símbolos de moneda '$', porcentaje '%' o sufijos 'pts' (ej: '$85%', '75pts'),
      extrayendo únicamente el valor numérico y convirtiéndolo a tipo float.
    - Asegura que 'nivel_animo' esté casteado a entero (int) sin espacios.
    - Convierte la columna 'fecha' a formato datetime.
    
    :param df: DataFrame de entrada.
    :return: DataFrame con los tipos de datos y formatos corregidos.
    """
    df_limpio = df.copy()
    
    # Limpieza específica de 'nivel_energia'
    if 'nivel_energia' in df_limpio.columns:
        print("  🧹 Aplicando limpieza específica en 'nivel_energia' (removiendo '$', '%', 'pts')...")
        # Remover caracteres no numéricos excepto puntos decimales
        df_limpio['nivel_energia'] = (
            df_limpio['nivel_energia']
            .astype(str)
            .str.replace('$', '', regex=False)
            .str.replace('%', '', regex=False)
            .str.replace('pts', '', regex=False)
            .str.strip()
        )
        df_limpio['nivel_energia'] = pd.to_numeric(df_limpio['nivel_energia'], errors='coerce')
        # Si quedó algún nulo por casteo, imputar con 70.0 (promedio saludable)
        df_limpio['nivel_energia'] = df_limpio['nivel_energia'].fillna(70.0)

    # Limpieza específica de 'nivel_animo'
    if 'nivel_animo' in df_limpio.columns:
        df_limpio['nivel_animo'] = (
            df_limpio['nivel_animo']
            .astype(str)
            .str.strip()
        )
        df_limpio['nivel_animo'] = pd.to_numeric(df_limpio['nivel_animo'], errors='coerce').fillna(3).astype(int)

    # Conversión de 'fecha'
    if 'fecha' in df_limpio.columns:
        df_limpio['fecha'] = pd.to_datetime(df_limpio['fecha'], errors='coerce')

    # Conversión de 'fecha_registro'
    if 'fecha_registro' in df_limpio.columns:
        df_limpio['fecha_registro'] = pd.to_datetime(df_limpio['fecha_registro'], errors='coerce')

    return df_limpio
