```python
from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from models import Course, Teacher
from database import get_db

router = APIRouter()

@router.get("/courses", response_model=list[Course])
async def list_courses(db: Session = next(get_db())):
    """
    Retrieve a list of all courses with their associated teacher information.

    Args:
        db (Session): The database session.

    Returns:
        list[Course]: A list of Course objects including teacher details.
    """
    try:
        courses = db.query(Course).all()  # Fetch all courses from the database
        return courses
    except Exception as e:
        # Log the exception and raise an HTTP error
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.put("/courses/{course_id}/assign-teacher", status_code=status.HTTP_204_NO_CONTENT)
async def assign_teacher_to_course(course_id: int, teacher_id: int, db: Session = next(get_db())):
    """
    Assign a teacher to a specific course.

    Args:
        course_id (int): The ID of the course to which the teacher will be assigned.
        teacher_id (int): The ID of the teacher to be assigned to the course.
        db (Session): The database session.

    Raises:
        HTTPException: If course or teacher does not exist.
    """
    course = db.query(Course).filter(Course.id == course_id).first()  # Fetch course by ID
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()  # Fetch teacher by ID
    if not teacher:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")

    # Assign the teacher to the course and commit the change
    course.teacher_id = teacher_id
    db.commit()
```
