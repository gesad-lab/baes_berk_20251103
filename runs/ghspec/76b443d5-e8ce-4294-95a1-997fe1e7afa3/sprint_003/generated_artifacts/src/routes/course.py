```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Extra
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Course  # Assuming Course is defined in models.py

router = APIRouter()

class CourseCreate(BaseModel):
    """Pydantic model for creating a Course."""
    name: str
    level: str

    class Config:
        extra = Extra.forbid  # Prevent extra fields in request body

@router.post("/courses", response_model=Course)
async def create_course(course: CourseCreate, db: Session = next(get_db())):
    """API endpoint to create a new Course."""
    if not course.name:
        raise HTTPException(status_code=400, detail={"code": "E001", "message": "Name is required."})

    if not course.level:
        raise HTTPException(status_code=400, detail={"code": "E002", "message": "Level is required."})

    new_course = Course(name=course.name, level=course.level)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return new_course

@router.get("/courses/{course_id}", response_model=Course)
async def get_course(course_id: int, db: Session = next(get_db())):
    """API endpoint to retrieve a Course by ID."""
    course = db.query(Course).filter(Course.id == course_id).first()
    
    if course is None:
        raise HTTPException(status_code=404, detail={"code": "E003", "message": "Course not found."})

    return course
```