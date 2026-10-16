from pathlib import Path
import pandas as pd


def load_data(df: pd.DataFrame, output_path: str) -> None:
    """Guarda el DataFrame procesado en formato Parquet."""

    ruta_salida = Path(output_path)
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)

    df.to_parquet(ruta_salida, index=False)

    print(f"Datos guardados correctamente en: {ruta_salida}")
    print(f"Registros exportados: {len(df)}")