from django.forms import ValidationError
from .csvUtil import process_csv
from students.models import Student
from .repositories import StudentRepository

class StudentService:
    @staticmethod
    def get_all_students(page, limit):
        students, total = StudentRepository.get_all_students(page, limit)
        return students, total
        
    @staticmethod
    def add_students_from_csv(file):
        processed_rows, rows_skipped = process_csv(file)
        if not processed_rows:
            return None, f'No rows processed. Rows skipped due to errors: {rows_skipped}.'

        students = [Student(**row_data) for row_data in processed_rows]
        Student.objects.bulk_create(students)  # This will save all entries to the database
        try:
            return students, f"Rows added: {len(processed_rows)}, Rows skipped: {rows_skipped}"
        except ValidationError as e:
                return None, str(e)


    @staticmethod
    def delete_all_students():
        return StudentRepository.delete_all_students()
