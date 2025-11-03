```python
# src/services/course_service.py

from pydantic import BaseModel, conint
from sqlalchemy.orm import Session
from models import Course, Teacher

class AssignTeacherRequest(BaseModel):
    teacher_id: conint(gt=0)  # Teacher ID must be a positive integer

def assign_teacher_to_course(course_id: int, teacher_id: int, db: Session):
    """
    Assign a teacher to a course.

    Parameters:
    - course_id: ID of the course to which the teacher will be assigned
    - teacher_id: ID of the teacher to assign to the course

    Returns:
    - course: The updated course record after assigning the teacher
    """

    # Validate Course existence
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise ValueError(f"Course with ID {course_id} does not exist")

    # Validate Teacher existence
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher is None:
        raise ValueError(f"Teacher with ID {teacher_id} does not exist")

    # Assign teacher to course
    course.teacher_id = teacher_id
    db.commit()
    db.refresh(course)

    return course
```