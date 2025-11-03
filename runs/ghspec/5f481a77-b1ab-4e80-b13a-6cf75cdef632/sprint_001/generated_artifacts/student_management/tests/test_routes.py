```python
import json
import unittest
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application and a SQLAlchemy instance for testing purposes
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

# Sample Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

# Sample route for creating a Student
@app.route('/students', methods=['POST'])
def create_student():
    data = request.json
    name = data.get('name')

    if not name:
        return json.dumps({
            "error": {
                "code": "E001",
                "message": "Name is required."
            }
        }), 400

    student = Student(name=name)
    db.session.add(student)
    db.session.commit()
    return json.dumps({"message": "Student created", "student": {"id": student.id, "name": student.name}}), 201

# Test case class for the routes
class TestStudentRoutes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a test client
        cls.app = app.test_client()
        # Create the database schema in memory
        with app.app_context():
            db.create_all()

    def test_create_student_with_valid_name(self):
        # Test successful creation of a student with valid input
        response = self.app.post('/students', json={'name': 'John Doe'})
        self.assertEqual(response.status_code, 201)
        response_json = json.loads(response.data)
        self.assertIn('message', response_json)
        self.assertEqual(response_json['message'], 'Student created')
        self.assertIn('student', response_json)
        self.assertEqual(response_json['student']['name'], 'John Doe')

    def test_create_student_without_name(self):
        # Test for error when creating a student without a name
        response = self.app.post('/students', json={})
        self.assertEqual(response.status_code, 400)
        response_json = json.loads(response.data)
        self.assertIn('error', response_json)
        self.assertEqual(response_json['error']['code'], 'E001')
        self.assertEqual(response_json['error']['message'], 'Name is required.')

if __name__ == '__main__':
    unittest.main()
```