```python
import pytest
from fastapi.testclient import TestClient
from main import app  # assuming your FastAPI app is defined in main.py
from models import Student  # assuming your Student model is defined here

client = TestClient(app)

@pytest.fixture
def create_student():
    # This function can be used to create a student for testing
    response = client.post("/students/", json={"name": "John Doe", "age": 20})
    yield response.json()  # Yield to allow test to use it
    # If needed, include code to delete the test student after tests run


def test_create_student_valid(create_student):
    """Test successful creation of a student."""
    student = create_student
    assert student["name"] == "John Doe"
    assert student["age"] == 20
    assert student["id"] is not None  # assuming the API returns an id


def test_create_student_invalid_age():
    """Test creating a student with invalid age."""
    response = client.post("/students/", json={"name": "Jane Doe", "age": -5})
    assert response.status_code == 422  # Unprocessable Entity
    assert "age" in response.json()["detail"][0]["loc"]  # Check if the error details are correct


def test_create_student_missing_name():
    """Test creating a student without a name."""
    response = client.post("/students/", json={"age": 20})
    assert response.status_code == 422
    assert "name" in response.json()["detail"][0]["loc"]


def test_get_student(create_student):
    """Test retrieval of a student by ID."""
    student = create_student
    response = client.get(f"/students/{student['id']}")
    assert response.status_code == 200
    assert response.json()["id"] == student["id"]


def test_get_nonexistent_student():
    """Test retrieval of a nonexistent student."""
    response = client.get("/students/999")  # assuming 999 does not exist
    assert response.status_code == 404  # Not Found


def test_update_student(create_student):
    """Test updating existing student."""
    student = create_student
    update_response = client.put(f"/students/{student['id']}", json={"name": "John Smith", "age": 21})
    assert update_response.status_code == 200
    assert update_response.json()["name"] == "John Smith"


def test_delete_student(create_student):
    """Test deletion of a student."""
    student = create_student
    delete_response = client.delete(f"/students/{student['id']}")
    assert delete_response.status_code == 204  # No Content
    # Verify that the student was indeed deleted
    get_response = client.get(f"/students/{student['id']}")
    assert get_response.status_code == 404
```