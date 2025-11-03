from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Base
from pydantic import BaseModel, EmailStr
import pytest

# Initialize the FastAPI application
app = FastAPI()

# SQLite database connection settings
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic model for creating a student
class StudentCreateModel(BaseModel):
    name: str
    email: EmailStr  # Automatically validates email

@app.post("/students", response_model=Student)
async def create_student(student: StudentCreateModel, db=next(get_db())):
    new_student = Student(**student.dict())
    db.add(new_student)
    try:
        db.commit()
        db.refresh(new_student)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Failed to create the student.")
    return new_student

# Integration tests to validate API contract for the email field
@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

def test_create_student_with_email(client):
    response = client.post("/students", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["email"] == "john@example.com"

def test_create_student_without_email(client):
    response = client.post("/students", json={"name": "Jane Doe"})
    assert response.status_code == 422  # Unprocessable Entity

def test_create_student_with_invalid_email(client):
    response = client.post("/students", json={"name": "Jane Doe", "email": "invalid-email"})
    assert response.status_code == 422  # Unprocessable Entity

def test_retrieve_student_by_id(client):
    # First create a student to retrieve
    create_response = client.post("/students", json={"name": "Alice Smith", "email": "alice@example.com"})
    student_id = create_response.json()["id"]

    # Now retrieve the created student
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == student_id
    assert data["name"] == "Alice Smith"
    assert data["email"] == "alice@example.com"