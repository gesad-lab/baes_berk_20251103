```python
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from src.models.course import Course
from src.schemas.course_schema import CourseCreate, CourseResponse
from src.database.database import get_db

router = APIRouter()

@router.post("/courses", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = next(get_db())):
    """Create a new Course entity."""
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@router.get("/courses/{course_id}", response_model=CourseResponse)
def read_course(course_id: int, db: Session = next(get_db())):
    """Retrieve a Course entity by its ID."""
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.put("/courses/{course_id}", response_model=CourseResponse)
def update_course(course_id: int, course: CourseCreate, db: Session = next(get_db())):
    """Update an existing Course entity by its ID."""
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    db_course.name = course.name
    db_course.level = course.level
    db.commit()
    db.refresh(db_course)
    return db_course

# In main.py, include the course routes
# from src.routes.course_routes import router as course_router
# app.include_router(course_router)
```