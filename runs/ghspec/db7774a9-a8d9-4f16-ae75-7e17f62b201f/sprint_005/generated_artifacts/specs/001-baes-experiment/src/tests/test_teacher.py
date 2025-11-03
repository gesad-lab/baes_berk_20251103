```python
# tests/test_teacher.py

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from src.main import app
from src.database.database import get_db
from src.models.teacher import Teacher
from src.schemas.teacher import TeacherCreate, TeacherResponse

client = TestClient(app)

@pytest.fixture(scope="module")
def db():
    # Dependency override for testing
    from src.database.database import SessionLocal
    yield SessionLocal()

def test_create_teacher_success(db: Session):
    # Successful teacher creation
    teacher_data = {"name": "John Doe", "email": "john.doe@example.com"}
    response = client.post("/teachers/", json=teacher_data)
    
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == teacher_data["name"]
    assert response.json()["email"] == teacher_data["email"]

def test_create_teacher_missing_name(db: Session):
    # Attempt to create a teacher without a name
    teacher_data = {"email": "missing.name@example.com"}
    response = client.post("/teachers/", json=teacher_data)
    
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name is required", "details": {}}}

def test_create_teacher_missing_email(db: Session):
    # Attempt to create a teacher without an email
    teacher_data = {"name": "Missing Email"}
    response = client.post("/teachers/", json=teacher_data)
    
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Email is required", "details": {}}}

def test_create_teacher_invalid_email(db: Session):
    # Attempt to create a teacher with an invalid email format
    teacher_data = {"name": "Invalid Email", "email": "invalid-email"}
    response = client.post("/teachers/", json=teacher_data)
    
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E003", "message": "Invalid email format", "details": {}}}

def test_get_teacher_by_id(db: Session):
    # Retrieve teacher by ID
    response = client.get("/teachers/1/")
    
    assert response.status_code == 200
    assert "name" in response.json()
    assert "email" in response.json()
    assert response.json()["id"] == 1

def test_list_all_teachers(db: Session):
    # List all teachers
    response = client.get("/teachers/")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)

```
