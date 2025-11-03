from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.student import Base, Student
import pytest

# Create a new FastAPI app for testing
app = FastAPI()

# Configure SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to override
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/students")
def create_student(student: Student, db=next(get_db())):
    db_student = Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get("/students/{student_id}")
def read_student(student_id: int, db=next(get_db())):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# Initialize the database for testing
@pytest.fixture(scope="module")
def test_db():
    # Create the tables
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the tables after tests
    Base.metadata.drop_all(bind=engine)

# Test client
client = TestClient(app)

def test_create_student(test_db):
    response = client.post("/students", json={"name": "John Doe", "age": 20})
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert "id" in response.json()

def test_read_student(test_db):
    # First create a student
    response = client.post("/students", json={"name": "Jane Doe", "age": 22})
    student_id = response.json()["id"]
    
    # Now retrieve the student by ID
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"

def test_read_non_existent_student(test_db):
    response = client.get("/students/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Student not found"}