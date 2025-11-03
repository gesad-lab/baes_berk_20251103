```python
import unittest
from unittest.mock import patch, MagicMock
from services.student_service import add_student, get_student_by_id, get_all_students

class TestStudentService(unittest.TestCase):

    @patch('services.student_service.StudentRepository')
    def test_add_student_success(self, MockStudentRepository):
        student_data = {'name': 'John Doe', 'age': 20, 'email': 'john@example.com'}
        mock_repo = MockStudentRepository.return_value
        mock_repo.add_student.return_value = True  # Simulating successful addition

        result = add_student(student_data)

        self.assertTrue(result)
        mock_repo.add_student.assert_called_once_with(student_data)

    @patch('services.student_service.StudentRepository')
    def test_get_student_by_id_found(self, MockStudentRepository):
        student_id = 1
        mock_student = {'id': student_id, 'name': 'John Doe', 'age': 20, 'email': 'john@example.com'}
        mock_repo = MockStudentRepository.return_value
        mock_repo.get_student_by_id.return_value = mock_student  # Simulating found student

        result = get_student_by_id(student_id)

        self.assertEqual(result, mock_student)
        mock_repo.get_student_by_id.assert_called_once_with(student_id)

    @patch('services.student_service.StudentRepository')
    def test_get_student_by_id_not_found(self, MockStudentRepository):
        student_id = 99
        mock_repo = MockStudentRepository.return_value
        mock_repo.get_student_by_id.return_value = None  # Simulating student not found

        result = get_student_by_id(student_id)

        self.assertIsNone(result)
        mock_repo.get_student_by_id.assert_called_once_with(student_id)

    @patch('services.student_service.StudentRepository')
    def test_get_all_students(self, MockStudentRepository):
        mock_students = [
            {'id': 1, 'name': 'John Doe', 'age': 20, 'email': 'john@example.com'},
            {'id': 2, 'name': 'Jane Doe', 'age': 22, 'email': 'jane@example.com'},
        ]
        mock_repo = MockStudentRepository.return_value
        mock_repo.get_all_students.return_value = mock_students  # Simulating retrieving all students

        result = get_all_students()

        self.assertEqual(result, mock_students)
        mock_repo.get_all_students.assert_called_once()

if __name__ == '__main__':
    unittest.main()
```