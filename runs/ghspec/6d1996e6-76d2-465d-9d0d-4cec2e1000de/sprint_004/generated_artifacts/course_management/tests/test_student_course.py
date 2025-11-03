# tests/test_student_course.py

import unittest
from flask import json
from app import app  # Application instance
from db.database import db_session
from models.student import Student  # Assuming Student model is imported
from models.course import Course  # Assuming Course model is imported
from models.student_course import StudentCourse  # New model for student-course relationship

class StudentCourseAPITestCase(unittest.TestCase):
    def setUp(self):
        """Set up a test client and a clean database."""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        
        # Clear the database session and setup mock data.
        db_session.remove()
        db_session.bind.engine.execute("TRUNCATE TABLE student_course RESTART IDENTITY CASCADE")
        db_session.bind.engine.execute("TRUNCATE TABLE students RESTART IDENTITY CASCADE")
        db_session.bind.engine.execute("TRUNCATE TABLE courses RESTART IDENTITY CASCADE")
        
        # Create a test student and course
        self.student = Student(name="Test Student")
        self.course = Course(title="Test Course")
        
        db_session.add(self.student)
        db_session.add(self.course)
        db_session.commit()

    def tearDown(self):
        """Clean up the database session."""
        db_session.remove()
    
    def test_enroll_student_in_course(self):
        """Test enrolling a student in a course."""
        response = self.client.post(f'/api/enroll', json={
            'student_id': self.student.id,
            'course_id': self.course.id
        })
        self.assertEqual(response.status_code, 201)  # Check if enrollment was successful
        
        # Verify if the association is created in the database
        self.assertEqual(StudentCourse.query.count(), 1)

    def test_enroll_student_invalid_student(self):
        """Test enrollment with a non-existent student ID."""
        response = self.client.post(f'/api/enroll', json={
            'student_id': 999,  # Non-existent student ID
            'course_id': self.course.id
        })
        self.assertEqual(response.status_code, 404)  # Expecting Not Found
        self.assertIn("Student not found", str(response.data))  # Check error message

    def test_enroll_student_invalid_course(self):
        """Test enrollment with a non-existent course ID."""
        response = self.client.post(f'/api/enroll', json={
            'student_id': self.student.id,
            'course_id': 999  # Non-existent course ID
        })
        self.assertEqual(response.status_code, 404)  # Expecting Not Found
        self.assertIn("Course not found", str(response.data))  # Check error message

    def test_retrieve_student_with_courses(self):
        """Test retrieving student information along with enrolled courses."""
        # First, enroll the student in the course
        self.client.post(f'/api/enroll', json={
            'student_id': self.student.id,
            'course_id': self.course.id
        })

        response = self.client.get(f'/api/students/{self.student.id}')
        self.assertEqual(response.status_code, 200)  # Check successful retrieval
        data = json.loads(response.data)
        self.assertEqual(data['name'], self.student.name)
        self.assertTrue(len(data['courses']) > 0)  # Verify courses association

    def test_unenroll_student_from_course(self):
        """Test unenrolling a student from a course."""
        # First, enroll the student in the course
        self.client.post(f'/api/enroll', json={
            'student_id': self.student.id,
            'course_id': self.course.id
        })
        
        response = self.client.delete(f'/api/unenroll', json={
            'student_id': self.student.id,
            'course_id': self.course.id
        })
        self.assertEqual(response.status_code, 204)  # Expect No Content on successful unenroll
        
        # Verify if the association is removed in the database
        self.assertEqual(StudentCourse.query.count(), 0)

if __name__ == '__main__':
    unittest.main()