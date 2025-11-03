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
        """Teardown app context after tests completion."""
        cls.app_context.pop()

    def setUp(self):
        """Create a new test database session."""
        db.create_all()
        self.student_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'age': 20
        }

    def tearDown(self):
        """Remove all tables after each test."""
        db.session.remove()
        db.drop_all()

    def test_create_student(self):
        """Test the creation of a new student record."""
        student = create_student(**self.student_data)
        self.assertIsInstance(student, Student)
        self.assertEqual(student.name, self.student_data['name'])
        self.assertEqual(student.email, self.student_data['email'])
        self.assertEqual(student.age, self.student_data['age'])

    def test_get_student_by_id(self):
        """Test retrieving a student by ID."""
        student = create_student(**self.student_data)
        retrieved_student = get_student_by_id(student.id)
        self.assertEqual(retrieved_student.id, student.id)
        self.assertEqual(retrieved_student.name, student.name)

    def test_get_all_students(self):
        """Test retrieving all students."""
        create_student(**self.student_data)
        students = get_all_students()
        self.assertGreater(len(students), 0)
        self.assertEqual(students[0].name, self.student_data['name'])
    
    def test_create_student_with_invalid_data(self):
        """Test creating a student with invalid data."""
        with self.assertRaises(ValueError):
            create_student(name='', email='invalid-email', age=-1)  # Invalid data

if __name__ == '__main__':
    unittest.main()
```