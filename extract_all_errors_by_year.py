from directory_reader import read_directory
from log_reader import read_log_file
import pandas as pd
import os

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

                  
'''
directory2017 = ['L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2017\\log2017-06',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2017\\log2017-07',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2017\\log2017-08',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2017\\log2017-09',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2017\\log2017-10',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2017\\log2017-11',
                  'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2017\\log2017-12']

list_directories = directory2017

# Initialize an empty list to store all file paths
all_file_paths = []

# Iterate through the list of directory paths and collect file paths
for directory_path in list_directories:
    file_paths = read_directory(directory_path)
    all_file_paths.extend(file_paths)
    
# Initialize a counter for file processing
file_counter = 0
errors = []
# Iterate through each file path in all_file_paths
for file_path in all_file_paths:
    # Increment the file counter
    file_counter += 1
    
    # Print a message indicating the file being processed
    print(f"Processing file {file_counter}/{len(all_file_paths)}: {file_path}")
    
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
error_df.to_csv('error_df2017.csv', index=False)
