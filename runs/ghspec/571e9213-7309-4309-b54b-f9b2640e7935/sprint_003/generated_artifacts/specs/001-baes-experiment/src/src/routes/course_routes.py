```python
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from models.course import Course
from schemas.course_schema import CourseSchema
from database import SessionLocal

router = APIRouter()

@router.post("/courses", response_model=CourseSchema)
def create_course(course: CourseSchema):
    """
    Create a new course in the database.
    
    Args:
        course (CourseSchema): The course data to be stored.
        
    Returns:
        CourseSchema: The created course with its details.
        
    Raises:
        HTTPException: If the course data is invalid or if an error occurs during database operation.
    """
    # Validate required fields
    if not course.name or not course.level:
        raise HTTPException(status_code=400, detail="Name and level are required.")

    db: Session = SessionLocal()
    try:
        new_course = Course(name=course.name, level=course.level)
        db.add(new_course)
        db.commit()
        db.refresh(new_course)
        return new_course
    except Exception as e:
        db.rollback()  # Rollback in case of error
        raise HTTPException(status_code=500, detail="An error occurred while creating the course.")
    finally:
        db.close()

@router.get("/courses/{id}", response_model=CourseSchema)
def get_course(id: int):
    """
    Retrieve a course by its ID.
    
    Args:
        id (int): The ID of the course to retrieve.
        
    Returns:
        CourseSchema: The course details.
        
    Raises:
        HTTPException: If the course is not found.
    """
    db: Session = SessionLocal()
    course = db.query(Course).filter(Course.id == id).first()
    
    if not course:
        raise HTTPException(status_code=404, detail=f"Course with ID {id} not found.")
    return course
```