import pandas as pd

# Step 1: Read the CSV file into a pandas DataFrame
file_path = 'grouped_errors_202201.csv'  # Replace with the path to your CSV file
data = pd.read_csv(file_path)

# Step 2: Sort the DataFrame by the "Count" column
sorted_data = data.sort_values(by='Count')

# Step 3: Print the sorted DataFrame
print(sorted_data)
