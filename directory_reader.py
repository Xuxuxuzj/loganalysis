import os

def read_directory(directory_path):
    file_paths = []

    # List all files in the directory
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.log'):  # Filter log files
                file_path = os.path.join(root, file)
                file_paths.append(file_path)
    
    return file_paths
