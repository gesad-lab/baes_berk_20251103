import pytest
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from src.models.teacher import Teacher  # Importing the Teacher model
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

# Fixture to set up a test database session
@pytest.fixture
def db_session():
    """Create a new database session for a test."""
    with app.app_context():
        db.create_all()  # Create database tables
        yield db.session  # Provide the session to the test
        db.drop_all()  # Clean up the database after tests

@app.route('/api/v1/teachers', methods=['POST'])
def create_teacher():
    """Create a new teacher."""
    data = request.json
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': {'code': 'E001', 'message': 'Name and email are required.'}}), 400
    teacher = Teacher(name=data['name'], email=data['email'])
    db.session.add(teacher)
    db.session.commit()
    return jsonify({'id': teacher.id, 'name': teacher.name, 'email': teacher.email}), 201

@app.route('/api/v1/teachers/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
    """Retrieve teacher information by ID."""
    teacher = Teacher.query.get(teacher_id)
    if not teacher:
        return jsonify({'error': {'code': 'E002', 'message': 'Teacher not found.'}}), 404
    return jsonify({'id': teacher.id, 'name': teacher.name, 'email': teacher.email}), 200

# Example requests and responses for the teacher API endpoints
def test_create_teacher(db_session):
    """Test creating a teacher with valid data."""
    response = app.test_client().post('/api/v1/teachers', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    assert response.status_code == 201
    assert response.json == {
        'id': 1,
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }

def test_create_teacher_with_missing_fields(db_session):
    """Test creating a teacher with missing name or email."""
    response = app.test_client().post('/api/v1/teachers', json={
        'name': ''
    })
    assert response.status_code == 400
    assert response.json == {'error': {'code': 'E001', 'message': 'Name and email are required.'}}

def test_get_teacher(db_session):
    """Test retrieving teacher information by ID."""
    teacher = Teacher(name='Jane Doe', email='jane.doe@example.com')
    db_session.add(teacher)
    db_session.commit()

    response = app.test_client().get(f'/api/v1/teachers/{teacher.id}')
    assert response.status_code == 200
    assert response.json == {
        'id': teacher.id,
        'name': 'Jane Doe',
        'email': 'jane.doe@example.com'
    }

def test_get_nonexistent_teacher(db_session):
    """Test retrieving information for a nonexistent teacher."""
    response = app.test_client().get('/api/v1/teachers/99999')
    assert response.status_code == 404
    assert response.json == {'error': {'code': 'E002', 'message': 'Teacher not found.'}}