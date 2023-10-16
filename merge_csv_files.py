import os
import pandas as pd

# Step 1: Initialize an empty DataFrame to store the merged data
merged_data = pd.DataFrame()

# Step 2: Specify the directory containing your CSV files
csv_directory = 'L:\\basic\\Personal Archive\\Z\\zhangj\\logfilecodes\\grouped_errors'

# Step 3: Loop through CSV files in the directory
for filename in os.listdir(csv_directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(csv_directory, filename)
        
        # Read each CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Step 4: Concatenate (merge) the DataFrames
        merged_data = pd.concat([merged_data, df], ignore_index=True)

# Step 5: Group by 'Error Group' and sum 'Count'
grouped_data = merged_data.groupby('Error Group')['Count'].sum().reset_index()

# Step 6: Group by 'Error Group' and concatenate 'Texts' as a single list
final_merged_data = merged_data.groupby('Error Group')['Texts'].sum().reset_index()

# Step 7: Merge the two DataFrames to combine 'Count' and 'Texts'
final_merged_data = final_merged_data.merge(grouped_data, on='Error Group')

# Step 8: Optionally, save the merged DataFrame to a new CSV file
final_merged_data.to_csv('L:\\basic\\Personal Archive\\Z\\zhangj\\logfilecodes\\all_errors2023.csv', index=False)
