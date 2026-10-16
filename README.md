# Clinical Trial ETL Pipeline 

## Descripción

Proyecto de Data Science II que implementa un pipeline ETL (*Extract, Transform, Load*) para procesar un dataset de ensayos clínicos.

El pipeline lee un archivo CSV, limpia y transforma los datos, y exporta el resultado en formato Parquet para facilitar su utilización en análisis de datos y futuros proyectos de Machine Learning.

## Estructura del proyecto

```text
clinical-trial-etl/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── data/
│   ├── raw/
│   └── processed/
└── notebooks/
    └── pipeline.testing.ipynb
```

## Tecnologías utilizadas

* Python
* Pandas
* PyArrow
* JupyterLab

## Dataset

Se utiliza un dataset de ensayos clínicos almacenado en formato CSV.

Archivo esperado:

`data/raw/synthetic_clinical_trial_data.csv`

El archivo contiene 1.000 registros y 11 columnas relacionadas con participantes, tratamientos, variables clínicas y resultados del ensayo.

El dataset original no se incluye en el repositorio. Para ejecutar el pipeline, es necesario obtener el archivo y colocarlo en la ruta indicada.

## Etapas del pipeline

### 1. Extracción

El módulo `src/extract.py` lee el archivo CSV y carga los datos en un DataFrame de Pandas.

### 2. Transformación

El módulo `src/transform.py` implementa las siguientes operaciones:

* Normalización de los nombres de las columnas.
* Conversión de la fecha de inscripción al tipo de dato fecha.
* Eliminación de registros duplicados.
* Gestión de valores nulos mediante reglas definidas.
* Optimización básica de memoria mediante tipos categóricos cuando corresponde.

### 3. Carga

El módulo `src/load.py` exporta los datos transformados a formato Parquet, conservando los tipos de datos y facilitando su lectura en tareas analíticas.

## Instalación

Se recomienda utilizar un entorno virtual de Python.

Instalar las dependencias con:

```bash
pip install -r requirements.txt
```

## Ejecución

1. Colocar el archivo CSV en `data/raw/`.
2. Instalar las dependencias.
3. Ejecutar el pipeline desde la raíz del proyecto:

```bash
python main.py
```

El archivo procesado se generará en:

`data/processed/clinical_trial_clean.parquet`

## Resultado de la ejecución

En la prueba realizada, el pipeline procesó correctamente los 1.000 registros y las 11 columnas originales.

No se detectaron duplicados ni valores nulos en el dataset utilizado. Los datos se exportaron correctamente a formato Parquet.

## Autoría

Proyecto académico desarrollado para la asignatura Data Science II de Coderhouse.

