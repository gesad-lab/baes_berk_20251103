from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, constr
from models import Course  # Assuming Course model is already defined in models.py
from database import get_db  # Assuming there's a function to get the database session

router = APIRouter()

class CourseCreateModel(BaseModel):
    name: constr(min_length=1)  # Ensures name is a non-empty string
    level: constr(min_length=1)  # Ensures level is a non-empty string

@router.post("/courses", response_model=Course)
async def create_course(course: CourseCreateModel, db: Session = next(get_db())):
    # Validate that both `name` and `level` are provided by Pydantic
    if not course.name:
        raise HTTPException(status_code=400, detail="E001: Course name is required")
    if not course.level:
        raise HTTPException(status_code=400, detail="E002: Course level is required")
    
    # Create the Course instance and save it to the database
    new_course = Course(name=course.name, level=course.level)
    db.add(new_course)
    
    # Commit and refresh the new course instance from the database
    db.commit()
    db.refresh(new_course)

    return new_course

@router.get("/courses/{id}", response_model=Course)
async def read_course(id: int, db: Session = next(get_db())):
    course = db.query(Course).filter(Course.id == id).first()
    
    # Raise a 404 error if the course doesn't exist
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    return course