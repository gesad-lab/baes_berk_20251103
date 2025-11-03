from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Database setup
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Course model definition
class Course(Base):
    __tablename__ = "courses"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)

# Pydantic model for validating request data
class CourseCreate(BaseModel):
    name: str = Field(..., min_length=1, title="Course Name")
    level: str = Field(..., min_length=1, title="Course Level")

class CourseResponse(CourseCreate):
    id: int

# FastAPI app creation
app = FastAPI()

# Dependency for getting the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/courses", response_model=CourseResponse, status_code=201)
async def create_course(course: CourseCreate, db: Session = next(get_db())):
    """
    Create a new course with the specified name and level.
    Validates that required fields are not empty.
    """
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@app.get("/courses/{course_id}", response_model=CourseResponse)
async def get_course(course_id: int, db: Session = next(get_db())):
    """
    Retrieve a course by its ID.
    Returns course details including name and level.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course