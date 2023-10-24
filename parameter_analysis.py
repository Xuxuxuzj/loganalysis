import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from directory_reader import read_directory
from log_reader import read_log_file
from extract_all_parameters import extract_parameter_values
from multiprocessing import Pool

list_directories = ['/home/zhangj/lood_storage/Personal Archive/Z/zhangj/logfiles-Z01-2017-2021/log2018/']

# Initialize an empty list to store all file paths
all_file_paths = []

# Iterate through the list of directory paths and collect file paths
for directory_path in list_directories:
    file_paths = read_directory(directory_path)
    all_file_paths.extend(file_paths)

# Read parameter information from the Excel file
parameter_file_path = '/home/zhangj/scratch/zhangj/logfilecodes/parameters for extraction.csv'
df = pd.read_csv(parameter_file_path)
parameters = {row['parameter']: (row['identification tekst'], row['1st break'], row['2nd break'], row['type of data']) for index, row in df.iterrows()}

# Initialize a dictionary of DataFrames to store parameter data
parameter_dataframes = {param: pd.DataFrame(columns=['Timestamp', 'Value']) for param in parameters}
#file_counter = 0

# Loop through the log files and extract parameter data
for file_path in all_file_paths:
    # Increment the file counter
    #file_counter += 1

    # Print a message indicating the file being processed
    # print(f"Processing file {file_counter}/{len(all_file_paths)}: {file_path}")

    log_lines = read_log_file(file_path)

    extracted_data = extract_parameter_values(log_lines, parameters)

    # Append the data to the respective DataFrame
    for param, data in extracted_data.items():

        if any(element == 'NA' for element in data):
            continue
        elif parameter_dataframes[param].empty:
            parameter_dataframes[param] = pd.DataFrame(data, columns=['Timestamp', 'Value'])
        else:
            parameter_dataframes[param] = pd.concat([parameter_dataframes[param], pd.DataFrame(data, columns=['Timestamp', 'Value'])])


# Define the directory where you want to save the Parquet files
output_directory = "/home/zhangj/scratch/zhangj/parameter_data_files/2018/"

# Loop through the parameter DataFrames and save them to Parquet files
for param, df in parameter_dataframes.items():
    parquet_file_path = os.path.join(output_directory, f"{param}.parquet")
    table = pa.Table.from_pandas(df)
    pq.write_table(table, parquet_file_path)
    print(f"Saved data for parameter {param} to {parquet_file_path}")