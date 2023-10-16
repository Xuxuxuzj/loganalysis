from log_reader import read_log_file

def filter_log(log_lines):
    needed_lines = []
    disk_full_found = False

    for line in log_lines: 
        data = line.strip().split('\t')
        if len(data) >= 10:
            text = data[-1]
            if 'Disk Full: available space is less than' in text and not disk_full_found:
                needed_lines.append(line)
                disk_full_found = True
                break
        
        if not disk_full_found:
            needed_lines.append(line)

    return needed_lines


def save_lines_to_log_file(lines, filename):
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)

# Assuming you already have the 'needed_lines' list
file_path = r'L:\\basic\divi\\Ima\\parrec\\!logfiles\\AMC-B1-MR-02\\2023-08\\log\\log202308190000.log'
lines = read_log_file(file_path)
needed_lines = filter_log(lines)

# Specify the filename for the new log file
new_log_filename = 'L:\\basic\\Personal Archive\\Z\\zhangj\\filtered_log202309190000.log'

# Save the 'needed_lines' to the new log file
save_lines_to_log_file(needed_lines, new_log_filename)