from log_reader import read_log_file

def extract_parameters(log_lines):
    parameters = []
    for line in log_lines[1:]:
        data = line.strip().split('\t')
        if len(data) >= 10:
            text = data[-1]

            if 'monitor_' in text:
                parameter = text.split('monitor_')[1].split('.dat')[0].strip()
                parameters.append(parameter)
            elif 'Monitor_' in text:
                parameter = text.split('Monitor_')[1].split('.dat')[0].strip()
                parameters.append(parameter)

    return parameters

def print_list_elements_one_per_row(parameters):
    for item in parameters:
        print(item)

def print_list_elements_in_one_row(parameters):
    print(' '.join(str(item) for item in parameters))





file_path = r'L:\\basic\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2023-06\\log\\log202306120000.log'
log_lines = read_log_file(file_path)
parameters = extract_parameters(log_lines)
print_list_elements_in_one_row(parameters)
path = 'L:\basic\Personal Archive\Z\zhangj\output.xlsx'
