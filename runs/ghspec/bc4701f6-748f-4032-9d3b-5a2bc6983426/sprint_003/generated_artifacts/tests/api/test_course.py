```python
import pytest
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel

app = FastAPI()

# Assuming Course model is defined in a separate file
from src.models.course import Course

# Simulating in-memory data store for courses
courses = {}

class CourseCreate(BaseModel):
    name: str
    level: str

@app.post("/courses", status_code=201)
def create_course(course: CourseCreate):
    if not course.name:
        raise HTTPException(status_code=400, detail="E001: Course name is required")
    if not course.level:
        raise HTTPException(status_code=400, detail="E002: Course level is required")
    
    course_id = len(courses) + 1
    courses[course_id] = course
    return {"id": course_id, "name": course.name, "level": course.level}

@app.get("/courses/{course_id}")
def get_course(course_id: int):
    if course_id not in courses:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"id": course_id, **courses[course_id].dict()}

# Test for course creation
def test_create_course_success():
    client = TestClient(app)
    response = client.post("/courses", json={"name": "Math 101", "level": "Beginner"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "Math 101", "level": "Beginner"}

def test_create_course_missing_name():
    client = TestClient(app)
    response = client.post("/courses", json={"level": "Beginner"})
    assert response.status_code == 400
    assert response.json() == {"detail": "E001: Course name is required"}

def test_create_course_missing_level():
    client = TestClient(app)
    response = client.post("/courses", json={"name": "Math 101"})
    assert response.status_code == 400
    assert response.json() == {"detail": "E002: Course level is required"}

def test_get_existing_course():
    client = TestClient(app)
    client.post("/courses", json={"name": "Science 101", "level": "Intermediate"})
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Science 101", "level": "Intermediate"}

def test_get_non_existing_course():
    client = TestClient(app)
    response = client.get("/courses/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Course not found"}
```