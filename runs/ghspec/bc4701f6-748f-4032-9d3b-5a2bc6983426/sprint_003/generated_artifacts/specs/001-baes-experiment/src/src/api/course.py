```python
from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from typing import Dict
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a new SQLAlchemy base class for the Course model
Base = declarative_base()

# Database setup (assuming SQLite for this example)
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the data model for Course
class Course(Base):
    __tablename__ = "courses"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

# Create the database tables (including Course)
Base.metadata.create_all(bind=engine)

# Pydantic model for request validation
class CourseCreate(BaseModel):
    name: str
    level: str

# FastAPI app instance
app = FastAPI()

# In-memory data store for simplicity (may be replaced with a proper database in the future)
courses: Dict[int, Course] = {}
id_counter = 1  # Simple counter for unique course IDs

@app.post("/courses", status_code=201)
def create_course(course: CourseCreate):
    global id_counter

    # Input validation for required fields
    if not course.name or not course.level:
        raise HTTPException(
            status_code=400,
            detail={"error": {"code": "E001", "message": "Both name and level are required."}}
        )
    
    # Create the new course instance
    new_course = Course(id=id_counter, name=course.name, level=course.level)
    
    # Increment the ID for the next course
    courses[id_counter] = new_course
    id_counter += 1

    return {"id": new_course.id, "name": new_course.name, "level": new_course.level}

@app.get("/courses/{course_id}")
def get_course(course_id: int):
    # Retrieve the course by ID, handle case where course is not found
    course = courses.get(course_id)
    if course is None:
        raise HTTPException(
            status_code=404,
            detail={"error": {"code": "E002", "message": "Course not found."}}
        )
    
    return {"id": course.id, "name": course.name, "level": course.level}
```