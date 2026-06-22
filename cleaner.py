# CSV CLEANER v1

import pandas as pd
import os

file_name = input("Enter the CSV file name inside sample_data: ")
file_path = os.path.join("sample_data", file_name)

df = pd.read_csv(file_path)

original_rows = len(df)

remove_duplicates = input("Would you like to remove duplicate rows? (y/n): ").lower()

duplicates_removed = 0

if remove_duplicates == "y":
    rows_before_duplicates = len(df)
    duplicate_check_columns = [col for col in df.columns if col.lower() != "id"]
    df = df.drop_duplicates(subset=duplicate_check_columns)
    duplicates_removed = rows_before_duplicates - len(df)

choice = input(
    "What do you want to do with missing values?\n"
    "1. Drop rows\n"
    "2. Fill with 0\n"
    "3. Leave unchanged\n"
)

rows_before_missing = len(df)

if choice == "1":
    df = df.dropna()
elif choice == "2":
    df = df.fillna(0)

missing_rows_removed = rows_before_missing - len(df)

print(f"Original rows: {original_rows}")
print(f"Duplicates removed: {duplicates_removed}")
print(f"Rows removed from missing values: {missing_rows_removed}")
print(f"Final rows: {len(df)}")
print(f"Rows removed total: {original_rows - len(df)}")

output_type = input(
    "How would you like your file back?\n"
    "1. CSV\n"
    "2. Excel\n"
)

if output_type == "1":
    df.to_csv("output/cleaned_dataset.csv", index=False)
elif output_type == "2":
    df.to_excel("output/cleaned_dataset.xlsx", index=False)

print("Cleaning complete.")