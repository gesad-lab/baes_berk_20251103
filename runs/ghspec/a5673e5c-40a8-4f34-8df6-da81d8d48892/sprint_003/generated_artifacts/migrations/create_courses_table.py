```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, constr
from sqlalchemy.orm import Session
from .models import Course  # Assuming Course model is already defined in models.py
from .database import get_db  # Assuming there's a function to get the database session

app = FastAPI()

# Pydantic schema for creating and updating Course
class CourseCreate(BaseModel):
    name: constr(min_length=1)  # Ensures name is a non-empty string
    level: constr(min_length=1)  # Ensures level is a non-empty string

class CourseOut(BaseModel):
    id: int
    name: str
    level: str

@app.post("/courses/", response_model=CourseOut)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    """Create a new course with name and level."""
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@app.get("/courses/{course_id}", response_model=CourseOut)
def get_course(course_id: int, db: Session = Depends(get_db)):
    """Retrieve the details of a course by ID."""
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@app.put("/courses/{course_id}", response_model=CourseOut)
def update_course_level(course_id: int, course: CourseCreate, db: Session = Depends(get_db)):
    """Update the level of an existing course."""
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    
    db_course.level = course.level
    db.commit()
    db.refresh(db_course)
    return db_course
```