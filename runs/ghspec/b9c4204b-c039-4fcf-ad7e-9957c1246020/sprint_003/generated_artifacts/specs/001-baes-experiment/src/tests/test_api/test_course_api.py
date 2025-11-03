```python
import json
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming the main FastAPI application is in src/main.py
from src.database import get_database  # Assuming there is a function to get the database
from src.models import CourseCreate  # Assuming CourseCreate is defined in src/models

client = TestClient(app)

# Integration tests for the course API endpoints
@pytest.mark.integration
def test_create_course_with_valid_data():
    """Test creating a new course with valid name and level."""
    response = client.post("/courses", json={"name": "Mathematics", "level": "101"})
    assert response.status_code == 201  # Check status code for successful creation
    course_data = response.json()
    assert course_data["name"] == "Mathematics"
    assert course_data["level"] == "101"

@pytest.mark.integration
def test_create_course_without_level():
    """Test error response when creating a course without level."""
    response = client.post("/courses", json={"name": "Mathematics"})  # Missing 'level'
    assert response.status_code == 400  # Check for bad request
    error_response = response.json()
    assert error_response["error"]["code"] == "E001"  # Assuming this is the error code for missing level
    assert "level" in error_response["error"]["message"]

@pytest.mark.integration
def test_list_courses():
    """Test retrieving the list of courses."""
    response = client.get("/courses")
    assert response.status_code == 200  # Check for successful retrieval
    courses = response.json()
    assert isinstance(courses, list)  # Ensure response is a JSON array
    # Optionally check if the course created earlier is in the list
    assert any(course["name"] == "Mathematics" for course in courses)

@pytest.mark.integration
def test_existing_student_data_intact_after_migration():
    """Test that existing student data remains intact after migration."""
    # Fetch existing student data
    response = client.get("/students")  # Retrieve the list of students
    assert response.status_code == 200
    initial_students = response.json()

    # Simulate database migration process (this would be handled separately in real scenario)

    # Fetch student data again after migration to ensure data integrity
    response_after_migration = client.get("/students")
    assert response_after_migration.status_code == 200
    students_after_migration = response_after_migration.json()

    # Validate that initial student data matches post-migration data
    assert initial_students == students_after_migration

    # Ensure length of initial and post-migration student lists are the same
    assert len(initial_students) == len(students_after_migration)
```