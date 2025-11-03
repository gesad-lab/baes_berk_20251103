```python
# src/routes/course_routes.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from typing import List, Optional

# Define the SQLAlchemy base
Base = declarative_base()

# Define the Course model
class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

# Pydantic schema for course creation
class CourseCreate(BaseModel):
    name: str
    level: str

# Pydantic schema for course response
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str

    class Config:
        orm_mode = True

# Create a FastAPI router
router = APIRouter()

# Create a database session
DATABASE_URL = "sqlite:///./test.db"  # or your desired database URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@router.post("/courses", response_model=CourseResponse)
def create_course(course: CourseCreate):
    """
    Create a new course with the provided name and level.
    
    Args:
        course (CourseCreate): The course data to be created.
    
    Returns:
        CourseResponse: The created course object with its ID.
    
    Raises:
        HTTPException: If the course creation fails.
    """
    db: Session = SessionLocal()
    db_course = Course(name=course.name, level=course.level)

    try:
        db.add(db_course)
        db.commit()
        db.refresh(db_course)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()

    return db_course

@router.get("/courses", response_model=List[CourseResponse])
def list_courses(skip: int = 0, limit: int = 100):
    """
    Retrieve a list of all courses.
    
    Args:
        skip (int): Number of records to skip (pagination).
        limit (int): Maximum number of records to return.
    
    Returns:
        List[CourseResponse]: A list of courses.
    """
    db: Session = SessionLocal()
    courses = db.query(Course).offset(skip).limit(limit).all()
    db.close()
    return courses

# Include the router in the main application (assumed to be defined elsewhere)
# from fastapi import FastAPI
# app = FastAPI()
# app.include_router(router)
```