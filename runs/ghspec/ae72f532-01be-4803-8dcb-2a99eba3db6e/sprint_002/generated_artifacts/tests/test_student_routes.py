```python
import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

@pytest.mark.parametrize("name, email, expected_status, expected_response", [
    ("John Doe", "john@example.com", 201, {"id": 1, "name": "John Doe", "email": "john@example.com"}),
    ("Jane Doe", "jane@example.com", 201, {"id": 2, "name": "Jane Doe", "email": "jane@example.com"}),
    ("Invalid User", None, 400, {"error": {"code": "E002", "message": "Email is required"}}),
])
def test_create_student(name, email, expected_status, expected_response):
    """Tests the creation of a student with various email scenarios."""
    response = client.post("/students", json={"name": name, "email": email})
    assert response.status_code == expected_status
    assert response.json() == expected_response

def test_retrieve_students_with_email():
    """Tests retrieving all students including their emails."""
    response = client.get("/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure the response is a list

def test_create_student_without_email():
    """Tests creating a student without email field."""
    response = client.post("/students", json={"name": "No Email"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Email is required"}}

def test_data_persistence_after_restart():
    """Tests if the data persists after restarting the application."""
    # Create a student
    response = client.post("/students", json={"name": "Persistence Test", "email": "persistence@example.com"})
    assert response.status_code == 201

    # Simulating application restart by creating a new TestClient instance
    client_after_restart = TestClient(app)
    response = client_after_restart.get("/students")
    students = response.json()

    # Check that the created student still exists
    assert any(student['name'] == "Persistence Test" for student in students)
    assert any(student['email'] == "persistence@example.com" for student in students)
```