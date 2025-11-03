```python
from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel, conint
from src.models import Course  # Import the Course model
from src.database import get_db  # Assuming a function to get the database session

router = APIRouter()

class AssignTeacherRequest(BaseModel):
    teacher_id: conint(gt=0)  # Ensures teacher_id is a positive integer

@router.post("/courses/{course_id}/assign_teacher")
async def assign_teacher(course_id: int, request: AssignTeacherRequest, db=Depends(get_db)):
    """
    Assign a teacher to a course.

    Args:
        course_id (int): The ID of the course.
        request (AssignTeacherRequest): The request body containing teacher_id.

    Returns:
        JSON: Confirmation of assignment with course_id and teacher_id.
    """
    # Validate that the course exists in the database
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Validate that the teacher_id is a valid teacher in the database
    teacher = db.query(Teacher).filter(Teacher.id == request.teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=400, detail="Invalid teacher ID")

    # Assign the teacher to the course
    course.teacher_id = request.teacher_id
    db.commit()

    return {"course_id": course.id, "teacher_id": request.teacher_id}

@router.put("/courses/{course_id}/update_teacher")
async def update_teacher(course_id: int, request: AssignTeacherRequest, db=Depends(get_db)):
    """
    Update the teacher assigned to a course.

    Args:
        course_id (int): The ID of the course.
        request (AssignTeacherRequest): The request body containing teacher_id.

    Returns:
        JSON: Confirmation of the update with course details and new teacher information.
    """
    # Validate that the course exists in the database
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Validate that the teacher_id is a valid teacher in the database
    teacher = db.query(Teacher).filter(Teacher.id == request.teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=400, detail="Invalid teacher ID")

    # Update the teacher for the course
    course.teacher_id = request.teacher_id
    db.commit()

    return {
        "course_id": course.id,
        "new_teacher": {
            "id": teacher.id,
            "name": teacher.name,
            "email": teacher.email
        }
    }

# Add the functionality for removing the teacher from the course if required
```