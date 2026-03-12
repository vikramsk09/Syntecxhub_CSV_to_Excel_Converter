"""
CSV → Excel Converter

Features:
1. Reads CSV file
2. Cleans / normalizes data
3. Handles missing values
4. Parses date columns
5. Renames columns
6. Saves data to Excel (.xlsx)
7. CLI arguments for input/output
8. Logging and error handling
"""

import pandas as pd
import argparse
import logging
import os


# -------------------------------
# Setup Logging
# -------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)


# Function: Clean Data

def clean_data(df):
    # Remove extra spaces from column names
    df.columns = df.columns.str.strip()

    # Convert column names to lowercase
    df.columns = df.columns.str.lower()

    # Replace spaces with underscore
    df.columns = df.columns.str.replace(" ", "_")

    # Fill missing values
    df = df.fillna("N/A")

    # Try converting columns with 'date' in the name
    for col in df.columns:
        if "date" in col:
            try:
                df[col] = pd.to_datetime(df[col], errors="coerce")
            except Exception:
                logging.warning(f"Could not parse date column: {col}")

    return df



# Function: Rename Columns

def rename_columns(df):
    rename_dict = {
        "fname": "first_name",
        "lname": "last_name",
        "dob": "date_of_birth"
    }

    df = df.rename(columns=rename_dict)

    return df


# Main Function

def convert_csv_to_excel(input_file, output_file):
    # Check if file exists
    if not os.path.exists(input_file):
        logging.error("Input file does not exist.")
        return

    try:
        logging.info("Reading CSV file...")

        # Read CSV
        df = pd.read_csv(input_file)

        logging.info("Cleaning data...")
        df = clean_data(df)

        logging.info("Renaming columns...")
        df = rename_columns(df)

        logging.info("Saving to Excel...")

        # Save as Excel
        df.to_excel(output_file, index=False, engine="openpyxl")

        logging.info(f"Conversion successful! File saved as: {output_file}")

    except Exception as e:
        logging.error(f"Error processing file: {e}")


# CLI Arguments

def main():
    parser = argparse.ArgumentParser(description="CSV to Excel Converter")

    parser.add_argument(
        "--input",
        required=True,
        help="Path to input CSV file"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Path to output Excel file"
    )

    args = parser.parse_args()

    convert_csv_to_excel(args.input, args.output)



# Run Script

if __name__ == "__main__":

    # Ask user for file names
    input_file = input("Enter the name of input file: ")
    output_file = input("Enter the name of Output file: ")

    # Run conversion
    convert_csv_to_excel(input_file, output_file)

