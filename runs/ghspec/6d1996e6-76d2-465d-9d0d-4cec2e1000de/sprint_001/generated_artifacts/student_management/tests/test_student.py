```python
import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Creating a Flask application instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Defining Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


# Create the database schema on startup
@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400
    new_student = Student(name=data['name'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'id': new_student.id, 'name': new_student.name}), 201


@app.route('/students/<int:id>', methods=['GET'])
def retrieve_student(id):
    student = Student.query.get(id)
    if student is None:
        return jsonify({'error': 'Student not found'}), 404
    return jsonify({'id': student.id, 'name': student.name}), 200


@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400
    student = Student.query.get(id)
    if student is None:
        return jsonify({'error': 'Student not found'}), 404
    student.name = data['name']
    db.session.commit()
    return jsonify({'id': student.id, 'name': student.name}), 200


@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    if student is None:
        return jsonify({'error': 'Student not found'}), 404
    db.session.delete(student)
    db.session.commit()
    return '', 204


@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create tables
        yield client
        db.drop_all()  # Clean up after tests


def test_create_student(client):
    response = client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 201
    assert 'id' in response.json
    assert response.json['name'] == 'John Doe'


def test_retrieve_student(client):
    # Create a student to retrieve
    create_response = client.post('/students', json={'name': 'Jane Doe'})
    student_id = create_response.json['id']
    
    response = client.get(f'/students/{student_id}')
    assert response.status_code == 200
    assert response.json['name'] == 'Jane Doe'


def test_update_student(client):
    create_response = client.post('/students', json={'name': 'Joe Smith'})
    student_id = create_response.json['id']
    
    response = client.put(f'/students/{student_id}', json={'name': 'Joseph Smith'})
    assert response.status_code == 200
    assert response.json['name'] == 'Joseph Smith'


def test_delete_student(client):
    create_response = client.post('/students', json={'name': 'Emily Johnson'})
    student_id = create_response.json['id']
    
    response = client.delete(f'/students/{student_id}')
    assert response.status_code == 204
    # Verify that the student was deleted
    response = client.get(f'/students/{student_id}')
    assert response.status_code == 404


def test_create_student_missing_name(client):
    response = client.post('/students', json={'age': 25})
    assert response.status_code == 400
    assert response.json['error'] == 'Name is required'


def test_retrieve_nonexistent_student(client):
    response = client.get('/students/999')  # A non-existent student ID
    assert response.status_code == 404
    assert response.json['error'] == 'Student not found'


def test_update_nonexistent_student(client):
    response = client.put('/students/999', json={'name': 'New Name'})
    assert response.status_code == 404
    assert response.json['error'] == 'Student not found'


def test_delete_nonexistent_student(client):
    response = client.delete('/students/999')  # Trying to delete a non-existent student
    assert response.status_code == 404
    assert response.json['error'] == 'Student not found'
```