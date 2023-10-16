import datetime
from log_reader import read_log_file
from patient_data_extractor import extract_patient_data
from start_end_time import get_start_end_time


def format_duration(duration):
    total_minutes = int(duration.total_seconds() // 60)
    return total_minutes



def exam_and_scan_durations(patients):
    exam_durations = []
    scan_durations = []
    number_scans = []

    for patient in patients:
        scan_count = 0
        first_scan_start = None
        last_scan_end = None
        exam_start_time = None
        door_open_time = None

        for data in patient:

            if len(data) >= 10:

                time_str = data[2]  # Third column
                text = data[-1]  # Last column

                if text == 'New examination selected':
                    exam_start_time = time_str
                if 'the door is opened' in text:
                    door_open_time = time_str

                if text == ' Scan starts':
                    scan_start_time = time_str
                    
                    if first_scan_start is None:
                        first_scan_start = scan_start_time

                if text == ' Scan completed':
                    scan_count += 1
                    last_scan_end = time_str
        


        
        if first_scan_start and last_scan_end:
            scan_duration = datetime.datetime.strptime(last_scan_end, '%H:%M:%S.%f') - datetime.datetime.strptime(first_scan_start, '%H:%M:%S.%f')
            scan_duration = format_duration(scan_duration) #in minutes
            scan_durations.append((first_scan_start, last_scan_end, scan_duration))
        
        if exam_start_time and door_open_time:
            exam_duration = datetime.datetime.strptime(door_open_time, '%H:%M:%S.%f') - datetime.datetime.strptime(exam_start_time, '%H:%M:%S.%f')
            exam_duration = format_duration(exam_duration)
            exam_durations.append((exam_start_time, door_open_time, exam_duration))

        number_scans.append(scan_count)


    return scan_durations, exam_durations, number_scans

# Usage
file_path = r'L:\\basic\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2023-01\\log\\log202301060000.log'
log_lines = read_log_file(file_path)
start_time, end_time = get_start_end_time(log_lines)
print(start_time, end_time)

patients = extract_patient_data(log_lines, end_time)
print(len(patients))
scan_durations, exam_durations, number_scans = exam_and_scan_durations(patients)
print(exam_durations)
print(scan_durations)
print(number_scans)




# Printing functions
def print_num_exams(exam_durations):
    number_exams = len(exam_durations)
    print(f'Total number of examinations: {number_exams}')

def print_exam_and_scan_duration(exam_durations, scan_durations):
    print('Duration for each patient:')
    for i, (scan_duration, exam_duration) in enumerate(zip(scan_durations, exam_durations), start=1):
        formatted_exam_start = exam_duration[0].strftime('%H:%M:%S')
        formatted_duration = format_duration(exam_duration[2])
        formatted_scan_duration = format_duration(scan_duration[2])
        formatted_scan_start = scan_duration[0].strftime('%H:%M:%S')

        print(f'Patient #{i}: Start Time: {formatted_exam_start}, Exam Duration: {formatted_duration}. Scan start: {formatted_scan_start}, Scan Duration: {formatted_scan_duration}, Total number of scans: {number_scans}')


#print_exam_and_scan_duration(exam_durations, scan_durations)