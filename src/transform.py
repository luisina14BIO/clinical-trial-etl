import pandas as pd


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia los datos, gestiona valores nulos y optimiza la memoria."""

    # Trabajar sobre una copia para conservar los datos originales
    df = df.copy()

    # 1. Normalizar los nombres de las columnas
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r"\s+", "_", regex=True)
    )

    print("Nombres de columnas normalizados.")

    # 2. Convertir la fecha de inscripción al tipo fecha
    if "enrollment_date" in df.columns:
        df["enrollment_date"] = pd.to_datetime(
            df["enrollment_date"],
            format="%m/%d/%y",
            errors="coerce"
        )

    print("Fecha de inscripción convertida correctamente.")

    # 3. Eliminar registros duplicados
    filas_iniciales = len(df)
    df = df.drop_duplicates()
    duplicados_eliminados = filas_iniciales - len(df)

    print(f"Duplicados eliminados: {duplicados_eliminados}")

    # 4. Gestionar valores nulos
    # Los identificadores y las variables de resultado son esenciales.
    # Se eliminan las filas que no permiten identificar al participante
    # o conocer el resultado del ensayo.
    columnas_esenciales = [
        "subject_id",
        "dropout",
        "adverse_events"
    ]

    columnas_esenciales = [
        columna for columna in columnas_esenciales
        if columna in df.columns
    ]

    filas_antes = len(df)
    df = df.dropna(subset=columnas_esenciales)
    filas_eliminadas = filas_antes - len(df)

    print(f"Filas eliminadas por datos esenciales faltantes: {filas_eliminadas}")

    # Completar categorías faltantes sin inventar información
    columnas_texto = df.select_dtypes(
        include=["object", "str", "category"]
    ).columns

    for columna in columnas_texto:
        df[columna] = df[columna].fillna("Desconocido")

    # Completar variables clínicas numéricas con la mediana
    # Solo se aplica a variables de medición, no a identificadores,
    # sitios ni variables binarias de resultado.
    columnas_a_excluir = [
        "subject_id",
        "site_id",
        "dropout",
        "adverse_events"
    ]

    columnas_numericas = df.select_dtypes(
        include="number"
    ).columns

    for columna in columnas_numericas:
        if columna not in columnas_a_excluir:
            if df[columna].isna().any():
                mediana = df[columna].median()
                df[columna] = df[columna].fillna(mediana)

    # 5. Optimizar el almacenamiento de variables categóricas
    columnas_texto = df.select_dtypes(
        include=["object", "str"]
    ).columns

    for columna in columnas_texto:
        if df[columna].nunique() < len(df) * 0.5:
            df[columna] = df[columna].astype("category")

    # 6. Informar los resultados de la transformación
    print("Transformación completada.")
    print(f"Filas finales: {len(df)}")
    print(f"Columnas finales: {len(df.columns)}")
    print(f"Valores nulos restantes: {df.isna().sum().sum()}")

    return df
