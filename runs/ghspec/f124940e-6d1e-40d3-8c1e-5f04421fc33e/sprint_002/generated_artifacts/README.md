```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming the FastAPI app is instantiated in src/main.py
from src.models import Student  # Assuming the Student model is located in src/models.py

client = TestClient(app)

@pytest.fixture(scope="module")
def create_student():
    # Setup: Create a student in the database
    response = client.post("/students/", json={"name": "Test Student", "email": "test@student.com"})
    yield response.json()
    # Teardown: Remove the created student (if applicable, depending on the testing strategy)

def test_create_student_with_email():
    response = client.post("/students/", json={"name": "Test Student", "email": "test@student.com"})
    assert response.status_code == 201
    assert response.json()["email"] == "test@student.com"

def test_create_student_with_invalid_email():
    response = client.post("/students/", json={"name": "Test Student", "email": "invalidemail"})
    assert response.status_code == 400
    assert "Invalid email format" in response.json()["detail"]

def test_retrieve_students_with_email(create_student):
    response = client.get("/students/")
    assert response.status_code == 200
    students = response.json()
    assert len(students) > 0
    assert "email" in students[0]  # Verify that the email field is included

def test_update_student_email(create_student):
    student_id = create_student["id"]
    new_email = "updated@student.com"
    response = client.put(f"/students/{student_id}", json={"name": "Test Student", "email": new_email})
    assert response.status_code == 200
    assert response.json()["email"] == new_email
```