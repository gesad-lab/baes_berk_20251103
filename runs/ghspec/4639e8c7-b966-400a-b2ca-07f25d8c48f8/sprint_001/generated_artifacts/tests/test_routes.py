import pytest
from flask import json
from src.app import create_app  # Assuming you have a Flask application factory

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_student_with_empty_name(client):
    """Test that creating a student with an empty name returns an error."""
    response = client.post('/students', json={'name': ''})  # Assuming the endpoint exists
    assert response.status_code == 400  # Expecting a bad request error
    data = json.loads(response.data)
    assert 'error' in data  # Expecting an error field in the response
    assert data['error']['code'] == 'E001'  # Check for specific error code
    assert data['error']['message'] == 'Name field is required'  # Expected error message

# Additional test cases can be added here for valid student creation and retrieval of all students.