```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.database import SessionLocal, engine
from src.models.course import Course
from src.models import Base

# Initialize the FastAPI application
app = FastAPI()

# Create the database tables if they do not exist
Base.metadata.create_all(bind=engine)

# Pydantic model for course creation
class CourseCreate(BaseModel):
    name: str
    level: str

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/courses/", response_model=CourseCreate)
def create_course(course: CourseCreate, db: Session = next(get_db())):
    """
    Create a new course with the provided name and level.
    
    Parameters:
    - course: CourseCreate: The course data to be created.
    - db: Session: The database session.

    Returns:
    - CourseCreate: The created course data.
    
    Raises:
    - HTTPException: If name or level is missing.
    """
    if not course.name or not course.level:
        raise HTTPException(status_code=400, detail="Both name and level are required")

    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    
    return db_course

@app.get("/courses/{course_id}", response_model=CourseCreate)
def read_course(course_id: int, db: Session = next(get_db())):
    """
    Retrieve course information by ID.
    
    Parameters:
    - course_id: int: The unique identifier for the course.
    - db: Session: The database session.

    Returns:
    - CourseCreate: The course data.
    
    Raises:
    - HTTPException: If the course does not exist.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    
    return course
```