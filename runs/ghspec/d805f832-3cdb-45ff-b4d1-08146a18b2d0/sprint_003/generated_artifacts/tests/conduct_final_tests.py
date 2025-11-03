```python
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Course, Base  # Import Course model from models
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

# Test data for creating a course
valid_course_data = {"name": "Math 101", "level": "Beginner"}
invalid_course_data_missing_name = {"level": "Beginner"}
invalid_course_data_missing_level = {"name": "Math 101"}

@pytest.fixture(scope="module")
def test_client():
    return TestClient(app)

@app.post("/courses", response_model=Course)
async def create_course(course: Course):
    db: Session = next(get_db())
    new_course = Course(name=course.name, level=course.level)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

@app.get("/courses/{course_id}", response_model=Course)
async def read_course(course_id: int):
    db: Session = next(get_db())
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

# Test cases for conducting final tests
def test_create_course(test_client):
    response = test_client.post("/courses", json=valid_course_data)
    assert response.status_code == 200
    assert response.json()["name"] == valid_course_data["name"]
    assert response.json()["level"] == valid_course_data["level"]

def test_create_course_missing_name(test_client):
    response = test_client.post("/courses", json=invalid_course_data_missing_name)
    assert response.status_code == 422  # Unprocessable Entity

def test_create_course_missing_level(test_client):
    response = test_client.post("/courses", json=invalid_course_data_missing_level)
    assert response.status_code == 422  # Unprocessable Entity

def test_read_course(test_client):
    # First create a course then retrieve it
    create_response = test_client.post("/courses", json=valid_course_data)
    course_id = create_response.json()["id"]
    
    response = test_client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    assert response.json()["id"] == course_id
    assert response.json()["name"] == valid_course_data["name"]

def test_read_nonexistent_course(test_client):
    response = test_client.get("/courses/999")  # Assuming this ID does not exist
    assert response.status_code == 404  # Not Found

# Testing database migration is typically done separately
# Here we assume the migration has been executed before test execution

```