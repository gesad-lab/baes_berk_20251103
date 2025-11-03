```python
import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from src.models import Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)  # Added email field

# Create the database schema
@app.before_first_request
def create_tables():
    db.create_all()

# Create student route
@app.route('/students', methods=['POST'])
def create_student():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    
    # Validate name presence
    if not name:
        return jsonify({"error": {"code": "E001", "message": "Name is required"}}), 400

    # Validate email presence and format here
    if not email or "@" not in email:
        return jsonify({"error": {"code": "E002", "message": "Invalid email format"}}), 400
    
    student = Student(name=name, email=email)
    try:
        db.session.add(student)
        db.session.commit()
        return jsonify({"id": student.id, "name": student.name, "email": student.email}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": {"code": "E003", "message": "Email must be unique"}}), 400

# Retrieve student route
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get(id)
    if not student:
        return jsonify({"error": {"code": "E004", "message": "Student not found"}}), 404
    return jsonify({"id": student.id, "name": student.name, "email": student.email}), 200


def test_create_student(db_session):
    """Test creating a student with valid data."""
    new_student = Student(name="John Doe", email="john.doe@example.com")
    db_session.add(new_student)
    db_session.commit()

    # Assert that the student was created
    retrieved_student = Student.query.filter_by(email="john.doe@example.com").first()
    assert retrieved_student is not None
    assert retrieved_student.name == "John Doe"

def test_create_student_without_email(db_session):
    """Test creating a student without an email."""
    response = app.test_client().post('/students', json={"name": "Jane Doe"})
    assert response.status_code == 400
    assert response.json['error']['code'] == "E002"

def test_create_student_with_duplicate_email(db_session):
    """Test creating a student with a duplicate email."""
    student1 = Student(name="John Doe", email="john.doe@example.com")
    db_session.add(student1)
    db_session.commit()

    response = app.test_client().post('/students', json={"name": "Jane Doe", "email": "john.doe@example.com"})
    assert response.status_code == 400
    assert response.json['error']['code'] == "E003"

def test_retrieve_student(db_session):
    """Test retrieving an existing student."""
    new_student = Student(name="Alice Smith", email="alice.smith@example.com")
    db_session.add(new_student)
    db_session.commit()

    response = app.test_client().get(f'/students/{new_student.id}')
    assert response.status_code == 200
    assert response.json['name'] == "Alice Smith"
    assert response.json['email'] == "alice.smith@example.com"

def test_retrieve_non_existent_student(db_session):
    """Test retrieving a non-existent student."""
    response = app.test_client().get('/students/999')
    assert response.status_code == 404
    assert response.json['error']['code'] == "E004"
```