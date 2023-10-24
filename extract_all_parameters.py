import pandas as pd
from log_reader import read_log_file
from datetime import datetime

def extract_parameter_values(log_lines, parameters):
    parameter_data = {param: [] for param in parameters}
    id_text_list = [value[0] for value in parameters.values()]
    filtered_log_lines = filter(lambda line: any(identification in line for identification in id_text_list), log_lines[1:])

    for line in filtered_log_lines:
        data = line.strip().split('\t')
        date, time_str, text = data[1], data[2], data[-1]

        for param, param_info in parameters.items():
            id_text, break1, break2, datatype = param_info
            if id_text in text:
                temp_text = text.split(break1)[1]
                value = extract_value(temp_text, break2)
                if value is None:
                    continue
                timestamp = datetime.strptime(f"{date} {time_str}", "%Y-%m-%d %H:%M:%S.%f")
                parameter_data[param].append((timestamp, convert_value(datatype, value)))

    return parameter_data

def extract_value(temp_text, break2):
    if break2 == 'space':
        return temp_text.split()[0].strip()
    elif break2 == 'none':
        return temp_text.strip()
    elif break2 == '"':
        return temp_text.split(break2)[2].strip()
    else:
        return temp_text.split(break2)[0].strip()

def convert_value(datatype, value):
    if datatype == 'numerical':
        return float(value)
    elif datatype == 'categorical':
        return int(value)
    elif datatype == 'percent':
        return f'{value}%'
    else:
        return value

'''
excel_file_path = 'L:\\basic\\Personal Archive\\Z\\zhangj\\parameters for extraction.xlsx'
df = pd.read_excel(excel_file_path)
parameters = {row['parameter']: (row['identification tekst'], row['1st break'], row['2nd break'], row['type of data']) for index, row in df.iterrows()}

file_path = r'L:\\basic\\Personal Archive\\Z\\zhangj\\logfiles-Z01-2017-2021\\log2017\\log2017-06\\log201706090000.log'
log_lines = read_log_file(file_path)
parameter_data = extract_parameter_values(log_lines, parameters)
'''

'''
#printing data
# Specify the parameter you want to print data for
selected_parameter = '1HRFAmp2_PredAvgPower'  # Replace 'ParameterName' with the parameter you want

if selected_parameter in parameter_data:
    print(f"Parameter: {selected_parameter}")
    for timestamp, value in parameter_data[selected_parameter]:
        print(f"  Timestamp: {timestamp}, Value: {value}")
else:
    print(f"Parameter '{selected_parameter}' not found in the data.")
'''

