```python
# tests/test_course.py

import unittest
from flask import json
from app import app  # Assuming app is defined in app.py
from db.database import db_session
from models.course import Course  # Assuming Course model is imported

class CourseAPITestCase(unittest.TestCase):
    def setUp(self):
        """Set up a test client and a clean database."""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        
        # Create a new course for testing
        with self.app.app_context():
            db_session.begin()
            db_session.execute('DELETE FROM courses')  # Clear existing courses
            db_session.commit()

    def tearDown(self):
        """Clean up after each test."""
        with self.app.app_context():
            db_session.execute('DELETE FROM courses')  # Clear existing courses
            db_session.commit()

    def test_create_course(self):
        """Test creating a new course."""
        response = self.client.post('/courses', 
                                     data=json.dumps({'name': 'Mathematics', 'level': 'Beginner'}),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertIn('id', data)  # Ensure the response includes an ID
        self.assertEqual(data['name'], 'Mathematics')
        self.assertEqual(data['level'], 'Beginner')

    def test_retrieve_course(self):
        """Test retrieving a course by ID."""
        # First, create a course to retrieve
        create_response = self.client.post('/courses', 
                                            data=json.dumps({'name': 'Physics', 'level': 'Intermediate'}),
                                            content_type='application/json')
        course_id = json.loads(create_response.data)['id']

        # Now, retrieve the course
        response = self.client.get(f'/courses/{course_id}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'Physics')
        self.assertEqual(data['level'], 'Intermediate')

    def test_retrieve_nonexistent_course(self):
        """Test retrieving a course that does not exist."""
        response = self.client.get('/courses/99999')  # Assume this ID does not exist
        self.assertEqual(response.status_code, 404)

    def test_update_course(self):
        """Test updating an existing course."""
        # First, create a course to update
        create_response = self.client.post('/courses', 
                                            data=json.dumps({'name': 'Biology', 'level': 'Advanced'}),
                                            content_type='application/json')
        course_id = json.loads(create_response.data)['id']

        # Now, update the course
        update_response = self.client.put(f'/courses/{course_id}', 
                                           data=json.dumps({'name': 'Updated Biology'}),
                                           content_type='application/json')
        self.assertEqual(update_response.status_code, 200)
        updated_data = json.loads(update_response.data)
        self.assertEqual(updated_data['name'], 'Updated Biology')
        self.assertEqual(updated_data['level'], 'Advanced')  # Ensure level remains unchanged

    def test_update_nonexistent_course(self):
        """Test updating a course that does not exist."""
        response = self.client.put('/courses/99999', 
                                    data=json.dumps({'name': 'Random Course'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
```