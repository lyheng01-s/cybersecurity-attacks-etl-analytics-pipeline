# Cybersecurity Attacks ETL & Analytics Pipeline

## Project Overview

This project demonstrates an end-to-end batch data engineering workflow using Microsoft SQL Server, PySpark, Python, and Power BI.

## Data Source

Cyber Security Attacks Dataset:

https://www.kaggle.com/datasets/teamincribo/cyber-security-attacks

The dataset contains approximately 40,000 cybersecurity event records.

## Project Workflow

1. Read the cybersecurity dataset from a CSV file.
2. Clean and standardize the data using Python and Pandas.
3. Load 40,000 records into Microsoft SQL Server.
4. Connect PySpark to SQL Server through JDBC.
5. Perform data-quality checks and analytical aggregations using PySpark.
6. Connect Power BI to SQL Server.
7. Visualize cybersecurity patterns and insights in Power BI.

## Main Technologies

* Python
* Pandas
* Microsoft SQL Server
* SQLAlchemy
* PyODBC
* PySpark
* JDBC
* Power BI

## Project Files

* `cybersecurity_attacks.csv` — original dataset
* `load_data.py` — loads and cleans the CSV data into SQL Server
* `pyspark_load_sqlserver.ipynb` — connects PySpark to SQL Server and performs analysis
* `Cyber_security_analysis.pbix` — Power BI dashboard
* `Data_Engineering_Slide.pdf` — project presentation
* `requirements.txt` — required Python packages

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

## Database Configuration

The project uses:

* Server: `localhost`
* Port: `1433`
* Database: `CybersecurityDB`
* Table: `dbo.CybersecurityAttacks`

Database credentials should not be committed to a public repository.

## Execution Order

### 1. Load the CSV into SQL Server

```bash
python load_data.py
```

Expected result:

```text
Successfully inserted 40000 rows into SQL Server!
```

### 2. Run the PySpark notebook

Open and run:

```text
pyspark_load_sqlserver.ipynb
```

Expected result:

```text
Successfully loaded 40,000 rows from SQL Server.
```

### 3. Open the Power BI dashboard

Open:

```text
Cyber_security_analysis.pbix
```

Refresh the report to retrieve the latest data from SQL Server.

## Processing Type

This project uses batch processing rather than real-time streaming. When the CSV data changes, rerun `load_data.py`, rerun the PySpark analysis, and refresh Power BI.
