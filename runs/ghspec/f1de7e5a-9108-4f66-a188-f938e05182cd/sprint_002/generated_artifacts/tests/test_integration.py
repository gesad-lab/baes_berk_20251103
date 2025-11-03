```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your main app is in a file called main.py

client = TestClient(app)

# Test case for creating a new student
def test_create_student():
    response = client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json() == {"name": "John Doe", "email": "john.doe@example.com"}

# Test case for creating a student with invalid email
def test_create_student_invalid_email():
    response = client.post("/students", json={"name": "Jane Doe", "email": "invalid-email"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid email format"}}

# Test case for creating a student with empty name
def test_create_student_empty_name():
    response = client.post("/students", json={"name": "", "email": "jane.doe@example.com"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Name cannot be empty"}}

# Test case for retrieving all students
def test_get_all_students():
    client.post("/students", json={"name": "Alice", "email": "alice@example.com"})
    response = client.get("/students")
    assert response.status_code == 200
    students = response.json()
    assert isinstance(students, list)
    assert all("email" in student for student in students)
```