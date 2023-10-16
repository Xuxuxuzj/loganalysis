import pandas as pd
import re

def remove_prefixes_and_filter(error_text):
    if isinstance(error_text, str):
        # Remove [---] prefix and trim spaces
        error_text = re.sub(r'^\[\s*[0-9]+\]\s*|\[---\]\s*', '', error_text).strip()

        # Filter out errors matching the specified patterns
        patterns_to_filter = [
            r'^[A-Za-z0-9]{8}\s+00000000',
            r'^0x[A-Fa-f0-9]{8}',
            r'^\d',
            r'^\s*<\s*',
            r'^\s*=\s*',
            r'^\s*>\s*',
            r'^\s*"\s*'
        ]
        
        if any(re.match(pattern, error_text) for pattern in patterns_to_filter):
            return None

    return error_text

def filter_errors(errors_csv, output_csv):
    # Apply remove_prefixes_and_filter to the DataFrame rows
    errors_df = pd.read_csv(errors_csv)
    errors_df['Error'] = errors_df['Error'].apply(remove_prefixes_and_filter)
    errors_df = errors_df.dropna(subset=['Error'])
    errors_df.to_csv(output_csv, index=False)
    # Count the occurrences of each error
    #error_counts = errors_df['Error'].value_counts().reset_index()
    #error_counts.columns = ['Error', 'Count']
    
    #error_counts.to_csv(output_csv, index=False)

# Input CSV file path
input_csv = 'error_df2021.csv'  # Replace with the path to your input CSV file

# Output CSV file path
output_csv = 'filtered_error.csv'  # Replace with the desired output CSV file path

# Filter and process errors
filter_errors(input_csv, output_csv)

