```python
import unittest
from src.services import create_student, get_student_by_id, get_all_students, create_course, get_all_courses
from src.models import Student, Course
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
        """Teardown app context after tests."""
        cls.app_context.pop()

    def test_create_student(self):
        # Ensure a student can be created successfully
        student_data = {'name': 'John Doe', 'age': 20}
        response = create_student(student_data)
        self.assertTrue(response['success'])
        self.assertEqual(response['student']['name'], student_data['name'])

    def test_get_student_by_id(self):
        # Verify that getting a student by ID returns the correct student
        student_data = {'name': 'Jane Doe', 'age': 22}
        create_student(student_data)
        student = get_student_by_id(1)  # Assuming the student has ID 1
        self.assertEqual(student['name'], student_data['name'])

    def test_get_all_students(self):
        # Verify retrieval of all students is accurate
        students = get_all_students()
        self.assertGreater(len(students), 0)

# New tests for Course retrieval
class TestCourseServices(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the testing database and create necessary tables."""
        init_db()
        cls.app_context = db.app.app_context()
        cls.app_context.push()

    @classmethod
    def tearDownClass(cls):
        """Teardown app context after tests."""
        cls.app_context.pop()

    def test_create_course(self):
        # Ensure a course can be created successfully
        course_data = {'name': 'Mathematics', 'level': 'Beginner'}
        response = create_course(course_data)
        self.assertTrue(response['success'])
        self.assertEqual(response['course']['name'], course_data['name'])
        self.assertEqual(response['course']['level'], course_data['level'])

    def test_get_all_courses(self):
        # Verify retrieval of all courses is accurate
        course_data1 = {'name': 'Mathematics', 'level': 'Beginner'}
        course_data2 = {'name': 'Physics', 'level': 'Intermediate'}
        create_course(course_data1)
        create_course(course_data2)
        courses = get_all_courses()
        self.assertGreater(len(courses), 0)
        self.assertIn(course_data1, courses)
        self.assertIn(course_data2, courses)

    def test_create_course_validation(self):
        # Ensure validation correctly identifies missing fields
        course_data = {'name': '', 'level': 'Advanced'}
        response = create_course(course_data)
        self.assertFalse(response['success'])
        self.assertIn('error', response)  # Assuming the response has an error field
        self.assertEqual(response['error'], "Name is required.")

        course_data = {'name': 'Chemistry', 'level': ''}
        response = create_course(course_data)
        self.assertFalse(response['success'])
        self.assertIn('error', response)
        self.assertEqual(response['error'], "Level is required.")
```