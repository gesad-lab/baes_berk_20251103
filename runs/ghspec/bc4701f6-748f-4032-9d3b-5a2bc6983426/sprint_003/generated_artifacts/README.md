```python
import pytest
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel

app = FastAPI()

# Assuming the Course model is already defined in src/models/course.py
from src.models.course import Course  # Import the Course model

# In-memory course data store for testing
courses = {}


# Create course function (simulated endpoint)
@app.post("/courses", status_code=201)
def create_course(course: Course):
    if not course.name or not course.level:
        raise HTTPException(status_code=400, detail="Name and level are required.")
    course_id = len(courses) + 1
    courses[course_id] = course
    return {"id": course_id, "course": course}


# Retrieve course function (simulated endpoint)
@app.get("/courses/{course_id}")
def get_course(course_id: int):
    if course_id not in courses:
        raise HTTPException(status_code=404, detail="Course not found.")
    return {"course": courses[course_id]}


# Test class for course functionality
class TestCourseAPI:
    client: TestClient

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.client = TestClient(app)
        courses.clear()  # Clear existing course data before each test

    def test_create_course_with_valid_data(self):
        response = self.client.post("/courses", json={"name": "Math 101", "level": "Beginner"})
        assert response.status_code == 201
        assert "id" in response.json()
        assert response.json()["course"]["name"] == "Math 101"
        assert response.json()["course"]["level"] == "Beginner"

    def test_create_course_with_missing_name(self):
        response = self.client.post("/courses", json={"level": "Beginner"})
        assert response.status_code == 400
        assert response.json() == {"detail": "Name and level are required."}

    def test_create_course_with_missing_level(self):
        response = self.client.post("/courses", json={"name": "Math 101"})
        assert response.status_code == 400
        assert response.json() == {"detail": "Name and level are required."}

    def test_get_course_with_valid_id(self):
        self.client.post("/courses", json={"name": "Math 101", "level": "Beginner"})
        response = self.client.get("/courses/1")
        assert response.status_code == 200
        assert response.json()["course"]["name"] == "Math 101"

    def test_get_course_with_invalid_id(self):
        response = self.client.get("/courses/999")
        assert response.status_code == 404
        assert response.json() == {"detail": "Course not found."}
```