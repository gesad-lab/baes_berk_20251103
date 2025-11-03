```python
import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Sample app and DB setup for the purpose of testing
app = Flask(__name__)
app.config['TESTING'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory database for testing
db = SQLAlchemy(app)

# Example models to simulate a student management system
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)

# Create a test route to add a student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(name=data['name'], age=data['age'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'id': new_student.id}), 201

# Create a test route to get all students
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{'id': student.id, 'name': student.name, 'age': student.age} for student in students]), 200

# Initialize the database before each test
@pytest.fixture(scope='module')
def test_app():
    with app.app_context():
        db.create_all()  # Create the database
        yield app
        db.drop_all()  # Clean up database

@pytest.fixture(scope='function')
def client(test_app):
    return test_app.test_client()

def test_add_student(client):
    response = client.post('/students', json={'name': 'John Doe', 'age': 21})
    assert response.status_code == 201
    assert 'id' in response.json

def test_get_students(client):
    client.post('/students', json={'name': 'John Doe', 'age': 21})  # Add a student
    response = client.get('/students')
    assert response.status_code == 200
    assert len(response.json) > 0
    assert response.json[0]['name'] == 'John Doe'
    assert response.json[0]['age'] == 21
```