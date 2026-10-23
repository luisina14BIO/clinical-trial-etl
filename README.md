# Pipeline ETL de Ensayos Clínicos con SQLite

Proyecto de ETL (Extracción, Transformación y Carga) que procesa datos sintéticos de ensayos clínicos utilizando Python, pandas, SQL y SQLite. El pipeline extrae datos desde un archivo CSV, limpia y transforma los registros y persiste los resultados en una base de datos relacional.

## Objetivos del Proyecto

* Construir un pipeline ETL modular y reutilizable.
* Limpiar y estandarizar datos de ensayos clínicos.
* Definir un esquema de tabla relacional mediante restricciones SQL.
* Persistir los datos transformados en SQLite.
* Validar la integridad de los datos y la repetibilidad del pipeline.

## Estructura del Proyecto

```text
clinical-trial-etl/
├── data/
│   ├── raw/
│      └── synthetic_clinical_trial_data.csv  
├── notebooks/
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── main.py
├── schema.sql
├── requirements.txt
└── README.md
```

## Flujo ETL

**1. Extracción**

Carga el conjunto de datos de origen desde un archivo CSV con 1.000 registros y 11 columnas.

**2. Transformación**

* Normaliza los nombres de las columnas utilizando el formato `snake_case` en minúsculas.
* Convierte las fechas de inscripción al tipo datetime.
* Elimina registros duplicados.
* Gestiona los valores faltantes en columnas esenciales y no esenciales.
* Optimiza los tipos de datos de las columnas de texto.

**3. Carga y persistencia**

* Crea la tabla `clinical_trials` utilizando el esquema SQL definido en `schema.sql`.
* Aplica restricciones de integridad mediante una clave primaria, una restricción `NOT NULL` y una restricción `CHECK`.
* Almacena los registros transformados en una base de datos SQLite.
* Permite recargas completas y repetibles sin duplicar registros.

## Validación de Datos

Se realizaron pruebas para verificar:

* La extracción, transformación y persistencia correctas de los 1.000 registros.
* La ausencia de valores nulos después de la transformación.
* La unicidad y ausencia de nulos en `subject_id`.
* La creación correcta del esquema de la base de datos y sus restricciones.
* La repetibilidad del pipeline en ejecuciones consecutivas, manteniendo los 1.000 registros.

## Tecnologías Utilizadas

* **Python 3.11:** desarrollo del pipeline.
* **pandas 3.0.6:** manipulación y transformación de datos.
* **SQLite:** almacenamiento y persistencia relacional.
* **SQL:** definición del esquema y restricciones de integridad.
* **JupyterLab:** pruebas y validación del pipeline.
* **GitHub:** control de versiones.

## Cómo Ejecutar el Proyecto

Clonar el repositorio y ubicarse en la carpeta raíz del proyecto.

Instalar las dependencias necesarias:

```bash
pip install -r requirements.txt
```

Ejecutar el pipeline desde la raíz del proyecto:

```bash
python main.py
```

El pipeline crea la base de datos SQLite en `data/processed/clinical_trials.db` y muestra los resultados de cada etapa del proceso ETL.

## Notas

El proyecto utiliza un conjunto de datos sintético de ensayos clínicos con fines educativos. La base de datos SQLite generada no se incluye en el repositorio, ya que se crea al ejecutar el pipeline.
