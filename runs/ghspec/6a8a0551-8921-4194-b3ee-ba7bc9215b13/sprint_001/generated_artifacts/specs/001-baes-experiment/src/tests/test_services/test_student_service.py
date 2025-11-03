```python
import unittest
from unittest.mock import patch, MagicMock

from services.student_service import StudentService
from models import Student


class TestStudentService(unittest.TestCase):
    def setUp(self):
        """Set up the test environment before each test."""
        self.service = StudentService()
        self.student_data = {'name': 'John Doe'}

    @patch('services.student_service.Student')
    def test_create_student_success(self, MockStudent):
        """Test creating a student successfully."""
        MockStudent.return_value = MagicMock(id=1, name='John Doe')
        student = self.service.create_student(self.student_data)

        self.assertEqual(student['name'], 'John Doe')
        self.assertIn('id', student)

    def test_create_student_missing_name(self):
        """Test creating a student without a name fails validation."""
        with self.assertRaises(ValueError) as context:
            self.service.create_student({'name': ''})

        self.assertEqual(str(context.exception), "Student name is required.")

    @patch('services.student_service.Student')
    def test_get_student_success(self, MockStudent):
        """Test retrieving a student successfully."""
        MockStudent.query.get.return_value = MagicMock(id=1, name='John Doe')
        student = self.service.get_student(1)

        self.assertEqual(student['name'], 'John Doe')
        self.assertIn('id', student)

    @patch('services.student_service.Student')
    def test_get_student_not_found(self, MockStudent):
        """Test retrieving a student that does not exist."""
        MockStudent.query.get.return_value = None
        student = self.service.get_student(999)

        self.assertIsNone(student)

    @patch('services.student_service.Student')
    def test_delete_student_success(self, MockStudent):
        """Test deleting a student successfully."""
        MockStudent.query.get.return_value = MagicMock(id=1, name='John Doe')
        self.service.delete_student(1)
        MockStudent.query.get.assert_called_once_with(1)
        MockStudent.query.filter_by().delete.assert_called_once()

    @patch('services.student_service.Student')
    def test_delete_student_not_found(self, MockStudent):
        """Test deleting a student that does not exist."""
        MockStudent.query.get.return_value = None
        with self.assertRaises(ValueError) as context:
            self.service.delete_student(999)

        self.assertEqual(str(context.exception), "Student not found.")

if __name__ == '__main__':
    unittest.main()
```