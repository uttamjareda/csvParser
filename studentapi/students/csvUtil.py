# csv_util.py

import csv
from django.core.exceptions import ValidationError
from io import StringIO
from studentapi import settings
        
def extract_state_from_location(city_name, csv_file_path=settings.USCITIES_PATH):
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['city'].lower() == city_name.lower():
                return row['state_name']
    return 'Unknown State'


def process_csv(file):
    csv_reader = csv.DictReader(file)
    processed_rows = []
    rows_skipped = 0

    for row in csv_reader:
        first_name = row.get('First Name', '').strip()
        last_name = row.get('Last Name', '').strip()
        full_name = f"{first_name} {last_name}".strip()
        
        if not full_name:
            print("Error processing row: Name is missing")
            rows_skipped += 1
            continue

        school = row.get('School', 'Unknown School')
        location = row.get('Location', 'Unknown Location')
        state = extract_state_from_location(location)

        # Identify all subject keys dynamically
        subject_keys = [key for key in row.keys() if "Class" in key]
        for subject_key in subject_keys:
            subject = row[subject_key].strip()
            if subject:  # Check if subject is not empty
                student_data = {
                    'name': full_name,
                    'school': school,
                    'state': state,
                    'subject': subject
                }
                processed_rows.append(student_data)
            else:
                rows_skipped += 1

    return processed_rows, rows_skipped
