```python
import unittest
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

# Error handling for when a student is not found
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": {
            "code": "E002",
            "message": "Student not found"
        }
    }), 404

# Endpoint to retrieve a Student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get(id)  # Fetch the student by the provided ID
    if not student:
        return not_found(404)  # Return a 404 response if student is not found
    return jsonify({"id": student.id, "name": student.name})

# Test case for student retrieval
class StudentManagementAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        db.create_all()  # Create the database schema
        self.sample_student = Student(name="John Doe")
        db.session.add(self.sample_student)  # Add a sample student for testing
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()  # Drop the database schema after tests

    def test_get_student_not_found(self):
        # Test retrieving a student with a non-existent ID
        response = self.app.get('/students/999')  # Use an ID that does not exist
        self.assertEqual(response.status_code, 404)  # Expect a 404 status code
        self.assertEqual(response.get_json(), {
            "error": {
                "code": "E002",
                "message": "Student not found"
            }
        })  # Expect the correct error message

# Entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```