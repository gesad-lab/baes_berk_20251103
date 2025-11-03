```python
import requests

BASE_URL = "http://localhost:8000/courses"  # Base URL for Course API

def test_create_course():
    """Test creating a new course with valid name and level."""
    response = requests.post(BASE_URL, json={"name": "Mathematics", "level": "100"})
    assert response.status_code == 201  # Ensure creation is successful
    data = response.json()  # Parse response data
    assert "id" in data  # Check that ID is returned
    assert data["name"] == "Mathematics"  # Verify course name
    assert data["level"] == "100"  # Verify course level

def test_retrieve_all_courses():
    """Test retrieving all course records."""
    response = requests.get(BASE_URL)  # Fetch all courses
    assert response.status_code == 200  # Ensure request was successful
    data = response.json()  # Parse the response data
    assert isinstance(data, list)  # Assert that the response is a list
    for course in data:
        assert "name" in course  # Verify each course has 'name'
        assert "level" in course  # Verify each course has 'level'

def test_update_course():
    """Test updating an existing course by ID."""
    # First, create a course to update
    create_response = requests.post(BASE_URL, json={"name": "Physics", "level": "200"})
    course_id = create_response.json()["id"]  # Get the ID of the newly created course

    # Now update the course
    update_response = requests.put(f"{BASE_URL}/{course_id}", json={"name": "Advanced Physics", "level": "300"})
    assert update_response.status_code == 200  # Ensure update was successful
    updated_data = update_response.json()  # Parse updated data
    assert updated_data["name"] == "Advanced Physics"  # Check updated name
    assert updated_data["level"] == "300"  # Check updated level

def test_create_course_without_required_fields():
    """Test creating a course without required fields."""
    response = requests.post(BASE_URL, json={"name": ""})  # Missing 'level'
    assert response.status_code == 422  # Should respond with unprocessable entity
    assert response.json()["detail"][0]["msg"] == "field required"  # Check error message for missing level

    response = requests.post(BASE_URL, json={"level": "100"})  # Missing 'name'
    assert response.status_code == 422  # Should respond with unprocessable entity
    assert response.json()["detail"][0]["msg"] == "field required"  # Check error message for missing name
```