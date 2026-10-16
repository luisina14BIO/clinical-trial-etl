
from pathlib import Path

from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data


def main():
    """Ejecuta el pipeline completo de datos clínicos."""

    ruta_proyecto = Path(__file__).resolve().parent

    ruta_entrada = (
        ruta_proyecto
        / "data"
        / "raw"
        / "synthetic_clinical_trial_data.csv"
    )

    ruta_salida = (
        ruta_proyecto
        / "data"
        / "processed"
        / "clinical_trial_clean.parquet"
    )

    print("=== INICIO DEL PIPELINE ===")

    print("\nETAPA 1: EXTRACCIÓN")
    df = extract_data(str(ruta_entrada))
    print(f"Registros extraídos: {len(df)}")

    print("\nETAPA 2: TRANSFORMACIÓN")
    df_limpio = transform_data(df)

    print("\nETAPA 3: CARGA")
    load_data(df_limpio, str(ruta_salida))

    print("\n=== PIPELINE FINALIZADO ===")


if __name__ == "__main__":
    main()
