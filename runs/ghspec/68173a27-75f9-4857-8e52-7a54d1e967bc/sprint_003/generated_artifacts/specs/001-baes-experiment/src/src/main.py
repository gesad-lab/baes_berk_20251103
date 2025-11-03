```python
# src/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
from src.models.course import Course  # Ensure this import matches your models
from src.repositories.course_repository import create_course, get_courses  # Ensure these repository methods exist

app = FastAPI()

# Pydantic model for Course creation
class CourseCreateRequest(BaseModel):
    name: str = Field(..., description="The name of the course")
    level: str = Field(..., description="The level of the course")

@app.post("/api/v1/courses", response_model=Course)
async def create_new_course(course: CourseCreateRequest):
    # Validate course input
    if not course.name or not course.level:
        raise HTTPException(
            status_code=400,
            detail={"error": {"code": "E001", "message": "Both name and level fields are required."}}
        )
    
    # Create course in the database using the repository method
    new_course = await create_course(course.name, course.level)
    return new_course

@app.get("/api/v1/courses", response_model=List[Course])
async def retrieve_all_courses():
    # Retrieve all courses using the repository method
    return await get_courses()
```