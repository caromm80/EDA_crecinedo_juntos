import pandas as pd
import os

files = {
    "Estudiantes": "datos_hoja_estudiantes.csv",
    "Cursos": "datos_hoja_cursos.csv",
    "Calificaciones": "datos_hoja_calificaciones.csv",
    "Inscripciones": "datos_hoja_inscripciones.csv"
}

with open("c:/Users/carol/cesde_ntp_EDA/tablas_google_sheets_tsv.txt", "w", encoding="utf-8") as out:
    for tab_name, csv_file in files.items():
        out.write("=" * 60 + "\n")
        out.write(f"TABLA: {tab_name} (Copiar desde la línea de abajo hasta el final de la tabla)\n")
        out.write("=" * 60 + "\n")
        
        df = pd.read_csv(f"c:/Users/carol/cesde_ntp_EDA/{csv_file}")
        
        # Escribir cabecera
        header = "\t".join(df.columns)
        out.write(header + "\n")
        
        # Escribir filas
        for idx, row in df.iterrows():
            row_str = "\t".join([str(val) for val in row.values])
            out.write(row_str + "\n")
            
        out.write("\n\n")

print("¡Tablas TSV para Google Sheets listas!")
