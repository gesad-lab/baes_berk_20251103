```python
import unittest
from src.services import create_course, assign_teacher_to_course, get_course_by_id
from src.models import Course, Teacher
from src.database import db, init_db

class TestCourseServices(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the testing database and create necessary tables."""
        init_db()
        cls.app_context = db.app.app_context()
        cls.app_context.push()
        cls.create_initial_data()

    @classmethod
    def tearDownClass(cls):
        """Clean up after tests."""
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    @classmethod
    def create_initial_data(cls):
        """Create initial data for testing."""
        cls.teacher = Teacher(name="John Doe")
        db.session.add(cls.teacher)
        db.session.commit()

        cls.course = Course(title="Math 101", teacher_id=None)  # No teacher assigned initially
        db.session.add(cls.course)
        db.session.commit()

    def test_assign_teacher_to_course(self):
        """Test assigning a teacher to an existing course."""
        response = assign_teacher_to_course(course_id=self.course.id, teacher_id=self.teacher.id)
        
        # Since this is a hypothetical function, we should assume it returns the updated course
        self.assertIsNotNone(response)
        self.assertEqual(response.teacher_id, self.teacher.id)

    def test_retrieve_course_with_teacher_details(self):
        """Test retrieving course details with teacher assigned."""
        assign_teacher_to_course(course_id=self.course.id, teacher_id=self.teacher.id)
        course_details = get_course_by_id(course_id=self.course.id)

        self.assertEqual(course_details.title, "Math 101")
        self.assertEqual(course_details.teacher_id, self.teacher.id)
        self.assertEqual(course_details.teacher.name, self.teacher.name)

    def test_assign_non_existent_teacher(self):
        """Test assigning a non-existent teacher to a course fails gracefully."""
        with self.assertRaises(ValueError) as context:
            assign_teacher_to_course(course_id=self.course.id, teacher_id=999)  # Assuming 999 is invalid
        
        self.assertEqual(str(context.exception), "Error: Teacher with id 999 does not exist.")

```