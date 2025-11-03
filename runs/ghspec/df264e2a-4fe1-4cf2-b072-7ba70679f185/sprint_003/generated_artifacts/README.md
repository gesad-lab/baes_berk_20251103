```python
# tests/test_course.py

import pytest

@pytest.fixture
def client():
    # Assuming there's a fixture to set up the test client properly
    from app import create_app
    app = create_app()
    with app.test_client() as client:
        yield client

def test_get_course_success(client):
    """Test retrieving an existing course by ID."""
    # First, create a course to retrieve
    course_data = {"name": "Mathematics", "level": "Intermediate"}
    create_response = client.post("/courses", json=course_data)
    assert create_response.status_code == 201
    course_id = create_response.json["id"]
    
    # Now retrieve the course by ID
    response = client.get(f"/courses/{course_id}")
    
    # Check response status and data
    assert response.status_code == 200
    assert response.json == {"id": course_id, "name": "Mathematics", "level": "Intermediate"}

def test_get_course_not_found(client):
    """Test retrieving a course that does not exist."""
    invalid_course_id = 9999  # Example ID that likely does not exist
    response = client.get(f"/courses/{invalid_course_id}")
    
    # Check for not found status
    assert response.status_code == 404
    assert response.json == {"error": {"code": "E404", "message": "Course not found."}}

def test_get_course_invalid_id(client):
    """Test retrieving a course with an invalid ID."""
    response = client.get("/courses/invalid_id")
    
    # Check for bad request status due to invalid ID format
    assert response.status_code == 400
    assert response.json == {"error": {"code": "E400", "message": "Invalid course ID."}}
```