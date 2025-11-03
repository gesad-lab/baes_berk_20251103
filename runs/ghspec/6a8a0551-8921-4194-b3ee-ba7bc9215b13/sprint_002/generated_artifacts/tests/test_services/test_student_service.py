```python
import unittest
from unittest.mock import patch, MagicMock

from services.student_service import StudentService
from models import Student


class TestStudentService(unittest.TestCase):
    def setUp(self):
        """Set up the test environment before each test."""
        self.service = StudentService()
        self.student_data = {'name': 'John Doe', 'email': 'john.doe@example.com'}

    @patch('services.student_service.Student')
    def test_create_student_success(self, MockStudent):
        """Test creating a student with valid data succeeds."""
        MockStudent.return_value = MagicMock(id=1, **self.student_data)
        
        created_student = self.service.create_student(self.student_data)
        
        self.assertEqual(created_student['name'], self.student_data['name'])
        self.assertEqual(created_student['email'], self.student_data['email'])
        MockStudent.assert_called_once_with(**self.student_data)

    @patch('services.student_service.Student')
    def test_create_student_missing_email(self, MockStudent):
        """Test creating a student without an email raises a validation error."""
        student_data = {'name': 'Jane Doe'}
        
        with self.assertRaises(ValueError) as context:
            self.service.create_student(student_data)
        
        self.assertEqual(str(context.exception), "Email is required.")

    @patch('services.student_service.Student')
    def test_create_student_invalid_email(self, MockStudent):
        """Test creating a student with an invalid email raises a validation error."""
        student_data = {'name': 'Jane Doe', 'email': 'invalid-email-format'}
        
        with self.assertRaises(ValueError) as context:
            self.service.create_student(student_data)
        
        self.assertEqual(str(context.exception), "Invalid email format.")

    @patch('services.student_service.Student')
    @patch('services.student_service.Student.query')
    def test_get_student_by_id_success(self, mock_query, MockStudent):
        """Test retrieving a student by ID returns the correct student data."""
        mock_query.get.return_value = MockStudent(id=1, name='John Doe', email='john.doe@example.com')
        
        student = self.service.get_student_by_id(1)
        
        self.assertEqual(student['name'], 'John Doe')
        self.assertEqual(student['email'], 'john.doe@example.com')

    @patch('services.student_service.Student')
    @patch('services.student_service.Student.query')
    def test_get_student_by_id_not_found(self, mock_query, MockStudent):
        """Test retrieving a student by ID that does not exist raises an error."""
        mock_query.get.return_value = None
        
        with self.assertRaises(ValueError) as context:
            self.service.get_student_by_id(99)
        
        self.assertEqual(str(context.exception), "Student not found.")

    @patch('services.student_service.Student')
    @patch('services.student_service.Student.query')
    def test_get_all_students_success(self, mock_query, MockStudent):
        """Test retrieving all students returns the correct student list."""
        mock_query.all.return_value = [
            MockStudent(id=1, name='John Doe', email='john.doe@example.com'),
            MockStudent(id=2, name='Jane Doe', email='jane.doe@example.com')
        ]
        
        students = self.service.get_all_students()
        
        self.assertEqual(len(students), 2)
        self.assertEqual(students[0]['name'], 'John Doe')
        self.assertEqual(students[0]['email'], 'john.doe@example.com')
        self.assertEqual(students[1]['name'], 'Jane Doe')
        self.assertEqual(students[1]['email'], 'jane.doe@example.com')
```