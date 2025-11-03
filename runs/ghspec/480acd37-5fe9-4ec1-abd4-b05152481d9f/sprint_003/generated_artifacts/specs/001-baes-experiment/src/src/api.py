```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
from src.models import Course  # Assuming the Course model is defined in models.py
from src.database import SessionLocal

app = FastAPI()

# Request schema for creating a Course
class CourseCreate(BaseModel):
    name: str = Field(..., example="Mathematics", description="Name of the course")
    level: str = Field(..., example="Beginner", description="Level of the course")

# Request schema for updating a Course
class CourseUpdate(BaseModel):
    name: str = Field(None, example="Mathematics", description="Name of the course")
    level: str = Field(None, example="Beginner", description="Level of the course")

# Response schema for Course
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str

# Dependency to get the database session
def get_db():
    db = SessionLocal()  # Replace with actual db session creation
    try:
        yield db
    finally:
        db.close()

@app.post("/courses", response_model=CourseResponse, status_code=201)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    """
    Create a new course.
    Validates that the name and level are provided.
    """
    new_course = Course(name=course.name, level=course.level)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

@app.get("/courses", response_model=List[CourseResponse])
def get_courses(db: Session = Depends(get_db)):
    """
    Retrieve all courses.
    """
    return db.query(Course).all()

@app.put("/courses/{course_id}", response_model=CourseResponse)
def update_course(course_id: int, course: CourseUpdate, db: Session = Depends(get_db)):
    """
    Update an existing course's name and/or level.
    Validates that the fields are provided.
    """
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    
    if course.name is not None:
        db_course.name = course.name
    if course.level is not None:
        db_course.level = course.level
    
    db.commit()
    db.refresh(db_course)
    return db_course
```