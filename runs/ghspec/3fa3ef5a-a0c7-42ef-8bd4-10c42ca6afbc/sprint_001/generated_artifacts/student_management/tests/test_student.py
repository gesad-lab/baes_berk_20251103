```python
import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_student_with_valid_name():
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201
    student = response.json()
    assert student['name'] == "John Doe"

def test_create_student_without_name():
    response = client.post("/students", json={})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "name"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }

def test_retrieve_student_by_id(client, created_student):
    response = client.get(f"/students/{created_student.id}")
    assert response.status_code == 200
    student = response.json()
    assert student['name'] == created_student.name

def test_retrieve_non_existent_student():
    response = client.get("/students/9999")  # Assume 9999 does not exist
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Student not found"
    }
```