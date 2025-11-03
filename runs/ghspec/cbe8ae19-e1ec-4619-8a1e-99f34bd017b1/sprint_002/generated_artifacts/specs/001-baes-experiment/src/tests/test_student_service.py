```python
import unittest
from app import create_app, db
from models import Student
from services.student_service import get_student_by_id

class TestStudentService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the test environment and create the application."""
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        db.create_all()  # Create the schema before running tests

        # Add a sample student for testing
        student = Student(name='John Doe', email='john@example.com')
        db.session.add(student)
        db.session.commit()
        cls.student_id = student.id

    @classmethod
    def tearDownClass(cls):
        """Clean up the database after running tests."""
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def test_get_student_by_id_success(self):
        """
        Test retrieving a student by ID successfully returns 
        the student's details including email.
        """
        student = get_student_by_id(self.student_id)
        
        # Check if the student details match
        self.assertIsNotNone(student)
        self.assertEqual(student.id, self.student_id)
        self.assertEqual(student.name, 'John Doe')
        self.assertEqual(student.email, 'john@example.com')

    def test_get_student_by_id_not_found(self):
        """
        Test retrieving a student by a non-existing ID returns None 
        indicating student was not found.
        """
        student = get_student_by_id(999)  # Assuming 999 is an ID that doesn't exist
        self.assertIsNone(student)

if __name__ == '__main__':
    unittest.main()
```