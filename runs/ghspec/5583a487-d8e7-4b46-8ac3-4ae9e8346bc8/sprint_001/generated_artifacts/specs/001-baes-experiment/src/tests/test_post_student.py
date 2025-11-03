import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Assuming the Flask app and database have been set up correctly

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

# Sample Student Model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

# Create Student Endpoint
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    
    if not data or 'name' not in data:
        return jsonify({
            'error': {
                'code': 'E001',
                'message': 'Name field is required.'
            }
        }), 400

    new_student = Student(name=data['name'])
    db.session.add(new_student)
    db.session.commit()

    return jsonify({'message': 'Student created successfully.'}), 201

# Tests for the POST /students endpoint
def test_create_student_success(client):
    response = client.post('/students', json={'name': 'John Doe'})
    assert response.status_code == 201
    assert response.get_json() == {'message': 'Student created successfully.'}

def test_create_student_missing_name(client):
    response = client.post('/students', json={})
    assert response.status_code == 400
    assert response.get_json() == {
        'error': {
            'code': 'E001',
            'message': 'Name field is required.'
        }
    }

@pytest.fixture
def client():
    with app.test_client() as client:
        db.create_all()  # Create tables
        yield client
        db.drop_all()  # Clean up after tests

# This file is a complete test file for the POST /students endpoint
# The tests validate successful creation and error handling for missing name field.