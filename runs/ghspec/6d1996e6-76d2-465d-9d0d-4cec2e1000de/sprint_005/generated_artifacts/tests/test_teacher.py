import unittest
from unittest.mock import patch
from services.teacher import TeacherService
from models.teacher import Teacher

class TestTeacherManagement(unittest.TestCase):
    def setUp(self):
        """Set up a test environment for Teacher tests."""
        self.teacher_service = TeacherService()

    @patch('models.teacher.Teacher')
    def test_create_new_teacher_success(self, mock_teacher):
        """Test creating a new teacher with valid name and email."""
        mock_teacher.return_value = Teacher(name='John Doe', email='john.doe@example.com')
        result = self.teacher_service.create_teacher('John Doe', 'john.doe@example.com')
        self.assertIsInstance(result, Teacher)
        self.assertEqual(result.name, 'John Doe')
        self.assertEqual(result.email, 'john.doe@example.com')

    def test_create_new_teacher_missing_name(self):
        """Test creating a new teacher with missing name."""
        with self.assertRaises(ValueError) as context:
            self.teacher_service.create_teacher('', 'john.doe@example.com')
        self.assertEqual(str(context.exception), "Name and email are required.")

    def test_create_new_teacher_missing_email(self):
        """Test creating a new teacher with missing email."""
        with self.assertRaises(ValueError) as context:
            self.teacher_service.create_teacher('John Doe', '')
        self.assertEqual(str(context.exception), "Name and email are required.")

    @patch('services.teacher.TeacherService.get_teacher_by_id')
    def test_retrieve_teacher_success(self, mock_get_teacher):
        """Test retrieving teacher's information by valid ID."""
        mock_get_teacher.return_value = Teacher(name='John Doe', email='john.doe@example.com')
        teacher = self.teacher_service.get_teacher_by_id(1)
        self.assertEqual(teacher.name, 'John Doe')
        self.assertEqual(teacher.email, 'john.doe@example.com')

    @patch('models.teacher.Teacher')
    def test_update_teacher_success(self, mock_teacher):
        """Test updating a teacher's information with valid data."""
        mock_teacher.return_value = Teacher(name='John Doe', email='john.doe@example.com')
        updated_teacher = self.teacher_service.update_teacher(1, name='Jane Doe', email='jane.doe@example.com')
        self.assertEqual(updated_teacher.name, 'Jane Doe')
        self.assertEqual(updated_teacher.email, 'jane.doe@example.com')

    def test_update_teacher_invalid_id(self):
        """Test updating a teacher with an invalid ID."""
        with self.assertRaises(ValueError) as context:
            self.teacher_service.update_teacher(999, name='Jane Doe', email='jane.doe@example.com')
        self.assertEqual(str(context.exception), "Teacher not found.")

if __name__ == '__main__':
    unittest.main()