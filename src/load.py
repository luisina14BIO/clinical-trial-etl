import sqlite3
from pathlib import Path

import pandas as pd


def load_data(
    df: pd.DataFrame,
    db_path: str,
    schema_path: str,
    table_name: str = "clinical_trials"
) -> None:
    """Persiste los datos transformados en una tabla SQLite."""

    ruta_db = Path(db_path)
    ruta_schema = Path(schema_path)

    if not ruta_schema.exists():
        raise FileNotFoundError(
            f"No se encontró el esquema SQL: {ruta_schema}"
        )

    if "subject_id" not in df.columns:
        raise ValueError("Falta la columna obligatoria 'subject_id'.")

    if df["subject_id"].isna().any():
        raise ValueError("subject_id contiene valores nulos.")

    if df["subject_id"].duplicated().any():
        raise ValueError("subject_id contiene valores duplicados.")

    if "dropout" in df.columns:
        valores_dropout = set(df["dropout"].dropna().unique())
        if not valores_dropout.issubset({0, 1}):
            raise ValueError("dropout solo puede contener valores 0 y 1.")

    ruta_db.parent.mkdir(parents=True, exist_ok=True)
    esquema_sql = ruta_schema.read_text(encoding="utf-8")

    # Evitar modificar el DataFrame original.
    df_carga = df.copy()

    # Guardar las fechas en un formato consistente para SQLite.
    if "enrollment_date" in df_carga.columns:
        df_carga["enrollment_date"] = (
            pd.to_datetime(
                df_carga["enrollment_date"],
                errors="coerce"
            )
            .dt.strftime("%Y-%m-%d")
        )

    try:
        with sqlite3.connect(ruta_db) as conexion:
            # Crear la tabla según el DDL.
            conexion.executescript(esquema_sql)

            # Recargar los datos sin eliminar la estructura de la tabla.
            conexion.execute(f'DELETE FROM "{table_name}"')

            df_carga.to_sql(
                name=table_name,
                con=conexion,
                if_exists="append",
                index=False
            )

            total = conexion.execute(
                f'SELECT COUNT(*) FROM "{table_name}"'
            ).fetchone()[0]

        print(f"Base de datos: {ruta_db}")
        print(f"Tabla: {table_name}")
        print(f"Registros almacenados: {total}")

    except sqlite3.Error as error:
        raise RuntimeError(
            f"Error al guardar los datos en SQLite: {error}"
        ) from error
