```python
# src/routes/course_routes.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.models import Course, Teacher
from src.database import get_db

router = APIRouter()

@router.post("/courses/{course_id}/assign_teacher")
def assign_teacher_to_course(course_id: int, teacher_id: int, db: Session = Depends(get_db)):
    """
    Assign a teacher to a course.

    Args:
        course_id (int): The ID of the course to which the teacher will be assigned.
        teacher_id (int): The ID of the teacher to assign to the course.
        db (Session): Database session dependency.

    Returns:
        JSON response indicating success or failure.
    """
    # Validate that a teacher_id has been provided
    if not teacher_id:
        # Raise an HTTP exception with status code 400 and a specific error message
        raise HTTPException(
            status_code=400,
            detail={"error": {"code": "E001", "message": "A teacher must be selected."}}
        )

    # Fetch the course from the database
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found.")

    # Fetch the teacher from the database
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found.")

    # Assign the teacher to the course
    course.teacher_id = teacher.id
    db.commit()

    return {"message": "Teacher assigned successfully."}

@router.get("/courses/{course_id}")
def get_course(course_id: int, db: Session = Depends(get_db)):
    """
    Retrieve course information including the assigned teacher details.

    Args:
        course_id (int): The ID of the course to retrieve.
        db (Session): Database session dependency.

    Returns:
        JSON response containing course information and assigned teacher details.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found.")
    
    # Prepare course information, including teacher details if assigned
    course_info = {
        "id": course.id,
        "name": course.name,
        "teacher": {
            "id": course.teacher.id if course.teacher else None,
            "name": course.teacher.name if course.teacher else None,
            "email": course.teacher.email if course.teacher else None
        }
    }
    
    return course_info
```