import datetime
from log_reader import read_log_file

def get_start_end_time(log_lines):
    start_times = []
    end_times = []

    for line in log_lines[1:]: 
        data = line.strip().split('\t')
        if len(data) >= 10:
            
            time_str = data[2]  # Third column
            text = data[-1]  # Last column
            if text == 'Starting Application Software':
                start_time = time_str
                start_times.append(start_time)
            if 'Finished stop of Application Software' in text:
                end_time = time_str
                end_times.append(end_time)

    first_start = start_times[0]
    last_end = end_times[-1]    

    return first_start, last_end


#usage
#file_path = r'L:\\basic\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2023-06\\log\\log202306120000.log'
#log_lines = read_log_file(file_path)
#start_time, end_time = get_start_end_time(log_lines)
