```python
# src/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any
from fastapi.responses import JSONResponse

app = FastAPI()

# Assuming we've defined these models in src/models.py
from src.models import Course, Teacher

# Example of a Course update request
class CourseUpdate(BaseModel):
    teacher_id: int

# Example of a course response including teacher details
class CourseResponse(BaseModel):
    id: int
    title: str
    teacher: Optional[Dict[str, Any]]  # Will include teacher's info if associated

@app.patch("/courses/{course_id}", response_model=CourseResponse)
async def update_course(course_id: int, course_update: CourseUpdate):
    """Update an existing course by associating it with a specific teacher."""
    course = await Course.get(course_id)  # Fetch course by ID
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    # Update the course with the new teacher_id
    course.teacher_id = course_update.teacher_id
    await course.save()  # Persist changes

    # Fetch associated teacher details
    teacher = await Teacher.get(course.teacher_id) if course.teacher_id else None

    return CourseResponse(
        id=course.id,
        title=course.title,
        teacher={"name": teacher.name, "email": teacher.email} if teacher else None
    )

@app.get("/courses/{course_id}", response_model=CourseResponse)
async def get_course(course_id: int):
    """Retrieve course details, including associated teacher's name and email."""
    course = await Course.get(course_id)  # Fetch course by ID
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    # Fetch the associated teacher if exists
    teacher = await Teacher.get(course.teacher_id) if course.teacher_id else None

    return CourseResponse(
        id=course.id,
        title=course.title,
        teacher={"name": teacher.name, "email": teacher.email} if teacher else None
    )

# Additional endpoints and functionality can be consolidated here...
```