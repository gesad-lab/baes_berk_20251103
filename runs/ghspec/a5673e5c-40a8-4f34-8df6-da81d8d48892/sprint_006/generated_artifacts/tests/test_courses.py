```python
import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # Setup logic for creating a unique teacher and course used for testing
    response = client.post("/teachers", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    assert response.status_code == 201
    teacher_id = response.json()['id']
    
    response = client.post("/courses", json={"name": "Mathematics 101"})
    assert response.status_code == 201
    yield {"teacher_id": teacher_id}  # Provide the teacher_id for use in tests

def test_assign_teacher_to_course(setup_database):
    """Test to assign a teacher to a given course."""
    teacher_id = setup_database["teacher_id"]
    response = client.post("/courses/1/teachers", json={"teacher_id": teacher_id})
    assert response.status_code == 200  # Check if the assignment was successful
    data = response.json()
    assert data['teacher_id'] == teacher_id  # Ensure the course has the right teacher

def test_retrieve_course_details():
    """Test retrieving course details including teacher information."""
    response = client.get("/courses/1")
    assert response.status_code == 200  # Check for a successful response
    data = response.json()
    
    assert 'teacher_name' in data  # Ensure teacher information is included
    assert data['teacher_name'] == "Jane Doe"  # Check if retrieved teacher name matches expectation

def test_foreign_key_relationship(setup_database):
    """Test the foreign key constraint on Course to Teacher."""
    teacher_id = setup_database["teacher_id"]
    
    # Attempting to assign a non-existent teacher (for testing FK)
    response = client.post("/courses/1/teachers", json={"teacher_id": 999})  # Assuming 999 doesn't exist
    assert response.status_code == 400  # Expecting a Bad Request due to FK violation
    assert response.json() == {"error": {"code": "E001", "message": "Invalid teacher ID", "details": {}}}  # Ensure the response matches expected error format
```