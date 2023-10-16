from patient_data_extractor import extract_patient_data
from log_reader import read_log_file
from start_end_time import get_start_end_time


def extract_coil_identification(patients):
    

    for i, patient in enumerate(patients):
        coil_names = set()

        for data in patient:

            if len(data) >= 10:
                text = data[-1]  # Last column

                if text.startswith("CI: Detected: "):
                    coil_name = text.split("CI: Detected: ")[1].split('/')[0].strip()
                    coil_names.add(coil_name)

        if not coil_names:
            if i == 0:
                continue
            else:
                continue

        total_coils = len(coil_names)

        if i != 0:
            print()

        print(f"Patient #{i} coil names")
        coil_names_str = ", ".join(coil_names)
        print(coil_names_str)

        print(f"Total number of coils: {total_coils}")

# Usage
file_path = r'L:\\basic\divi\\Ima\\parrec\\!logfiles\\AMC-Z0-MR-01\\2023-06\\log\\log202306120000.log'
lines = read_log_file(file_path)
start_time, end_time = get_start_end_time(lines)
patients = extract_patient_data(lines, end_time)
extract_coil_identification(file_path)
