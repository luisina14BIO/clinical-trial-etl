import pandas as pd


def extract_data(file_path):
    """Lee un archivo CSV y lo carga en un DataFrame."""

    df = pd.read_csv(file_path)

    print(f"Dataset cargado: {len(df)} filas y {len(df.columns)} columnas")

    return df
