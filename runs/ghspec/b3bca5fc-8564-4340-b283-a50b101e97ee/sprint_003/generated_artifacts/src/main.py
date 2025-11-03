```python
# src/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Course  # Assuming Course model is defined in models.py

app = FastAPI()

# Initialize the database and create the Course table if it doesn't exist
@app.on_event("startup")
async def startup():
    # Create the database tables
    Base.metadata.create_all(bind=engine)

# Pydantic model for course creation
class CourseCreate(BaseModel):
    name: str
    level: str

# Pydantic model for course response
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str

@app.post("/courses", response_model=CourseResponse, status_code=201)
async def create_course(course: CourseCreate):
    if not course.name or not course.level:
        raise HTTPException(status_code=400, detail="Both name and level are required")

    db: Session = SessionLocal()
    new_course = Course(name=course.name, level=course.level)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return CourseResponse(id=new_course.id, name=new_course.name, level=new_course.level)

@app.get("/courses", response_model=List[CourseResponse], status_code=200)
async def get_courses():
    db: Session = SessionLocal()
    courses = db.query(Course).all()
    return [CourseResponse(id=course.id, name=course.name, level=course.level) for course in courses]
```