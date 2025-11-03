import json
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Creating a Flask app and configuring SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Student
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)

# Create the database and the Student table
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to create a student
@app.route('/students', methods=['POST'])
def create_student():
    data = json.loads(request.data)
    name = data.get('name')
    
    # Input validation: name is required
    if not name:
        return {'error': {'code': 'E001', 'message': 'Name is required'}}, 400
    
    new_student = Student(name=name)
    db.session.add(new_student)
    db.session.commit()
    
    return {'message': 'Student created', 'id': new_student.id, 'name': new_student.name}, 201

# API endpoint to retrieve all students
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return [{'id': student.id, 'name': student.name} for student in students], 200

# API endpoint to retrieve a student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return {'error': {'code': 'E002', 'message': 'Student not found'}}, 404
    return {'id': student.id, 'name': student.name}, 200

# Test cases for Student routes
@pytest.mark.parametrize('name, expected_status', [
    ('John Doe', 201),
    ('', 400),
])
def test_create_student(client, name, expected_status):
    response = client.post('/students', json={'name': name})
    assert response.status_code == expected_status

def test_retrieve_all_students(client):
    client.post('/students', json={'name': 'John Doe'})
    client.post('/students', json={'name': 'Jane Doe'})
    response = client.get('/students')
    assert response.status_code == 200
    assert len(response.json) == 2

def test_retrieve_student_by_id(client):
    response = client.post('/students', json={'name': 'John Doe'})
    student_id = response.json['id']
    response = client.get(f'/students/{student_id}')
    assert response.status_code == 200
    assert response.json['name'] == 'John Doe'

def test_retrieve_nonexistent_student_fails(client):
    response = client.get('/students/999')
    assert response.status_code == 404
    assert response.json['error']['code'] == 'E002'

# Test Initial Setup
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
```

In this file, I have implemented how to test the create student functionality and handled the various cases as described in the specifications. Each test case corresponds to the provided scenarios including creating a student, retrieving all students, and validating input for empty names.