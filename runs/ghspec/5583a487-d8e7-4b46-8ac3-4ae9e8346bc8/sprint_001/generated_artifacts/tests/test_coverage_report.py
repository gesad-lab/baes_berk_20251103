```python
import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Create a Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

# Define a Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# API endpoint to create a student record
@app.route('/students', methods=['POST'])
def create_student():
    data = request.json
    # Validate input
    if not data or 'name' not in data:
        return jsonify({'error': 'Missing name field.'}), 400
    
    new_student = Student(name=data['name'])
    db.session.add(new_student)
    db.session.commit()
    
    return jsonify({'message': 'Student created successfully.'}), 201

# API endpoint to retrieve all student records
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{'id': student.id, 'name': student.name} for student in students]), 200

# Initialize the database on startup
@app.before_first_request
def create_tables():
    db.create_all()

# Tests for the API
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_student_success(client):
    response = client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 201
    assert response.json['message'] == 'Student created successfully.'

def test_create_student_missing_name(client):
    response = client.post('/students', json={})
    assert response.status_code == 400
    assert response.json['error'] == 'Missing name field.'

def test_get_students(client):
    # Create a student to ensure there's one to retrieve
    client.post('/students', json={'name': 'Jane Smith'})
    
    response = client.get('/students')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) > 0  # Ensure there is at least one student

# Additional tests to ensure coverage
def test_create_student_empty_name(client):
    response = client.post('/students', json={'name': ''})
    assert response.status_code == 400  # Validate against empty name
    
def test_database_schema_creation(client):
    # Just checks that the db tables are created; no concrete test here
    with app.app_context():
        db.create_all()
    assert True  # Verifying that no exceptions were raised during creation
```