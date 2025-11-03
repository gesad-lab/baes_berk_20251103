```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import json

app = FastAPI()

# In-memory placeholder for courses, assuming a database setup will replace this in the future.
courses = []

# Define the Course model
class Course(BaseModel):
    name: str
    level: str

@app.post("/courses", response_model=Course)
async def create_course(course: Course):
    """
    Create a new course with the provided name and level.
    
    Parameters:
    - course: Course data containing name and level.
    
    Returns:
    - A Course object representing the created course.
    
    Raises:
    - HTTPException: If the course data is invalid.
    """
    # Validate that both name and level are provided
    if not course.name or not course.level:
        raise HTTPException(status_code=400, detail="Both 'name' and 'level' fields are required.")

    # Simulating saving to a database
    courses.append(course)

    # Returning the created course as a JSON response
    return course

@app.get("/courses", response_model=List[Course])
async def list_courses():
    """
    Retrieve a list of all courses.

    Returns:
    - A list of Course objects containing names and levels.
    """
    return courses
```