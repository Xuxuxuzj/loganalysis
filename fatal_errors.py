from log_reader import read_log_file
from directory_reader import read_directory
from directory_reader import read_directory
import pandas as pd

def extract_fatal_errors(file_paths):
    errors = []

    for file_path in file_paths:
        log_lines = read_log_file(file_path)

        for line in log_lines[1:]:
            data = line.strip().split('\t')
            if len(data) >= 10:
                severity = data[4]
                date = data[1]
                text = data[-1]
                if severity == 'F':
                    errors.append((date, text))

    return errors

directory_path = 'L:\\basic\\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2023-08\\log'
file_paths = read_directory(directory_path)

# Extract errors
errors = extract_fatal_errors(file_paths)

# Create a dictionary to count error frequencies based on the error message
error_counts = defaultdict(list)

for date, error_text in errors:
    error_counts[error_text].append(date)

# Create a DataFrame with Date, Error, and Count columns
data = {'Date': [], 'Fatal Error': [], 'Count': []}
for error, dates in error_counts.items():
    count = len(dates)
    if count > 1:
        dates = ', '.join(dates)  # Join multiple dates into a single string
    else:
        dates = dates[0]  # Keep the single date as is
    data['Date'].append(dates)
    data['Fatal Error'].append(error)
    data['Count'].append(count)

error_df = pd.DataFrame(data)

# Sort the DataFrame by date and error message
error_df = error_df.sort_values(by=['Date', 'Fatal Error'])


# Print or export the DataFrame as needed
excel_file_path = 'L:\\basic\\Personal Archive\\Z\\zhangj\\fatal_errors_count.xlsx'

# Export the DataFrame to an Excel file
error_df.to_excel(excel_file_path, index=False)