"""
Script de Verificación - Proyecto Integrador de Analítica

Este script verifica que todos los archivos y carpetas necesarios
estén presentes y correctamente configurados.
"""

import os
import sys

# Reconfigurar la codificación de la consola para evitar errores con emojis en Windows
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass # Para versiones de Python muy antiguas

def verificar_estructura():
    """Verifica la estructura del proyecto"""
    print("=" * 60)
    print("🔍 VERIFICACIÓN DEL PROYECTO: ANALÍTICA DE DATOS")
    print("=" * 60)
    
    archivos_requeridos = {
        "Inicio.py": "📄 Página de inicio",
        "requirements.txt": "📦 Dependencias Python",
        ".gitignore": "🚫 Archivo git ignore",
        "README.md": "📖 Documentación",
        "Desarrollos_de_software_20260319.csv": "📊 Dataset ejemplo"
    }
    
    carpetas_requeridas = {
        "pages": "📁 Carpeta de páginas"
    }
    
    archivos_paginas = {
        "pages/1_Análisis Exploratorio de Datos (EDA).py": "🔍 Módulo EDA",
        "pages/2_Resultados (EDA).py": "📝 Módulo de Resultados"
    }
    
    print("\n✅ ARCHIVOS REQUERIDOS:")
    print("-" * 60)
    archivos_ok = 0
    for archivo, descripcion in archivos_requeridos.items():
        existe = os.path.exists(archivo)
        estado = "✓" if existe else "✗"
        archivos_ok += existe
        print(f"{estado} {descripcion}: {archivo}")
    
    print("\n✅ CARPETAS REQUERIDAS:")
    print("-" * 60)
    carpetas_ok = 0
    for carpeta, descripcion in carpetas_requeridas.items():
        existe = os.path.isdir(carpeta)
        estado = "✓" if existe else "✗"
        carpetas_ok += existe
        print(f"{estado} {descripcion}: {carpeta}")
    
    print("\n✅ ARCHIVOS DE PÁGINAS:")
    print("-" * 60)
    paginas_ok = 0
    for archivo, descripcion in archivos_paginas.items():
        existe = os.path.exists(archivo)
        estado = "✓" if existe else "✗"
        paginas_ok += existe
        print(f"{estado} {descripcion}: {archivo}")
    
    print("\n" + "=" * 60)
    total_requeridos = len(archivos_requeridos) + len(carpetas_requeridas) + len(archivos_paginas)
    total_ok = archivos_ok + carpetas_ok + paginas_ok
    
    if total_ok == total_requeridos:
        print(f"✨ ¡ESTRUCTURA CORRECTA! ({total_ok}/{total_requeridos})")
        print("=" * 60)
        print("\n🚀 PRÓXIMOS PASOS:")
        print("-" * 60)
        print("1. Ejecuta: streamlit run Inicio.py")
        print("2. Abre tu navegador en: http://localhost:8501")
        print("3. Carga un archivo CSV para explorar")
        return True
    else:
        print(f"❌ ESTRUCTURA INCOMPLETA ({total_ok}/{total_requeridos})")
        print("=" * 60)
        print("\n⚠️  Archivos faltantes:")
        print("-" * 60)
        for archivo in archivos_requeridos.keys():
            if not os.path.exists(archivo):
                print(f"  - {archivo}")
        for carpeta in carpetas_requeridas.keys():
            if not os.path.isdir(carpeta):
                print(f"  - {carpeta}/")
        for archivo in archivos_paginas.keys():
            if not os.path.exists(archivo):
                print(f"  - {archivo}")
        return False

def verificar_python():
    """Verifica la versión de Python"""
    print("\n✅ VERIFICACIÓN DE PYTHON:")
    print("-" * 60)
    version_info = sys.version_info
    version_str = f"{version_info.major}.{version_info.minor}.{version_info.micro}"
    print(f"Versión instalada: Python {version_str}")
    
    if version_info.major >= 3 and version_info.minor >= 8:
        print("✓ Versión compatible (3.8+)")
        return True
    else:
        print("✗ Versión insuficiente (requiere 3.8+)")
        return False

if __name__ == "__main__":
    estructura_ok = verificar_estructura()
    python_ok = verificar_python()
    
    if estructura_ok and python_ok:
        print("\n✨ ¡Todo está listo! Puedes comenzar el proyecto.")
        sys.exit(0)
    else:
        print("\n❌ Por favor, completa la configuración antes de continuar.")
        sys.exit(1)
