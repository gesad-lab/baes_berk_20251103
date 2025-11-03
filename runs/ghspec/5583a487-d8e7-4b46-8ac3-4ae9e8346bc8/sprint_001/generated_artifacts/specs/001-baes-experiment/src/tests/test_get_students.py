import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application for testing
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Define the API route to get all students
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{'id': student.id, 'name': student.name} for student in students]), 200

# Test cases for the GET /students endpoint
def test_get_students_empty():
    """Test that GET /students returns an empty list when no students exist."""
    response = app.test_client().get('/students')
    assert response.status_code == 200
    assert response.json == []

def test_get_students_with_data():
    """Test that GET /students returns a list of all students when they exist."""
    # Add sample data
    student1 = Student(name='John Doe')
    student2 = Student(name='Jane Smith')
    db.session.add(student1)
    db.session.add(student2)
    db.session.commit()

    response = app.test_client().get('/students')
    assert response.status_code == 200
    assert response.json == [
        {'id': student1.id, 'name': 'John Doe'},
        {'id': student2.id, 'name': 'Jane Smith'}
    ]

def test_get_students_invalid_response_format():
    """Test that GET /students response format is correct."""
    response = app.test_client().get('/students')
    assert response.content_type == 'application/json'
    assert isinstance(response.json, list)

@pytest.mark.parametrize("student_data,expected_length", [
    ([], 0),
    ([{'name': 'Alice'}], 1),
    ([{'name': 'Bob'}, {'name': 'Charlie'}], 2)
])
def test_get_students_variable_data(student_data, expected_length):
    """Test that GET /students can handle varying amounts of student data."""
    for student in student_data:
        new_student = Student(name=student['name'])
        db.session.add(new_student)
    db.session.commit()

    response = app.test_client().get('/students')
    assert response.status_code == 200
    assert len(response.json) == expected_length