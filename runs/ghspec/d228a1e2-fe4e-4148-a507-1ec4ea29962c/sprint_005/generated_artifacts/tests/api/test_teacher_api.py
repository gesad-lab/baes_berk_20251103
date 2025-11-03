```python
import pytest
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Import the Teacher model from app/models.py (Assumed to be already defined in the project)
from app.models import Teacher

# Create the test client
@pytest.fixture
def client():
    db.create_all()  # Create database tables
    yield app.test_client()  # Provide the test client
    db.drop_all()  # Clean up after tests

def create_teacher(client, name, email):
    """Helper function to create a teacher for testing."""
    return client.post('/teachers', json={'name': name, 'email': email})

def test_create_teacher(client):
    """Test creating a new teacher."""
    response = create_teacher(client, 'John Doe', 'john.doe@example.com')
    assert response.status_code == 201  # HTTP Status 201 Created
    assert response.get_json() == {'success': True}

def test_create_teacher_with_invalid_email(client):
    """Test creating a new teacher with an invalid email."""
    response = create_teacher(client, 'Jane Doe', 'invalid-email-format')
    assert response.status_code == 400  # HTTP Status 400 Bad Request
    assert response.get_json() == {'error': {'code': 'E001', 'message': 'Invalid email format'}}  

def test_get_teacher_details(client):
    """Test retrieving details of a teacher that exists."""
    create_teacher(client, 'Alice Smith', 'alice.smith@example.com')  # Create a teacher to retrieve
    teacher = Teacher.query.first()  # Get the first teacher to retrieve its details
    response = client.get(f'/teachers/{teacher.id}')
    assert response.status_code == 200  # HTTP Status 200 OK
    assert response.get_json() == {'id': teacher.id, 'name': teacher.name, 'email': teacher.email}

def test_get_teacher_details_not_found(client):
    """Test getting details of a teacher that does not exist."""
    response = client.get('/teachers/99999')  # Assume this ID doesn't exist
    assert response.status_code == 404  # HTTP Status 404 Not Found
    assert response.get_json() == {'error': {'code': 'E002', 'message': 'Teacher not found'}}  
```