# Syntecxhub_CSV_to_Excel_Converter
CSV to Excel Converter

This project is a simple and efficient Python-based CSV to Excel Converter that reads data from a CSV file, performs basic data cleaning and normalization, and exports the processed data into an Excel (.xlsx) file.
The project demonstrates practical usage of Python, pandas, and openpyxl for data processing and file conversion. It also includes logging and error handling to make the script more reliable and user-friendly.

- Features
1. Reads CSV files and converts them into Excel format (.xlsx)
2. Cleans and normalizes column names (removes spaces, converts to lowercase, replaces spaces with underscores)
3. Handles missing values automatically
4. Parses columns containing date values
5. Supports simple column renaming for better data readability
6. Includes logging for process tracking and error reporting
7. Checks whether the input file exists before processing

- Technologies Used
1. Python
2. pandas
3. openpyxl
4. argparse
5. logging

- How It Works
1) The program asks the user to enter the name of the input CSV file.
2) The CSV data is loaded into a pandas DataFrame.

- Data cleaning operations are performed:
1) Column normalization
2) Missing value handling
3) Date parsing
4) Selected columns are renamed for better structure.
5) The cleaned dataset is exported as an Excel file.

- Example Usage
Run the script and provide the file names when prompted:
python CSV_to_Excel_Converter.py

- Example input:
1) Enter the name of input file: sample.csv
2) Enter the name of Output file: sample.xlsx
   
- Project Purpose:
- This project was created to practice data processing and automation in Python, and to demonstrate how CSV data can be cleaned and converted into structured Excel files for easier analysis and reporting.
