```python
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.models import Course, Teacher, CourseCreate, CourseResponse
from src.database import get_db

router = APIRouter()

@router.get("/courses/{course_id}", response_model=CourseResponse)
def get_course_details(course_id: int, db: Session = Depends(get_db)):
    """
    Retrieve Course details including associated Teacher information.

    Args:
        course_id (int): The ID of the Course to retrieve.
        db (Session): The database session to use.

    Returns:
        CourseResponse: The details of the Course, including associated Teacher information.

    Raises:
        HTTPException: If the Course is not found.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Prepare response data
    response_data = {
        "id": course.id,
        "name": course.name,
        "teacher_name": course.teacher.name if course.teacher else None,
        "teacher_email": course.teacher.email if course.teacher else None,
    }

    return response_data

@router.post("/courses/{course_id}/teachers")
def assign_teacher_to_course(course_id: int, teacher_id: int, db: Session = Depends(get_db)):
    """
    Associate a Teacher with a Course.

    Args:
        course_id (int): The ID of the Course to associate the Teacher with.
        teacher_id (int): The ID of the Teacher to associate with the Course.
        db (Session): The database session to use.

    Returns:
        JSON Response: Confirmation of teacher assignment.

    Raises:
        HTTPException: If the Course or Teacher is not found.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")

    # Associate the Teacher with the Course
    course.teacher_id = teacher.id
    db.commit()

    return {"teacher_id": teacher.id}
```