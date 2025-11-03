from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import get_db, Base
from models import Course, Teacher

# Create a new FastAPI instance for testing
app = FastAPI()

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Use an in-memory database for testing
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency override for the test database session
@app.on_event("startup")
def startup():
    # Create the database tables and populate with initial data for tests
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    # Add sample Teacher and Course for testing
    teacher = Teacher(id=1, name="John Doe", email="john.doe@example.com")
    course = Course(id=1, title="Math 101", teacher_id=None)  # No teacher assigned initially
    db.add(teacher)
    db.add(course)
    db.commit()
    db.close()

@app.on_event("shutdown")
def shutdown():
    # Drop the database tables to reset state after tests run
    Base.metadata.drop_all(bind=engine)

# Setup the test client
client = TestClient(app)

# Test cases for course retrieval and teacher assignment
def test_assign_teacher_to_course_success():
    response = client.post("/courses/1/assign-teacher", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assigned successfully"}

def test_assign_teacher_to_course_already_assigned():
    # Assign a teacher to the course
    client.post("/courses/1/assign-teacher", json={"teacher_id": 1})
    response = client.post("/courses/1/assign-teacher", json={"teacher_id": 2})
    assert response.status_code == 409
    assert response.json() == {"error": {"code": "E002", "message": "Course already has a teacher assigned."}}

def test_assign_teacher_to_nonexistent_course():
    response = client.post("/courses/999/assign-teacher", json={"teacher_id": 1})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E001", "message": "Course not found."}}

def test_assign_nonexistent_teacher():
    response = client.post("/courses/1/assign-teacher", json={"teacher_id": 999})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E001", "message": "Teacher not found."}}

def test_get_course_success():
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "Math 101",
        "teacher": {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com",
        }
    }

def test_get_nonexistent_course():
    response = client.get("/courses/999")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E001", "message": "Course not found."}}