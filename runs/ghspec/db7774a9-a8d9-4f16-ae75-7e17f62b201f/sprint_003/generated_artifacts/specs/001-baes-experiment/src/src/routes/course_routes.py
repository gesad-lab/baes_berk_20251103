from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel, Field
from typing import List, Optional

# Instantiate a new FastAPI router for course routes
router = APIRouter()

# Pydantic model for course creation and retrieval
class Course(BaseModel):
    id: Optional[int] = None  # Auto-incremented ID, not to be provided by user
    name: str = Field(..., min_length=1, description="The name of the course")
    level: str = Field(..., min_length=1, description="The level of the course")

# In-memory storage for course objects (this should typically be a database)
courses = []
next_id = 1  # To simulate auto-incrementing IDs

@router.post("/courses", response_model=Course, status_code=201)
async def create_course(course: Course):
    global next_id
    # Check if course name and level are provided
    if not course.name or not course.level:
        raise HTTPException(status_code=400, detail="Name and level are required.")
    
    # Create a new course with an auto-incremented ID
    course.id = next_id
    courses.append(course)
    next_id += 1
    return course

@router.get("/courses/{course_id}", response_model=Course)
async def retrieve_course(course_id: int):
    # Retrieve a course by ID
    for course in courses:
        if course.id == course_id:
            return course
    raise HTTPException(status_code=404, detail="Course not found.")

@router.get("/courses", response_model=List[Course])
async def list_courses():
    # List all courses
    return courses

# Note: Replace the in-memory storage with database interactions in production.