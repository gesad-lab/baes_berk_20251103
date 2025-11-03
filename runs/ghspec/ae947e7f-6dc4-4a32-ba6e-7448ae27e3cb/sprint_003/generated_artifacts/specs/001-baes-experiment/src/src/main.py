```python
from fastapi import FastAPI, HTTPException
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from typing import List

DATABASE_URL = "sqlite:///./test.db"  # Use your actual database URL

# SQLAlchemy setup
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Course model
class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

# Create tables
Base.metadata.create_all(bind=engine)

# API parameters model
class CourseCreate(BaseModel):
    name: str
    level: str

# FastAPI app
app = FastAPI()

@app.post("/courses", response_model=CourseCreate)
def create_course(course: CourseCreate):
    """Create a new course with the given name and level."""
    db = SessionLocal()
    db_course = Course(name=course.name, level=course.level)
    
    try:
        db.add(db_course)
        db.commit()
        db.refresh(db_course)
    except Exception as e:
        db.rollback()  # Rollback in case of error
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()

    return db_course

@app.get("/courses/{course_id}", response_model=CourseCreate)
def read_course(course_id: int):
    """Retrieve a course by its ID."""
    db = SessionLocal()
    course = db.query(Course).filter(Course.id == course_id).first()

    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    
    return course
```