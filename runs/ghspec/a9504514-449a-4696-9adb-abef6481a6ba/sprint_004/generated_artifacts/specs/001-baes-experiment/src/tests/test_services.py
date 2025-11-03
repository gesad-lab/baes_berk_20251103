```python
import unittest
from src.services import create_course, get_all_courses, enroll_student_in_course, get_student_courses
from src.models import Course, Student
from src.database import db, init_db

class TestCourseServices(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the testing database and create necessary tables."""
        init_db()
        cls.app_context = db.app.app_context()
        cls.app_context.push()

        # Create a sample course and student for testing
        cls.sample_course = Course(name="Biology 101", level="Undergraduate")
        cls.sample_student = Student(name="John Doe")

        db.session.add(cls.sample_course)
        db.session.add(cls.sample_student)
        db.session.commit()

    @classmethod
    def tearDownClass(cls):
        """Clean up after tests."""
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def test_enroll_student_in_course(self):
        """Test enrolling a student in a course successfully."""
        response = enroll_student_in_course(self.sample_student.id, self.sample_course.id)
        self.assertEqual(response['student_id'], self.sample_student.id)
        self.assertEqual(response['course_id'], self.sample_course.id)

    def test_get_student_courses(self):
        """Test retrieval of courses for a given student."""
        enroll_student_in_course(self.sample_student.id, self.sample_course.id)  # Enroll the student first
        
        courses = get_student_courses(self.sample_student.id)
        self.assertEqual(len(courses), 1)
        self.assertEqual(courses[0]['id'], self.sample_course.id)

    def test_enroll_invalid_student(self):
        """Test handling of enrollment for a non-existent student."""
        with self.assertRaises(ValueError) as context:
            enroll_student_in_course(9999, self.sample_course.id)  # Assuming 9999 does not exist
        self.assertEqual(str(context.exception), "Student not found.")

    def test_enroll_invalid_course(self):
        """Test handling of enrollment for a non-existent course."""
        with self.assertRaises(ValueError) as context:
            enroll_student_in_course(self.sample_student.id, 9999)  # Assuming 9999 does not exist
        self.assertEqual(str(context.exception), "Course not found.")

if __name__ == '__main__':
    unittest.main()
```