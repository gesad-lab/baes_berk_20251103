```python
import json
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming the main FastAPI application is in src/main.py
from src.database import get_database  # Assuming there is a function to get the database

client = TestClient(app)

# Integration tests for the student API endpoints
@pytest.mark.integration
def test_create_student_with_email():
    """Test creating a new student with valid name and email"""
    response = client.post("/students", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201  # Check that the response status is 201 Created
    assert response.json() == {"name": "John Doe", "email": "john@example.com"}

@pytest.mark.integration
@pytest.mark.parametrize("student_data,expected_status,expected_response", [
    ({"name": "Jane Doe"}, 400, {"detail": "Field 'email' is required"}),  # Missing email
    ({"email": "jane@example.com"}, 400, {"detail": "Field 'name' is required"}),  # Missing name
    ({"name": "", "email": "jane@example.com"}, 400, {"detail": "Field 'name' must not be empty"}),  # Invalid name
])
def test_create_student_validation(student_data, expected_status, expected_response):
    """Test validation on creation of a new student"""
    response = client.post("/students", json=student_data)
    assert response.status_code == expected_status  # Check that the correct status code is returned
    assert response.json() == expected_response  # Check that the correct error message is returned
```