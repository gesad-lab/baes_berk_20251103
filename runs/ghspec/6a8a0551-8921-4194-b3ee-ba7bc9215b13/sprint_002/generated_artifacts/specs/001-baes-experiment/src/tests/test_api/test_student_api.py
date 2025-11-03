```python
import json
import pytest
from api import create_app, db
from api.models import Student

@pytest.fixture(scope='module')
def test_client():
    """Setup a test client for the Flask application."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()  # Create the in-memory database
        yield app.test_client()  # Create the test client
        db.drop_all()  # Drop the in-memory database after testing

def test_retrieve_specific_student_success(test_client):
    """Test retrieving a specific student successfully."""
    # Given: a student is created
    student_data = {"name": "John Doe", "email": "john.doe@example.com"}
    response = test_client.post('/students/', data=json.dumps(student_data), 
                                 content_type='application/json')
    created_student = response.get_json()
    
    # When: retrieving the student by ID
    response = test_client.get(f'/students/{created_student["id"]}')
    
    # Then: the response should match the created student's data
    assert response.status_code == 200
    assert response.json == created_student

def test_retrieve_specific_student_not_found(test_client):
    """Test retrieving a student that does not exist."""
    # When: attempting to retrieve a non-existent student
    response = test_client.get('/students/9999')  # An ID that does not exist
    
    # Then: a 404 error should be returned with appropriate error message
    assert response.status_code == 404
    assert response.json == {
        "error": {
            "code": "E404",
            "message": "Student not found"
        }
    }
```