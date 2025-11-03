```python
import unittest
from main import app, db
from models import Student

class ApiTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the test client and database before any tests."""
        cls.app = app.test_client()
        cls.app.testing = True
        with app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        """Clean up the database after tests are run."""
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_student_with_valid_email(self):
        """Test creating a student with a valid email."""
        response = self.app.post('/api/students', json={
            'name': 'John Doe',
            'email': 'john.doe@example.com'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('student', response.json)

    def test_create_student_with_invalid_email(self):
        """Test creating a student with an invalid email format."""
        response = self.app.post('/api/students', json={
            'name': 'Jane Doe',
            'email': 'jane.doe@.com'
        })
        self.assertEqual(response.status_code, 400)  # Bad Request
        self.assertIn('error', response.json)

    def test_retrieve_student(self):
        """Test retrieving a student by ID after creation."""
        # First create a student
        create_response = self.app.post('/api/students', json={
            'name': 'Alice Smith',
            'email': 'alice.smith@example.com'
        })
        student_id = create_response.json['student']['id']

        # Now retrieve the student
        retrieve_response = self.app.get(f'/api/students/{student_id}')
        self.assertEqual(retrieve_response.status_code, 200)
        self.assertEqual(retrieve_response.json['student']['id'], student_id)

    def test_retrieve_nonexistent_student(self):
        """Test retrieving a student that does not exist."""
        response = self.app.get('/api/students/99999')  # Assuming this ID does not exist
        self.assertEqual(response.status_code, 404)  # Not Found
        self.assertIn('error', response.json)

if __name__ == '__main__':
    unittest.main()
```