```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming the FastAPI app is in src/main.py
from src.models import TeacherResponse  # Importing the TeacherResponse model

@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

def test_get_teacher_by_id(test_client):
    """Test retrieving a teacher's details by ID."""
    teacher_id = 1  # This ID should correspond to an existing teacher in the database
    response = test_client.get(f"/teachers/{teacher_id}")
    
    assert response.status_code == 200
    # Ensure the response structure matches the TeacherResponse model
    assert response.json() == {
        "id": teacher_id,
        "name": "John Doe",  # Replace with the expected name of the teacher
        "email": "john.doe@example.com"  # Replace with the expected email of the teacher
    }

def test_get_teacher_not_found(test_client):
    """Test retrieving a teacher that does not exist."""
    non_existent_teacher_id = 999  # Use an ID that does not exist
    response = test_client.get(f"/teachers/{non_existent_teacher_id}")

    assert response.status_code == 404
    assert response.json() == {
        "error": {
            "code": "E404",
            "message": "Teacher not found",
            "details": {}
        }
    }
```