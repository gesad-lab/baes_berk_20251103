```python
# app/api/course.py

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from typing import List

router = APIRouter()

@router.patch("/courses/{id}/assign-teacher")
async def assign_teacher_to_course(id: int, teacher_id: str, db: Session):
    """
    Assign a teacher to a course.

    Parameters:
    - id: The ID of the course to update.
    - teacher_id: The ID of the teacher to assign.

    Returns:
    - Confirmation message in JSON format.

    Raises:
    - HTTPException: If the course or teacher does not exist.
    """
    course = db.query(models.Course).filter(models.Course.id == id).first()
    teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found.")
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found.")

    course.teacher_id = teacher_id
    db.commit()
    db.refresh(course)

    return {"message": "Teacher assigned to course successfully."}

@router.get("/courses/{id}", response_model=schemas.Course)
async def get_course(id: int, db: Session):
    """
    Retrieve course details by course ID, including associated teacher information.

    Parameters:
    - id: The ID of the course to retrieve.

    Returns:
    - Course details in JSON format.

    Raises:
    - HTTPException: If the course is not found.
    """
    course = db.query(models.Course).filter(models.Course.id == id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found.")

    return course
```