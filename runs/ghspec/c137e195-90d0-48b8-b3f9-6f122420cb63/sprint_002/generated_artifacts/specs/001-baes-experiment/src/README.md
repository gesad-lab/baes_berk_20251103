```python
# Filename: tests/test_students.py

from fastapi import FastAPI, HttpException
from fastapi.testclient import TestClient
from database.db import init_db
from api.students import router as student_router

app = FastAPI()

@app.on_event("startup")
def startup():
    """Initialize the database on application startup."""
    init_db()

app.include_router(student_router)

client = TestClient(app)

def test_create_student_with_valid_email():
    """Test creating a student with valid name and email."""
    response = client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}

def test_create_student_with_missing_email():
    """Test creating a student with a missing email."""
    response = client.post("/students", json={"name": "Jane Doe"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Email is required"}

def test_create_student_with_invalid_email():
    """Test creating a student with an invalid email format."""
    response = client.post("/students", json={"name": "Jane Doe", "email": "invalid_email_format"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid email format"}

def test_retrieve_students_success():
    """Test retrieving all students returns JSON with correct format."""
    client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    client.post("/students", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    
    response = client.get("/students")
    assert response.status_code == 200
    student_list = response.json()
    assert isinstance(student_list, list)
    assert len(student_list) == 2
    assert all("name" in student and "email" in student for student in student_list)

def test_retrieve_students_no_students():
    """Test retrieving students when no entries exist."""
    response = client.get("/students")
    assert response.status_code == 200
    assert response.json() == []

```