```python
import unittest
from src.services import create_student, get_student_by_id, get_all_students
from src.models import Student
from src.database import db, init_db

class TestStudentServices(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the testing database and create necessary tables."""
        init_db()
        cls.app_context = db.app.app_context()
        cls.app_context.push()

    @classmethod
    def tearDownClass(cls):
        """Teardown app context after all tests have run."""
        cls.app_context.pop()

    def test_create_student_with_email(self):
        """Test creating a student with a valid name and email."""
        response = create_student(name='John Doe', email='john.doe@example.com')
        self.assertTrue(response['success'])
        self.assertIsNotNone(response['student_id'], "Student ID should be returned upon successful creation.")
        
        # Verify student is created in the database
        student = get_student_by_id(response['student_id'])
        self.assertEqual(student.name, 'John Doe')
        self.assertEqual(student.email, 'john.doe@example.com')

    def test_create_student_without_email(self):
        """Test error handling when creating a student without an email."""
        response = create_student(name='Jane Doe', email=None)
        self.assertFalse(response['success'])
        self.assertEqual(response['error'], "Email field is required.", "Should prompt about missing email.")

    def test_create_student_with_invalid_email(self):
        """Test error handling when creating a student with an invalid email format."""
        response = create_student(name='Invalid Email', email='invalid-email')
        self.assertFalse(response['success'])
        self.assertEqual(response['error'], "Invalid email format.", "Should prompt about invalid email format.")

    def test_get_all_students_includes_email(self):
        """Test retrieving all students includes email information."""
        create_student(name='Alice Smith', email='alice.smith@example.com')
        create_student(name='Bob Johnson', email='bob.johnson@example.com')

        all_students = get_all_students()
        self.assertGreater(len(all_students), 0, "Should return at least one student.")
        
        # Verify emails are included in the results
        for student in all_students:
            self.assertIn('email', student, "Each student record should contain an email field.")

if __name__ == '__main__':
    unittest.main()
```