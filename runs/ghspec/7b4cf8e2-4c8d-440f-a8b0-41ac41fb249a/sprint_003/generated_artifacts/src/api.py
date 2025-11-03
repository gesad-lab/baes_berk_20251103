```python
from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from typing import List, Optional
from src.models import Course  # Assume Course model exists in models.py
from src.database import SessionLocal  # Assume SessionLocal handles database sessions

app = FastAPI()

class CourseCreate(BaseModel):
    name: str
    level: str

class CourseUpdate(BaseModel):
    name: Optional[str] = None
    level: Optional[str] = None

@app.post("/courses", response_model=Course)
def create_course(course: CourseCreate):
    """Create a new course record with a provided name and level."""
    if not course.name or not course.level:
        raise HTTPException(status_code=400, detail="Both name and level are required.")

    db = SessionLocal()
    try:
        new_course = Course(name=course.name, level=course.level)
        db.add(new_course)
        db.commit()
        db.refresh(new_course)
        return new_course
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="An error occurred while creating the course.")
    finally:
        db.close()

@app.get("/courses/{id}", response_model=Course)
def get_course(id: int):
    """Retrieve details of a specific course by ID."""
    db = SessionLocal()
    course = db.query(Course).filter(Course.id == id).first()
    db.close()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found.")
    return course

@app.put("/courses/{id}", response_model=Course)
def update_course(id: int, course_update: CourseUpdate):
    """Update an existing course's name or level by ID."""
    db = SessionLocal()
    course = db.query(Course).filter(Course.id == id).first()
    
    if not course:
        db.close()
        raise HTTPException(status_code=404, detail="Course not found.")

    # Update course fields if provided
    if course_update.name:
        course.name = course_update.name
    if course_update.level:
        course.level = course_update.level

    try:
        db.commit()
        db.refresh(course)
        return course
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="An error occurred while updating the course.")
    finally:
        db.close()
```