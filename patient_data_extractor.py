from log_reader import read_log_file
from start_end_time import get_start_end_time

def extract_patient_data(lines, end_time):
    patients = []
    current_patient = []

    for line in lines:
        data = line.strip().split('\t')

        
        if len(data) >= 10:
            text = data[-1]
            time_str = data[2]

            if text == 'New examination selected':

                if current_patient:
                    patients.append(current_patient)
                    current_patient = []
            current_patient.append(data)

            if time_str == end_time:
                #print("time string normal")
                patients.append(current_patient)
                current_patient = []
                break
    
    if current_patient:
        patients.append(current_patient)
    
    patients = patients[1:]
    return patients


#file_path = r'L:\\basic\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2023-06\\log\\log202306120000.log'
#lines = read_log_file(file_path)
#start_time, end_time = get_start_end_time(lines)
#patients = extract_patient_data(lines, end_time)