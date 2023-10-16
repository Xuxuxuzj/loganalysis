from log_reader import read_log_file

def get_processes(log_lines):
    process_set = set()

    for line in log_lines[1:]:
        data = line.strip().split('\t')
        if len(data) >= 10:
            process = data[5].strip()
            process_set.add(process)

    return process_set

file_path = r'L:\\basic\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2023-01\\log\\log202301060000.log'
log_lines = read_log_file(file_path)
processes = get_processes(log_lines)
print(processes)