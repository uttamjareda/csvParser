from django.urls import reverse
from django.test import TestCase, Client
from students.models import Student
from io import StringIO
from django.core.files.uploadedfile import SimpleUploadedFile
from unittest.mock import patch

class StudentAPITest(TestCase):
    def setUp(self):
        # Set up data for tests
        self.client = Client()
        Student.objects.create(name="John Doe", subject="A", school="Springfield High", state="Springfield")
        Student.objects.create(name="Jane Smith", subject="B", school="Ridgemont High", state="Ridgemont")

    def tearDown(self):
        Student.objects.all().delete()

    def test_get_all_students(self):
        response = self.client.get(reverse('get_all_students'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)  # Checking if the pagination count matches

    def test_add_students_from_csv(self):
        csv_content = b'First Name,Last Name,Class 1,Class 2,School,Location\r\nJohn,Doe,Math,Science,MIT,New York\r\nJane,Smith,English,Art,Harvard,Los Angeles'
        uploaded_file = SimpleUploadedFile('testfile.csv', csv_content, content_type='text/csv')
        with patch('students.services.StudentService.add_students_from_csv') as mocked_service:
            mocked_service.return_value = ([Student(name="John Doe", subject="Math", school="MIT", state="New York")], "Rows added: 1, Rows skipped: 0")
            response = self.client.post(reverse('add_from_csv'), {'studentcsv': uploaded_file})
            self.assertEqual(response.status_code, 200)
            self.assertIn('Students added successfully', response.json()['message'])

    def test_delete_all_students(self):
        response = self.client.delete(reverse('delete_all_students'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Deleted', response.json()['message'])
        self.assertEqual(Student.objects.count(), 0)  # Ensure all students are deleted

