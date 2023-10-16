from log_reader import read_log_file
from directory_reader import read_directory
import pandas as pd


directory_path = 'L:\\basic\\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2023-01\\log'

file_paths = read_directory(directory_path)

# Extract all errors with severity 'E'
errors = []

for file_path in file_paths:
    log_lines = read_log_file(file_path)

    for line in log_lines[1:]:
        data = line.strip().split('\t')
        if len(data) >= 10:
            severity = data[4]
            date = data[1]
            text = data[9]  # Change this line to use data[9]
            if severity == 'E':
                errors.append((date, text))

# Create a DataFrame for all errors with a 'Count' column initialized to 1
error_data = {'Date': [], 'Error': [], 'Count': []}
for date, error_text in errors:
    error_data['Date'].append(date)
    error_data['Error'].append(error_text)
    error_data['Count'].append(1)  # Count each error as 1

error_df = pd.DataFrame(error_data)
error_df['Error'] = error_df['Error'].str.strip()

# Save the DataFrame containing all errors
error_df.to_csv('error_df.csv', index=False)
