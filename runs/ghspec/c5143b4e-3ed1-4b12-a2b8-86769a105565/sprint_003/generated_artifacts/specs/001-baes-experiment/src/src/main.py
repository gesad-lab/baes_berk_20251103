from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, ValidationError
from typing import List
from sqlalchemy.orm import Session
from . import models, crud, database

app = FastAPI()

# Pydantic schema for Course creation
class CourseCreate(BaseModel):
    name: str = Field(..., title="Course Name", max_length=100)
    level: str = Field(..., title="Course Level", max_length=50)

@app.post("/courses/", response_model=models.Course)
async def create_course(course: CourseCreate):
    """
    Create a new course with the provided details.

    Parameters:
    - course: CourseCreate schema containing course name and level.

    Returns:
    - The created Course entity.
    
    Raises:
    - HTTPException: If unable to create a course with a detailed error message.
    """
    try:
        db: Session = database.get_db()
        return crud.create_course(db=db, course=course)
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors())
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while creating the course.")
        
@app.get("/courses/", response_model=List[models.Course])
async def get_courses():
    """
    Retrieve a list of all courses.

    Returns:
    - A list of Course entities containing name and level.
    """
    db: Session = database.get_db()
    return crud.get_courses(db=db)