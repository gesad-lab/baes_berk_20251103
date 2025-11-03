```python
# tests/test_student.py

import pytest

# Example test case for creating a student with valid email
def test_create_student(client):
    response = client.post("/students", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "John Doe", "email": "john@example.com"}

# Example test case for error handling on missing email
def test_create_student_missing_email(client):
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Email is required."
        }
    }

# Example test case for retrieving a student
def test_retrieve_student(client):
    client.post("/students", json={"name": "John Doe", "email": "john@example.com"})
    response = client.get("/students/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe", "email": "john@example.com"}
```