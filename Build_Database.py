import sqlite3
import pandas as pd
from pathlib import Path

path = Path.cwd()

def create_db(db_name, filename, table_name):
    file_path = path / filename
    con = sqlite3.connect(db_name)
    print('DB Build Success.')
    cursor = con.cursor()
    Study_Performance = pd.read_csv(file_path)
    Study_Performance.to_sql(table_name, con, index=False, if_exists='replace')
    results = cursor.execute(f"select count(*) from {table_name}").fetchall()
    print(f'Data Imported Successfully.\n{results[0][0]} Rows Inserted.')
    con.commit()
    con.close()

if __name__ == "__main__":
    db_name = "StudyData.db"  # Change the database name here
    filename = "study_performance.csv"
    table_name = "Study_Performance"
    create_db(db_name, filename, table_name)
