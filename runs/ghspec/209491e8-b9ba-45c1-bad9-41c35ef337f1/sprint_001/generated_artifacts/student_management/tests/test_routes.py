```python
import os
import pytest
from fastapi.testclient import TestClient
from src.main import app

# Ensure all necessary environment variables are set before running tests
def validate_environment_variables():
    required_vars = ["DATABASE_URL", "SECRET_KEY"]
    missing_vars = [var for var in required_vars if var not in os.environ]
    if missing_vars:
        raise Exception(f"Missing environment variables: {', '.join(missing_vars)}")

# Validation of environment variables
validate_environment_variables()

client = TestClient(app)

def test_create_student():
    # Test the creation of a student
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201  # Check if creation was successful
    assert response.json() == {"id": 1, "name": "John Doe"}  # Check response content

def test_create_student_without_name():
    # Test creating a student without a name
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
    }  # Check error response format

def test_retrieve_students():
    # Test retrieving the list of students
    response = client.get("/students")
    assert response.status_code == 200  # Check if retrieval was successful
    assert isinstance(response.json(), list)  # Response should be a list
    assert {"id": 1, "name": "John Doe"} in response.json()  # Ensure the created student is in the list

def test_create_student_with_invalid_name():
    # Test creating a student with an invalid name (if there are additional validation rules)
    response = client.post("/students", json={"name": ""})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "name"],
                "msg": "Name must not be empty",
                "type": "value_error"
            }
        ]
    }  # Check error response format
```