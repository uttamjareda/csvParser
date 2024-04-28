from django.test import TestCase
from io import StringIO
from students.csvUtil import process_csv

class CSVUtilTests(TestCase):
    
    def test_process_csv_with_well_formed_data(self):
        csv_data = StringIO("""
            First Name,Last Name,Class 1,Class 2,School,Location
            John,Doe,Math,Science,MIT,New York
            Jane,Smith,English,Art,Harvard,Los Angeles
            """.strip())

        processed_rows, rows_skipped = process_csv(csv_data)
        self.assertEqual(len(processed_rows), 4)  # Expecting 2 subjects per student
        self.assertEqual(rows_skipped, 0)  # No rows should be skipped

        # Check the first subject of the first student
        self.assertEqual(processed_rows[0]['name'], 'John Doe')
        self.assertEqual(processed_rows[0]['school'], 'MIT')
        self.assertEqual(processed_rows[0]['subject'], 'Math')
        self.assertEqual(processed_rows[0]['state'], 'New York')

        # Check the second subject of the first student
        self.assertEqual(processed_rows[1]['subject'], 'Science')

        # Check the first subject of the second student
        self.assertEqual(processed_rows[2]['name'], 'Jane Smith')
        self.assertEqual(processed_rows[2]['school'], 'Harvard')
        self.assertEqual(processed_rows[2]['subject'], 'English')

        # Check the second subject of the second student
        self.assertEqual(processed_rows[3]['subject'], 'Art')
        self.assertEqual(processed_rows[3]['state'], 'California')
