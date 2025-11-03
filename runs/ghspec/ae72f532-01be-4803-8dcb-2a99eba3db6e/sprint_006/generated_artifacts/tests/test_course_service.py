```python
import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# Function to create a teacher for testing purposes
def create_teacher(name: str, email: str):
    response = client.post("/teachers/", json={"name": name, "email": email})
    return response.json()

# Function to create a course for testing purposes
def create_course(title: str, description: str, teacher_id: int):
    response = client.post("/courses/", json={"title": title, "description": description, "teacher_id": teacher_id})
    return response.json()

# Function to downgrade the database schema - specifically to drop `teacher_id`
def downgrade():
    # Simulating dropping the column teacher_id from the Course table
    # This is a placeholder function to indicate future implementation
    pass

# Test to create a new teacher
def test_create_teacher():
    # Valid teacher data
    response = create_teacher("John Doe", "john.doe@example.com")
    assert response["name"] == "John Doe"
    assert response["email"] == "john.doe@example.com"

# Test to assign a teacher to a course
def test_assign_teacher_to_course():
    teacher = create_teacher("Jane Smith", "jane.smith@example.com")
    course = create_course("Math 101", "Introduction to Mathematics", teacher["id"])
    
    assert course["teacher_id"] == teacher["id"]

# Test retrieval of course details
def test_retrieve_course_details():
    teacher = create_teacher("Emily Johnson", "emily.johnson@example.com")
    course = create_course("Science 101", "Introduction to Science", teacher["id"])
    
    response = client.get(f"/courses/{course['id']}")
    assert response.status_code == 200
    assert response.json()["teacher_id"] == teacher["id"]

# Test assignment with non-existent teacher
def test_assign_non_existent_teacher_to_course():
    response = client.post("/courses/", json={"title": "History 101", "description": "Introduction to History", "teacher_id": 99999})
    assert response.status_code == 404  # Assuming the system returns 404 for non-existent teacher
    assert response.json()["error"]["message"] == "Teacher does not exist"
```