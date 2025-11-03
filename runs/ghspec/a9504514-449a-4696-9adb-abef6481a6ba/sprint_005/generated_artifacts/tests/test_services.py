```python
import unittest
from src.services import create_course, get_all_courses, enroll_student_in_course, get_student_courses, create_teacher, get_teacher_by_id
from src.models import Course, Student, Teacher
from src.database import db, init_db

class TestCourseServices(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the testing database and create necessary tables."""
        init_db()
        cls.app_context = db.app.app_context()
        cls.app_context.push()

        # Create a sample course and student for testing
        cls.course = Course(name="Sample Course")
        cls.student = Student(name="Sample Student", email="student@example.com")
        db.session.add(cls.course)
        db.session.add(cls.student)
        db.session.commit()

    @classmethod
    def tearDownClass(cls):
        """Clean up the database after tests."""
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def test_create_teacher(self):
        """Test successful creation of a teacher."""
        teacher_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com'
        }
        teacher = create_teacher(teacher_data)
        self.assertIsNotNone(teacher.id)  # Ensure the teacher has been created with an ID
        self.assertEqual(teacher.name, teacher_data['name'])
        self.assertEqual(teacher.email, teacher_data['email'])

    def test_get_teacher_by_id(self):
        """Test successful retrieval of teacher details by ID."""
        teacher_data = {
            'name': 'Jane Smith',
            'email': 'jane.smith@example.com'
        }
        teacher = create_teacher(teacher_data)
        retrieved_teacher = get_teacher_by_id(teacher.id)
        self.assertEqual(retrieved_teacher.name, teacher_data['name'])
        self.assertEqual(retrieved_teacher.email, teacher_data['email'])

    def test_create_teacher_missing_name(self):
        """Test validation for missing name."""
        teacher_data = {
            'email': 'missing.name@example.com'
        }
        with self.assertRaises(ValueError) as context:
            create_teacher(teacher_data)
        self.assertEqual(str(context.exception), "Name is required.")

    def test_create_teacher_invalid_email(self):
        """Test validation for invalid email format."""
        teacher_data = {
            'name': 'Invalid Email',
            'email': 'invalid-email-format'
        }
        with self.assertRaises(ValueError) as context:
            create_teacher(teacher_data)
        self.assertEqual(str(context.exception), "Invalid email format.")
```