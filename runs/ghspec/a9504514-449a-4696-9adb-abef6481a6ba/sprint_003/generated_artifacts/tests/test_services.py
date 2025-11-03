```python
import unittest
from src.services import create_course, get_all_courses
from src.models import Course
from src.database import db, init_db

class TestCourseServices(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the testing database and create necessary tables."""
        init_db()
        cls.app_context = db.app.app_context()
        cls.app_context.push()

        # Create a sample course for testing retrieval
        cls.sample_course = Course(name="Mathematics", level="Beginner")
        db.session.add(cls.sample_course)
        db.session.commit()

    @classmethod
    def tearDownClass(cls):
        """Teardown app context and drop the testing database."""
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def test_create_course_success(self):
        """Test that a course is created successfully with valid data."""
        response = create_course(name="Physics", level="Intermediate")
        self.assertTrue(response['success'])
        self.assertEqual(response['course']['name'], "Physics")
        self.assertEqual(response['course']['level'], "Intermediate")

    def test_create_course_missing_name(self):
        """Test that attempting to create a course without a name fails."""
        response = create_course(name="", level="Advanced")
        self.assertFalse(response['success'])
        self.assertIn('error', response)
        self.assertEqual(response['error'], "Course name is required.")

    def test_create_course_missing_level(self):
        """Test that attempting to create a course without a level fails."""
        response = create_course(name="Chemistry", level="")
        self.assertFalse(response['success'])
        self.assertIn('error', response)
        self.assertEqual(response['error'], "Course level is required.")

    def test_get_all_courses(self):
        """Test that all courses are retrieved successfully."""
        response = get_all_courses()
        self.assertTrue(isinstance(response, list))
        self.assertGreater(len(response), 0)
        self.assertEqual(response[0]['name'], self.sample_course.name)
        self.assertEqual(response[0]['level'], self.sample_course.level)
```