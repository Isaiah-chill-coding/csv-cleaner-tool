# CSV Cleaner Tool

A lighter Python utility for cleaning CSV datasets and exporting the result as either a CSV or Excel file.

## Overview

This project was made to automate easy data-cleaning tasks that are usually required before data analysis or spreadsheet processing.

The tool allows users to import a CSV file, remove any duplicate records, handle those missing values using several strategies, and export the cleaned dataset in their preferred format. This is version 1 for now. 

## Features

* Import CSV files
* Remove duplicate rows
* Ignore ID columns when checking for duplicate records
* Handle missing values by:

  * Removing incomplete rows
  * Filling missing values with 0
  * Leaving missing values unchanged
* Export cleaned data as:

  * CSV
  * Excel (.xlsx)
* Show a summary including:

  * Original row count
  * Duplicate rows removed
  * Rows removed due to missing values
  * Final row count

## Technologies

* Python
* Pandas
* OpenPyXL

## Project Structure

```text
csv-cleaner-tool/
├── cleaner.py
├── requirements.txt
├── README.md
├── sample_data/
│   └── dataset.csv
└── output/
    └── cleaned_dataset.csv
```

## Installation

Install the required packages, you can write it in the terminal:

```bash
pip install -r requirements.txt
```

## Usage

1. Place a CSV file inside the `sample_data` folder.
2. Run:

```bash
python cleaner.py
```

3. Enter the file name when prompted.
4. Choose whether to:

   * Remove duplicate rows
   * Handle missing values
   * Export as CSV or Excel

The cleaned file will be saved inside the `output` folder.

## Example Use Cases Can Include

* Cleaning customer spreadsheets
* Removing duplicate records
* Preparing datasets for analysis
* Organizing CSV files before importing into Excel or databases

## Future Improvements

* Better error handling
* Automatic output filenames based on the input file
* Additional missing-value strategies
* Column selection options
* PDF to CSV integration
