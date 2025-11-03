import pytest
from flask import json
from src.api.course_routes import create_course, get_course, update_course
from src.models.course_model import Course

@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client

def test_create_course_with_valid_data(client):
    """Test creating a course with valid name and level."""
    response = client.post('/courses', 
                           data=json.dumps({"name": "Mathematics", "level": "Beginner"}), 
                           content_type='application/json')
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == "Mathematics"
    assert data['level'] == "Beginner"

def test_get_course_by_id(client):
    """Test retrieving a course by its ID."""
    # First create a course to retrieve
    create_response = client.post('/courses', 
                                   data=json.dumps({"name": "Science", "level": "Intermediate"}), 
                                   content_type='application/json')
    course_id = create_response.get_json()['id']
    
    # Now retrieve the course
    response = client.get(f'/courses/{course_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == course_id
    assert data['name'] == "Science"
    assert data['level'] == "Intermediate"

def test_update_course(client):
    """Test updating an existing course."""
    # Create a course to update
    create_response = client.post('/courses', 
                                   data=json.dumps({"name": "History", "level": "Advanced"}), 
                                   content_type='application/json')
    course_id = create_response.get_json()['id']
    
    # Update the course
    response = client.put(f'/courses/{course_id}', 
                          data=json.dumps({"name": "History", "level": "Expert"}), 
                          content_type='application/json')
    assert response.status_code == 200
    updated_data = response.get_json()
    assert updated_data['name'] == "History"
    assert updated_data['level'] == "Expert"

def test_create_course_with_missing_fields(client):
    """Test error handling for missing course fields."""
    response = client.post('/courses', 
                           data=json.dumps({"name": ""}),  # Missing level
                           content_type='application/json')
    assert response.status_code == 400
    error_data = response.get_json()
    assert error_data['error']['code'] == "E001"
    assert error_data['error']['message'] == "Both name and level are required."

    response = client.post('/courses', 
                           data=json.dumps({"level": "Advanced"}),  # Missing name
                           content_type='application/json')
    assert response.status_code == 400
    error_data = response.get_json()
    assert error_data['error']['code'] == "E001"
    assert error_data['error']['message'] == "Both name and level are required."