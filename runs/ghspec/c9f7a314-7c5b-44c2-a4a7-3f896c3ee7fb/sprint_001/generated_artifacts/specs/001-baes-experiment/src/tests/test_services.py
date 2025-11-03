```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models import Student

client = TestClient(app)

# Sample valid student data for tests
valid_student_data = {"name": "John Doe"}

@pytest.fixture(scope="module")
def create_student():
    response = client.post("/students", json=valid_student_data)
    assert response.status_code == 201  # Ensure student creation is successful
    return response.json()

def test_create_student_valid_data():
    response = client.post("/students", json=valid_student_data)
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == valid_student_data["name"]

def test_create_student_invalid_data():
    # Test with an empty name
    response = client.post("/students", json={"name": ""})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid name provided", "details": {}}}

def test_retrieve_student(create_student):
    student_id = create_student["id"]
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json() == create_student

def test_retrieve_non_existing_student():
    response = client.get("/students/9999")  # Assuming 9999 doesn't exist
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E002", "message": "Student not found", "details": {}}}

def test_update_student(create_student):
    student_id = create_student["id"]
    updated_data = {"name": "Jane Doe"}
    response = client.put(f"/students/{student_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == updated_data["name"]

def test_update_non_existing_student():
    response = client.put("/students/9999", json={"name": "Non Existent"})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E002", "message": "Student not found", "details": {}}}

def test_delete_student(create_student):
    student_id = create_student["id"]
    response = client.delete(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Student deleted successfully"}

def test_delete_non_existing_student():
    response = client.delete("/students/9999")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E002", "message": "Student not found", "details": {}}}
```