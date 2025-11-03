```python
# src/controllers/course_controller.py

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from models import Course, Teacher  # Import necessary models
from database import get_db  # Assuming this is the function to get a database session

router = APIRouter()

@router.put("/courses/{course_id}/assign_teacher")
async def assign_teacher(course_id: int, teacher_data: dict, db: Session = Depends(get_db)):
    """
    Assign a teacher to a course.
    
    Parameters:
    - course_id (int): The ID of the course to which a teacher is to be assigned.
    - teacher_data (dict): Contains the teacher_id for the assignment.

    Raises:
    - HTTPException: If the course does not exist or teacher_id is missing.

    Returns:
    - dict: Confirmation of the teacher assignment.
    """
    
    # Validate presence of teacher_id in request body
    if "teacher_id" not in teacher_data:
        raise HTTPException(status_code=400, detail={
            "error": {
                "code": "E001",
                "message": "Missing 'teacher_id' in request data."
            }
        })

    # Fetch the course to validate if it exists
    course = db.query(Course).filter(Course.id == course_id).first()

    if not course:
        raise HTTPException(status_code=404, detail={
            "error": {
                "code": "E002",
                "message": "Course not found."
            }
        })

    # Fetch teacher to ensure it exists
    teacher = db.query(Teacher).filter(Teacher.id == teacher_data['teacher_id']).first()

    if not teacher:
        raise HTTPException(status_code=404, detail={
            "error": {
                "code": "E003",
                "message": "Teacher not found."
            }
        })

    # Assign the teacher to the course
    course.teacher_id = teacher_data['teacher_id']
    db.commit()

    return {
        "message": "Teacher assigned successfully.",
        "course_id": course.id,
        "teacher_id": teacher_data['teacher_id']
    }
```