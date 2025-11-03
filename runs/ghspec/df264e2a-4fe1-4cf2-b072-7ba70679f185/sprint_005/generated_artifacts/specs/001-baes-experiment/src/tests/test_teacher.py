```python
import pytest

# Assuming we have a client fixture that initializes the FastAPI test client

def test_create_teacher(client):
    response = client.post("/teachers", json={"name": "Jane Doe", "email": "jane@example.com"})
    assert response.status_code == 201
    assert response.json() == {"message": "Teacher added successfully."}

def test_create_teacher_without_name(client):
    response = client.post("/teachers", json={"email": "jane@example.com"})
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Name and email are required."
        }
    }

def test_create_teacher_without_email(client):
    response = client.post("/teachers", json={"name": "Jane Doe"})
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Name and email are required."
        }
    }

def test_get_teacher_by_id(client):
    # First we need to create a teacher to test fetching
    response = client.post("/teachers", json={"name": "Jane Doe", "email": "jane@example.com"})
    assert response.status_code == 201

    teacher_id = response.json().get("teacher_id") # Replace with actual key returned

    # Now fetch the teacher by ID
    response = client.get(f"/teachers/{teacher_id}")
    assert response.status_code == 200
    assert response.json() == {
        "name": "Jane Doe",
        "email": "jane@example.com"
    }

def test_get_teacher_not_found(client):
    response = client.get("/teachers/999")
    assert response.status_code == 404
    assert response.json() == {
        "error": {
            "code": "E002",
            "message": "Teacher not found."
        }
    }
```