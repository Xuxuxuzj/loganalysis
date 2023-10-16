import pandas as pd

def to_excel(df, excel_path):  # Changed the function signature to accept DataFrame
    df.to_excel(excel_path, index=False)

# Load the DataFrame from the CSV file
og_csv = pd.read_csv('ungrouped_errors.csv')

# Define the Excel file path
excel_path = 'ungrouped_errors2022.xlsx'

# Export the DataFrame to Excel using your 'to_excel' function
to_excel(og_csv, excel_path)