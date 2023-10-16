import pandas as pd

# Replace 'your_excel_file.xlsx' with the path to your Excel file.
excel_file_path = 'Error_id_strings.xlsx'

# Read the Excel file into a Pandas DataFrame.
df_error_ids = pd.read_excel(excel_file_path)

# Extract the values from the "Error id" column and convert them into a set.
error_ids_set = set(df_error_ids['Error id'])


# Replace 'error_df2023.csv' with the path to your CSV file.
csv_file_path = 'filtered_error.csv'

# Read the CSV file into a Pandas DataFrame.
error_df = pd.read_csv(csv_file_path)

# Initialize dictionaries to store grouped errors and a set to store unique ungrouped errors.
grouped_errors = {}
ungrouped_errors_set = set()

# Iterate through each error in the CSV file.
for index, row in error_df.iterrows():
    error_text = str(row['Error'])
    error_id_found = False

    for error_id in error_ids_set:
        er_id = str(error_id)
        if er_id in error_text.lower():
            # The error matches one of the error IDs.
            if er_id not in grouped_errors:
                grouped_errors[er_id] = {
                    'ErrorTexts': set(),
                    'Dates': set(),  # Use a set to store unique dates
                    'Count': 0
                }
            grouped_errors[er_id]['ErrorTexts'].add(error_text)
            grouped_errors[er_id]['Dates'].add(row['Date'])  # Add date to the set
            grouped_errors[er_id]['Count'] += row['Count']
            error_id_found = True
            break

    if not error_id_found:
        

        if error_text == "Launchpad(CSC):" or error_text == "Server:":
            continue
        if "MRLog(data):" in error_text and "}" in error_text:
            continue
        if "0x" or ":00" or "EDX" or "EAX" or "MPAAC(): >" or "{filtered"in error_text:
            continue

        else:
            ungrouped_errors_set.add((error_text, row['Date'], row['Count']))

# Create DataFrames for grouped errors and convert the set of ungrouped errors to a list.
grouped_errors_df = pd.DataFrame(grouped_errors).T.reset_index()
grouped_errors_df = grouped_errors_df.rename(columns={'index': 'Error id'})
grouped_errors_df['ErrorTexts'] = grouped_errors_df['ErrorTexts'].apply(list)

ungrouped_errors_list = list(ungrouped_errors_set)
ungrouped_errors_df = pd.DataFrame(ungrouped_errors_list, columns=['ErrorText', 'Date', 'Count'])
ungrouped_errors_df = ungrouped_errors_df[~ungrouped_errors_df['ErrorText'].str.contains(r'<|>')]


# Save the grouped errors DataFrame to a CSV file.
grouped_errors_csv_file = 'grouped_errors.csv'
grouped_errors_df.to_csv(grouped_errors_csv_file, index=False)

# Save the ungrouped errors DataFrame to a separate CSV file.
ungrouped_errors_csv_file = 'ungrouped_errors.csv'
ungrouped_errors_df.to_csv(ungrouped_errors_csv_file, index=False)
