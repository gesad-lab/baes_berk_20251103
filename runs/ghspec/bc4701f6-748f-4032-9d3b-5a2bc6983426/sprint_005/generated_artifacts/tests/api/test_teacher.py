```python
import pytest
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field
from src.api.teacher import app  # Assuming the FastAPI app for teachers is defined here

client = TestClient(app)

# Sample data for testing
@pytest.fixture(scope="module")
def teacher_data():
    return {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

@pytest.fixture(scope="module")
def invalid_teacher_data():
    return [
        {},  # Missing both name and email
        {"name": "Jane Doe"},  # Missing email
        {"email": "jane.doe@example.com"},  # Missing name
    ]

def test_create_teacher_success(teacher_data):
    response = client.post("/teachers", json=teacher_data)
    assert response.status_code == 201
    assert response.json() == {**teacher_data, "id": response.json().get("id")}

@pytest.mark.parametrize("invalid_data", invalid_teacher_data)
def test_create_teacher_validation_error(invalid_data):
    response = client.post("/teachers", json=invalid_data)
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Validation error: Missing required fields.",
            "details": {
                "missing_fields": [
                    "name" if "name" not in invalid_data else "",
                    "email" if "email" not in invalid_data else ""
                ]
            }
        }
    }
```
