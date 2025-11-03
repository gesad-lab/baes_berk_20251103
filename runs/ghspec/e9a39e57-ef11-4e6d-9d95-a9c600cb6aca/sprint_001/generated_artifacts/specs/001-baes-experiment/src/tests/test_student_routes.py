import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

# Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

# Create the database schema
@app.before_first_request
def create_tables():
    db.create_all()

# Create student route
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({"error": "Name is required"}), 400
    
    student = Student(name=name)
    db.session.add(student)
    db.session.commit()
    return jsonify({"id": student.id, "name": student.name}), 201

# Retrieve student by ID route
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get(id)
    if student is None:
        return jsonify({"error": "Student not found"}), 404
    return jsonify({"id": student.id, "name": student.name})

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture
def init_database():
    db.create_all()
    yield
    db.drop_all()

def test_create_student(client, init_database):
    response = client.post('/students', json={"name": "John Doe"})
    assert response.status_code == 201
    assert response.get_json() == {"id": 1, "name": "John Doe"}

def test_get_student(client, init_database):
    # First create a student to retrieve
    create_response = client.post('/students', json={"name": "Jane Doe"})
    student_id = create_response.get_json()['id']

    # Now, retrieve the student by ID
    response = client.get(f'/students/{student_id}')
    assert response.status_code == 200
    assert response.get_json() == {"id": student_id, "name": "Jane Doe"}

def test_get_student_not_found(client, init_database):
    response = client.get('/students/999')
    assert response.status_code == 404
    assert response.get_json() == {"error": "Student not found"}