```python
# src/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from src.models.course import Course  # Import the Course model
from src.models.student import Student  # Existing Student model import
from src.services.course_service import CourseService  # New Course service
from src.services.student_service import StudentService  # Existing Student service

app = FastAPI()

# Course schema for request validation
class CourseCreate(BaseModel):
    name: str
    level: str

class CourseResponse(BaseModel):
    id: int
    name: str
    level: str

# In-memory course storage for simplicity (replace with database in real scenario)
courses = []
course_id_counter = 1

@app.post("/courses", response_model=CourseResponse, status_code=201)
def create_course(course: CourseCreate):
    """Creates a new course with a name and level."""
    global course_id_counter
    if not course.name or not course.level:
        raise HTTPException(status_code=422, detail="Both name and level must be provided.")
    
    new_course = Course(id=course_id_counter, name=course.name, level=course.level)
    courses.append(new_course)
    course_id_counter += 1
    return new_course

@app.get("/courses/{course_id}", response_model=CourseResponse)
def get_course(course_id: int):
    """Retrieves a course by ID."""
    course = next((course for course in courses if course.id == course_id), None)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found.")
    return course

@app.get("/courses", response_model=List[CourseResponse])
def list_courses():
    """Lists all available courses."""
    return courses
```