# Student Study Performance Dataset Analysis

This project provides insights into the Student Study Performance Dataset, focusing on factors influencing students' test scores and academic performance.

## Project Structure

- **Build_Database.py:** Python script to create a SQLite database and import data from the CSV file.
- **StudyPerformance.py:** Flask web application to visualize the dataset with pages for the index, about, and data.
- **templates/:** HTML templates for the website.

## Usage

1. Install dependencies: `pip install -r requirements.txt`
2. Run the database builder: `python Build_Database.py`
3. Launch the web application: `python StudyPerformance.py`

## About the Dataset

- **Source of Data:** The dataset is sourced from Kaggle.
- **Size:** 1000 rows x 8 columns.
- **Variables:** Gender, Race/Ethnicity, Parental Level of Education, Lunch, Test Preparation Course, Math Score, Reading Score, Writing Score.

## Key Features

- **Demographic Factors Analysis:** Explore the impact of gender, ethnicity, and parental level of education on students' test scores.
- **Student Support Examination:** Analyze the effects of lunch habits and test preparation courses on academic performance.
- **Subject Scores Analysis:** Assess students' scores in math, reading, and writing subjects.

## Additional Information

- The `StudyData.db` file contains the SQLite database with the imported dataset. You can use a SQLite database viewer to explore the data further.

- The website is currently set to run in debug mode (`app.run(debug=True)` in `StudyPerformance.py`). For production use, consider changing this configuration.

## Group Members

- **Santhosh Raghavendra Gopi**
- **Prakash Tejashwani Samboju**
- **Oluwaseun Soyinka**
