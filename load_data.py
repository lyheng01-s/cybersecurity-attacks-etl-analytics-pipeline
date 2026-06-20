import os
from urllib.parse import quote_plus

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()


def load_cybersecurity_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(current_dir, "cybersecurity_attacks.csv")

    print("Loading CSV into Pandas DataFrame...")
    df = pd.read_csv(csv_file_path, encoding="utf-8-sig")

    # Clean column names
    df.columns = df.columns.str.strip()

    time_col = next(
        (col for col in df.columns if "imestamp" in col.lower()),
        None
    )

    if time_col:
        df.rename(columns={time_col: "Timestamp"}, inplace=True)

    df.columns = df.columns.str.replace(" ", "_", regex=False)
    df.columns = df.columns.str.replace("/", "_", regex=False)
    df.columns = df.columns.str.replace("-", "_", regex=False)

    df["Timestamp"] = pd.to_datetime(
        df["Timestamp"],
        errors="coerce"
    )

    # SQL Server settings
    server = os.getenv("DB_SERVER", "localhost,1433")
    database = os.getenv("DB_NAME", "CybersecurityDB")
    username = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    driver = "ODBC Driver 17 for SQL Server"

    odbc_connection = (
        f"DRIVER={{{driver}}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
        f"Encrypt=yes;"
        f"TrustServerCertificate=yes;"
    )

    connection_string = (
        "mssql+pyodbc:///?odbc_connect="
        + quote_plus(odbc_connection)
    )

    engine = create_engine(
        connection_string,
        fast_executemany=True
    )

    table_name = "CybersecurityAttacks"

    print(
        f"Inserting {len(df)} rows into "
        f"dbo.{table_name}..."
    )

    try:
        with engine.begin() as conn:
            conn.execute(
                text(
                    f"DROP TABLE IF EXISTS "
                    f"dbo.{table_name}"
                )
            )

        df.to_sql(
            name=table_name,
            schema="dbo",
            con=engine,
            if_exists="replace",
            index=False,
            chunksize=1000
        )

        print(
            f"Successfully inserted {len(df)} rows "
            f"into SQL Server!"
        )

    except Exception as e:
        print(f"An error occurred: {e}")
        raise


if __name__ == "__main__":
    load_cybersecurity_data()