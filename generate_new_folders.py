import os

# Specify the path where you want to create the new folders.
base_path = 'L://basic//Personal Archive//Z//zhangj//logfiles-Z01-2017-2021'

# List of folder names you want to create.
folder_names = [
    "log2019-07", "log2019-08", "log2019-09", "log2019-10", "log2019-11", "log2019-12",
    "log2018-01", "log2018-02", "log2018-03", "log2018-04", "log2018-05", "log2018-06",
    "log2018-07", "log2018-08", "log2018-09", "log2018-10", "log2018-11", "log2018-12",
    "log2017-06", "log2017-07", "log2017-08", "log2017-09", "log2017-10", "log2017-11", "log2017-12"
]

# Create the folders one by one.
for folder_name in folder_names:
    # Construct the full path for the new folder.
    new_folder_path = os.path.join(base_path, folder_name)
    
    # Check if the folder already exists before creating it.
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
        print(f"Created folder: {new_folder_path}")
    else:
        print(f"Folder already exists: {new_folder_path}")
