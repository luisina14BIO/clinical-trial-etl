from pathlib import Path

from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data


def main():
    """Ejecuta el pipeline ETL de datos clínicos."""

    ruta_proyecto = Path(__file__).resolve().parent

    ruta_entrada = (
        ruta_proyecto
        / "data"
        / "raw"
        / "synthetic_clinical_trial_data.csv"
    )

    ruta_db = (
        ruta_proyecto
        / "data"
        / "processed"
        / "clinical_trials.db"
    )

    ruta_schema = ruta_proyecto / "schema.sql"

    print("=== INICIO DEL PIPELINE ===")

    # 1. Extracción
    print("\nETAPA 1: EXTRACCIÓN")
    df = extract_data(str(ruta_entrada))
    print(f"Registros extraídos: {len(df)}")

    # 2. Transformación
    print("\nETAPA 2: TRANSFORMACIÓN")
    df_limpio = transform_data(df)
    print(f"Registros transformados: {len(df_limpio)}")

    # 3. Persistencia
    print("\nETAPA 3: PERSISTENCIA")
    load_data(
        df_limpio,
        str(ruta_db),
        str(ruta_schema)
    )

    print("\n=== PIPELINE FINALIZADO ===")


if __name__ == "__main__":
    main()
