```python
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base, Student
from src.services.student_service import StudentService

# Setup the FastAPI application for testing
app = FastAPI()

# In-memory SQLite for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

# Dependency to override
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Include the Student service in your app
student_service = StudentService(get_db)

@app.post("/students/")
def create_student(name: str):
    return student_service.create_student(name)

@app.get("/students/{student_id}")
def read_student(student_id: int):
    return student_service.get_student(student_id)

@app.put("/students/{student_id}")
def update_student(student_id: int, name: str):
    return student_service.update_student(student_id, name)

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    return student_service.delete_student(student_id)

# Initialize the test client
client = TestClient(app)

# Test cases
def test_create_student():
    response = client.post("/students/", json={"name": "John Doe"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe"}

def test_read_student():
    response = client.post("/students/", json={"name": "Jane Doe"})
    student_id = response.json()["id"]
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json() == {"id": student_id, "name": "Jane Doe"}

def test_update_student():
    response = client.post("/students/", json={"name": "Alice"})
    student_id = response.json()["id"]
    response = client.put(f"/students/{student_id}", json={"name": "Alice Smith"})
    assert response.status_code == 200
    assert response.json() == {"id": student_id, "name": "Alice Smith"}

def test_delete_student():
    response = client.post("/students/", json={"name": "Bob"})
    student_id = response.json()["id"]
    response = client.delete(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json() == {"detail": "Student deleted successfully"}

    # Check that the student was actually deleted
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 404  # Not found

def test_create_student_invalid_name():
    response = client.post("/students/", json={"name": ""})  # Empty name
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "name"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }
```