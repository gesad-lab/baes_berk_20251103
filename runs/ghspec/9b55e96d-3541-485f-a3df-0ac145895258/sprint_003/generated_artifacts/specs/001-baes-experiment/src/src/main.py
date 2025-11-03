```python
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from typing import List

router = APIRouter()

# Defining the Course model for input validation
class CourseCreate(BaseModel):
    name: str = Field(..., title="Name of the Course", min_length=1)
    level: str = Field(..., title="Level of the Course", min_length=1)

# Course endpoint to create a new course
@router.post("/courses", response_description="Create a new course", status_code=status.HTTP_200_OK)
async def create_course(course: CourseCreate):
    # Here you would save the course to the database
    return {"message": "Course created successfully"}

# Course retrieval endpoint example
@router.get("/courses/{course_id}", response_description="Get a course by ID")
async def get_course(course_id: int):
    # Here you would retrieve the course from the database
    return {"id": course_id, "name": "Sample Course", "level": "Beginner"}

# Course update endpoint
@router.put("/courses/{course_id}", response_description="Update an existing course")
async def update_course(course_id: int, course: CourseCreate):
    # Here you would update the course in the database
    return {"message": "Course updated successfully"}
```