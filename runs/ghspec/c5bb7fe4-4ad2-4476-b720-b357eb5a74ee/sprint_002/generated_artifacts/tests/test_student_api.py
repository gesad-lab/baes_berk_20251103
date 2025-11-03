```python
import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from src.models import Student  # Import the existing Student model
from sqlalchemy.exc import IntegrityError

# Initialize Flask app and db for testing
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for tests
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create all database tables for testing
with app.app_context():
    db.create_all()

@app.route('/students', methods=['POST'])
def create_student():
    """Create a new student with name and email."""
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"error": {"code": "E001", "message": "Name and Email are required."}}), 400

    student = Student(name=name, email=email)
    db.session.add(student)
    db.session.commit()
    return jsonify({"id": student.id, "name": student.name, "email": student.email}), 201

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    """Update an existing student's email."""
    data = request.get_json()
    email = data.get('email')

    student = Student.query.get_or_404(student_id)
    if email:
        student.email = email
        db.session.commit()
        return jsonify({"id": student.id, "name": student.name, "email": student.email}), 200

    return jsonify({"error": {"code": "E001", "message": "Email is required."}}), 400

@app.route('/students', methods=['GET'])
def get_students():
    """Retrieve all students."""
    students = Student.query.all()
    return jsonify([{"id": student.id, "name": student.name, "email": student.email} for student in students]), 200


def test_create_student_with_email(test_client):
    """Test creating a new student with email successfully."""
    response = test_client.post('/students', json={"name": "Alice Wonderland", "email": "alice@example.com"})
    data = response.get_json()
    assert response.status_code == 201
    assert data['name'] == "Alice Wonderland"
    assert data['email'] == "alice@example.com"


def test_update_student_email(test_client):
    """Test updating a student's email successfully."""
    # First create a student to update
    response = test_client.post('/students', json={"name": "Bob Builder", "email": "bob@example.com"})
    student_id = response.get_json()['id']

    # Now update that student's email
    response = test_client.put(f'/students/{student_id}', json={"email": "bob@builder.com"})
    data = response.get_json()
    assert response.status_code == 200
    assert data['email'] == "bob@builder.com"


def test_retrieve_students(test_client):
    """Test retrieving all students to ensure email is included."""
    test_client.post('/students', json={"name": "Charlie Chaplin", "email": "charlie@example.com"})
    test_client.post('/students', json={"name": "Daisy Duck", "email": "daisy@example.com"})
    
    response = test_client.get('/students')
    data = response.get_json()
    
    assert response.status_code == 200
    assert len(data) == 2
    assert any(student['name'] == "Charlie Chaplin" and student['email'] == "charlie@example.com" for student in data)
    assert any(student['name'] == "Daisy Duck" and student['email'] == "daisy@example.com" for student in data)
```