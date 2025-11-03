```python
import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_teacher():
    response = client.post("/api/v1/teachers", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    assert response.status_code == 201
    assert "id" in response.json()

def test_create_teacher_with_duplicate_email():
    # Create the first teacher with a unique email
    client.post("/api/v1/teachers", json={"name": "John", "email": "john.doe@example.com"})
    
    # Attempt to create a second teacher with the same email
    response = client.post("/api/v1/teachers", json={"name": "Johnny", "email": "john.doe@example.com"})
    
    # Confirm that the response indicates a bad request due to duplicate email
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Email already exists.", "details": {}}}

def test_create_teacher_without_name():
    # Attempt to create a teacher without a name
    response = client.post("/api/v1/teachers", json={"email": "missing.name@example.com"})
    
    # Ensure that a 400 response is returned for missing fields
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Name is required.", "details": {}}}

def test_create_teacher_without_email():
    # Attempt to create a teacher without an email
    response = client.post("/api/v1/teachers", json={"name": "No Email"})
    
    # Ensure that a 400 response is returned for missing fields
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E003", "message": "Email is required.", "details": {}}}

def test_create_teacher_with_invalid_email_format():
    # Attempt to create a teacher with an invalid email format
    response = client.post("/api/v1/teachers", json={"name": "Invalid Email", "email": "invalid_email"})
    
    # Ensure that a 400 response is returned for invalid email format
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E004", "message": "Invalid email format.", "details": {}}}
```