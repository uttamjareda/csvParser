from .models import Student
from django.core.paginator import Paginator

class StudentRepository:
    @staticmethod
    def get_all_students(page_number, page_size):
        query_set = Student.objects.all()
        paginator = Paginator(query_set, page_size)
        page = paginator.get_page(page_number)
        students = list(page.object_list.values())
        return students, paginator.count

    @staticmethod
    def create_students(student_data_list):
        return Student.objects.bulk_create(student_data_list)

    @staticmethod
    def delete_all_students():
        return Student.objects.all().delete()
