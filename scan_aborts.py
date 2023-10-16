from log_reader import read_log_file
from directory_reader import read_directory

directory_path = 'L:\\basic\divi\\Ima\\parrec\\!logfiles\\AMC-B1-MR-02\\2023-07\\log'
file_paths = read_directory(directory_path)


def find_scan_aborts(file_paths):
    scan_aborts = []

    for file_path in file_paths:
        log_lines = read_log_file(file_path)

        for line in log_lines[1:]:
            data = line.strip().split('\t')

            if len(data) >= 10:
                date = data[1]  # Second column
                log_text = data[-1]

                if "Current no of Scan" in log_text:
                    number_aborts = int(log_text.split('Aborts')[1].strip())
                    if number_aborts != 0:
                        scan_aborts.append((date, number_aborts))

    return scan_aborts

aborts = find_scan_aborts(file_paths)
print(aborts)
