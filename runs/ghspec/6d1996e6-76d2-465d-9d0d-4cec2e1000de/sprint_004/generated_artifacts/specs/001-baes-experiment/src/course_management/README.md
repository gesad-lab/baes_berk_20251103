# tests/test_student_course.py

import unittest
from flask import json
from app import app  # Assuming app is defined in app.py
from db.database import db_session
from models.student import Student  # Assuming Student model is imported
from models.course import Course  # Assuming Course model is imported
from models.student_course import StudentCourse  # Importing the StudentCourse model

class StudentCourseAPITestCase(unittest.TestCase):
    def setUp(self):
        """Set up a test client and a clean database."""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

        with self.app.app_context():
            # Create a new test database and sample data
            db_session.create_all()
            self.student = Student(name="Test Student")
            self.course = Course(name="Test Course")
            db_session.add(self.student)
            db_session.add(self.course)
            db_session.commit()

            # Enroll student in the course for testing unenrollment
            db_session.add(StudentCourse(student_id=self.student.id, course_id=self.course.id))
            db_session.commit()

    def tearDown(self):
        """Clean up database after tests."""
        with self.app.app_context():
            db_session.remove()
            db_session.drop_all()

    def test_unenroll_student_from_course(self):
        """Test unenrolling a student from a course successfully."""
        response = self.client.delete(f'/students/{self.student.id}/courses/{self.course.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'confirmed the removal', response.data)

        # Verify the student no longer enrolled in the course
        student_courses = StudentCourse.query.filter_by(student_id=self.student.id).all()
        self.assertEqual(len(student_courses), 0)

    def test_unenroll_student_from_nonexistent_course(self):
        """Test attempting to unenroll a student from a course that does not exist."""
        response = self.client.delete(f'/students/{self.student.id}/courses/999')
        self.assertEqual(response.status_code, 404)

    def test_unenroll_nonexistent_student(self):
        """Test attempting to unenroll a nonexistent student from a course."""
        response = self.client.delete('/students/999/courses/1')  # Assume course ID 1 exists
        self.assertEqual(response.status_code, 404)

    def test_unenroll_student_without_course_enrollment(self):
        """Test attempting to unenroll a student who is not enrolled in the specified course."""
        # Create a course but do not enroll the student
        new_course = Course(name="Another Course")
        db_session.add(new_course)
        db_session.commit()

        response = self.client.delete(f'/students/{self.student.id}/courses/{new_course.id}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()