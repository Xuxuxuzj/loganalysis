import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from directory_reader import read_directory
from log_reader import read_log_file
from extract_all_parameters import extract_parameter_values
from multiprocessing import Pool


'''
list_directories2023 = ['L:\\basic\\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2023-01\\log',
                    'L:\\basic\\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2023-02\\log',
                    'L:\\basic\\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2023-03\\log',
                    'L:\\basic\\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2023-04\\log',
                    'L:\\basic\\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2023-05\\log',
                    'L:\\basic\\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2023-06\\log',
                    'L:\\basic\\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2023-07\\log',
                    'L:\\basic\\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2023-08\\log']


list_directories2022 = ['L:\\basic\\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2022-01\\log',
                    'L:\\basic\\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2022-02\\log',
                    'L:\\basic\\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2022-03\\log',
                    'L:\\basic\\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2022-04\\log',
                    'L:\\basic\\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2022-05\\log',
                    'L:\\basic\\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2022-06\\log',
                    'L:\\basic\\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2022-07\\log',
                    'L:\\basic\\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2022-08\\log',
                    'L:\\basic\\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2022-09\\log',
                    'L:\\basic\\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2022-10\\log',
                    'L:\\basic\\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2022-11\\log',
                    'L:\\basic\\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2022-12\\log',
                    ]

directory2021 = ['L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2021\\log2021-01',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2021\\log2021-02',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2021\\log2021-03',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2021\\log2021-04',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2021\\log2021-05',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2021\\log2021-06',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2021\\log2021-07',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2021\\log2021-08',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2021\\log2021-09',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2021\\log2021-10',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2021\\log2021-11',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2021\\log2021-12']

directory2020 = ['L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2020\\log2020-01',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2020\\log2020-02',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2020\\log2020-03',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2020\\log2020-04',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2020\\log2020-05',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2020\\log2020-06',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2020\\log2020-07',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2020\\log2020-08',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2020\\log2020-09',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2020\\log2020-10',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2020\\log2020-11',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2020\\log2020-12']

directory2019 = ['L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2019\\log2019-01',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2019\\log2019-02',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2019\\log2019-03',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2019\\log2019-04',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2019\\log2019-05',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2019\\log2019-06',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2019\\log2019-07',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2019\\log2019-08',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2019\\log2019-09',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2019\\log2019-10',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2019\\log2019-11',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2019\\log2019-12']         

directory2018 = ['L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2018\\log2018-01',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2018\\log2018-02']
               
directory2017 = ['L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2017\\log2017-06',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2017\\log2017-07',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2017\\log2017-08',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2017\\log2017-09',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2017\\log2017-10',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2017\\log2017-11',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2017\\log2017-12']
'''
list_directories = ['//home//zhangj//lood_storage//Personal Archive//Z//zhangj//logfiles-Z01-2017-2021//log2017//']

# Initialize an empty list to store all file paths
all_file_paths = []

# Iterate through the list of directory paths and collect file paths
for directory_path in list_directories:
    file_paths = read_directory(directory_path)
    all_file_paths.extend(file_paths)

# Read parameter information from the Excel file
parameter_file_path = '//home//zhangj//lood_storage//Personal Archive//Z//zhangj//logfilecodes//parameters for extraction.xlsx'
df = pd.read_excel(parameter_file_path)
parameters = {row['parameter']: (row['identification tekst'], row['1st break'], row['2nd break'], row['type of data']) for index, row in df.iterrows()}

# Initialize a dictionary of DataFrames to store parameter data
parameter_dataframes = {param: pd.DataFrame(columns=['Timestamp', 'Value']) for param in parameters}
file_counter = 0

# Loop through the log files and extract parameter data
for file_path in all_file_paths:
    # Increment the file counter
    file_counter += 1

    # Print a message indicating the file being processed
    print(f"Processing file {file_counter}/{len(all_file_paths)}: {file_path}")

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
output_directory = "/home//zhangj//lood_storage//Personal Archive//zhangj//parameter_data_files"

# Loop through the parameter DataFrames and save them to Parquet files
for param, df in parameter_dataframes.items():
    parquet_file_path = os.path.join(output_directory, f"{param}.parquet")
    table = pa.Table.from_pandas(df)

    if os.path.exists(parquet_file_path):
        existing_table = pq.read_table(parquet_file_path)
        table = pa.concat_tables([existing_table, table])

    pq.write_table(table, parquet_file_path)
    print(f"Appended data for parameter {param} to {parquet_file_path}")