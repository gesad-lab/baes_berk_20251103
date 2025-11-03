```python
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from models import Course  # Assuming the Course model is defined in models.py
from database import get_db  # Dependency to get the database session

router = APIRouter()

@router.post("/courses", response_model=dict)
def create_course(name: str, level: str, db: Session = Depends(get_db)):
    """
    Create a new Course with a name and level.

    Parameters:
    - name: The name of the course (str)
    - level: The level of the course (str)
    - db: Database session

    Returns:
    - JSON response with a success message or error message.
    """
    if not name or not level:
        raise HTTPException(status_code=400, detail={"error": "Both name and level are required."})
    
    new_course = Course(name=name, level=level)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return {"message": "Course created successfully", "course": {"id": new_course.id, "name": new_course.name, "level": new_course.level}}

@router.get("/courses/{course_id}", response_model=dict)
def get_course(course_id: int, db: Session = Depends(get_db)):
    """
    Retrieve details of a specific Course by its ID.

    Parameters:
    - course_id: The ID of the course (int)
    - db: Database session

    Returns:
    - JSON response with course details or an error message.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail={"error": "Course not found."})

    return {"id": course.id, "name": course.name, "level": course.level}

@router.put("/courses/{course_id}", response_model=dict)
def update_course(course_id: int, name: Optional[str] = None, level: Optional[str] = None, db: Session = Depends(get_db)):
    """
    Update information of an existing Course.

    Parameters:
    - course_id: The ID of the course (int)
    - name: The new name of the course (Optional[str])
    - level: The new level of the course (Optional[str])
    - db: Database session
    
    Returns:
    - JSON response with a success message or error message.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail={"error": "Course not found."})

    if name:
        course.name = name
    if level:
        course.level = level
    
    db.commit()
    db.refresh(course)
    return {"message": "Course updated successfully", "course": {"id": course.id, "name": course.name, "level": course.level}}

# Include this router in the main application
# from fastapi import FastAPI
# app = FastAPI()
# app.include_router(router)
```