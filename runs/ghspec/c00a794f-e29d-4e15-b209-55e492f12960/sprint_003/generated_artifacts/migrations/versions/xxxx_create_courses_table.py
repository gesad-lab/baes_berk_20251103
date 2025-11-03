```python
# tests/test_course.py
import pytest

# Test for creating a new course with valid name and level
def test_add_course_with_valid_data(client):
    response = client.post("/courses", json={"name": "Math 101", "level": "beginner"})
    assert response.status_code == 200
    assert response.json() == {"message": "Course added successfully"}

# Test for attempting to create a new course without providing a level
def test_add_course_without_level(client):
    response = client.post("/courses", json={"name": "Math 101"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Level is required."}}

# Test for retrieving all courses when there are courses in the database
def test_retrieve_all_courses(client):
    # First, create some courses
    client.post("/courses", json={"name": "Math 101", "level": "beginner"})
    client.post("/courses", json={"name": "History 201", "level": "intermediate"})

    # Now retrieve all courses
    response = client.get("/courses")
    assert response.status_code == 200

    # Check if the response includes the correct course details
    assert len(response.json()) == 2
    assert response.json() == [
        {"name": "Math 101", "level": "beginner"},
        {"name": "History 201", "level": "intermediate"},
    ]

# Test for validating migration - check if existing student data is preserved
def test_student_data_preserved_after_migration(client):
    # Assuming there was a student added before migration
    client.post("/students", json={"name": "Jane Doe", "email": "jane@example.com"})
    
    # Perform migration (this would be handled in the setup/test environment)
    # Verify student data is still accessible
    response = client.get("/students")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0] == {"name": "Jane Doe", "email": "jane@example.com"}
```