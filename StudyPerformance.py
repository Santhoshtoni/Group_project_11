from flask import Flask, render_template
import sqlite3
from pathlib import Path

app = Flask(__name__)

# Define the path to the database file
db_name = 'StudyData.db'
file_path = Path(__file__).resolve().parent / db_name

@app.route('/')
def index():
    return render_template("index_fillin.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/data")
def data():

    # Connect to the SQLite database
    con = sqlite3.connect(file_path)
    cursor = con.cursor()

    # Select the first 10 records from the Study_Performance table
    cursor.execute("SELECT * FROM Study_Performance ORDER BY 1 ASC LIMIT 10")
    study_performance = cursor.fetchall()

    # Close the database connection
    con.close()


    # Render the template with the fetched data
    return render_template("data_table_fillin.html", data=study_performance)

if __name__ == "__main__":
    app.run(debug=True)
