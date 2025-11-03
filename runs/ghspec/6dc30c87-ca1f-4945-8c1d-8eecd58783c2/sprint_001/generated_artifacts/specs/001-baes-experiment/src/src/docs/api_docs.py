```python
import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def test_students():
    # Setup code to create student records or other necessary data
    yield
    # Teardown code (if needed)

def test_get_student_by_id_success(test_students):
    """
    Test retrieving a student by ID successfully.
    Expect a 200 OK response with student data when the student exists.
    """
    # Assuming there's a student with ID 1 for testing
    response = client.get("/students/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Test Student"}

def test_get_student_by_id_not_found(test_students):
    """
    Test retrieving a student by ID that does not exist.
    Expect a 404 Not Found response.
    """
    # Assuming student ID 999 does not exist
    response = client.get("/students/999")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Student not found."}}

def test_get_student_by_id_invalid_id(test_students):
    """
    Test retrieving a student by an invalid ID.
    Expect a 400 Bad Request response.
    """
    response = client.get("/students/invalid_id")
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E400", "message": "Invalid student ID."}}
```