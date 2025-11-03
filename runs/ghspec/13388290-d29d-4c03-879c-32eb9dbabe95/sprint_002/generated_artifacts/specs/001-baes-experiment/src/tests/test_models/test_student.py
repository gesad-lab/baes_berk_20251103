```python
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import Student

# Setup Flask and SQLAlchemy for testing
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create the database schema for testing
with app.app_context():
    db.create_all()

def test_create_student_with_email(client):
    """Test successful creation of a student with a valid name and email."""
    response = client.post('/students', json={'name': 'John Doe', 'email': 'john.doe@example.com'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'John Doe'
    assert data['email'] == 'john.doe@example.com'

def test_create_student_without_email(client):
    """Test creation of a student that fails due to missing email."""
    response = client.post('/students', json={'name': 'Jane Doe'})
    assert response.status_code == 400
    error_data = response.get_json()
    assert error_data['error']['code'] == 'E001'
    assert error_data['error']['message'] == 'Email is required'

def test_retrieve_student_with_email(client):
    """Test retrieving a student record that includes the email."""
    # First create a student
    client.post('/students', json={'name': 'Alice Smith', 'email': 'alice.smith@example.com'})
    
    # Now try to retrieve that student by their ID
    response = client.get('/students/1')  # Assuming '1' is the ID of the student we just created
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Alice Smith'
    assert data['email'] == 'alice.smith@example.com'
```