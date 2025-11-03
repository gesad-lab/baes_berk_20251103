```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr
from typing import List
from models import Course, db

app = FastAPI()

class CourseCreateRequest(BaseModel):
    name: constr(min_length=1)  # Validate non-empty string for name
    level: constr(min_length=1)  # Validate non-empty string for level

class CourseResponse(BaseModel):
    id: int
    name: str
    level: str

@app.post("/courses", response_model=CourseResponse, status_code=201)
async def create_course(course: CourseCreateRequest):
    """Create a new course."""
    new_course = Course(name=course.name, level=course.level)
    db.session.add(new_course)
    db.session.commit()
    return new_course

@app.get("/courses", response_model=List[CourseResponse], status_code=200)
async def get_courses():
    """Retrieve all courses."""
    courses = Course.query.all()
    return courses
```