```python
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models import Course, Teacher  # Import Course and Teacher models

def assign_teacher_to_course(course_id: int, teacher_id: int, db: Session):
    """
    Assigns a teacher to a course.

    Parameters:
    - course_id: The ID of the course to which the teacher will be assigned.
    - teacher_id: The ID of the teacher to be assigned.
    - db: The database session.

    Raises:
    - HTTPException: If the course or teacher does not exist.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with ID {course_id} not found."
        )

    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Teacher with ID {teacher_id} not found."
        )

    # Assign the teacher to the course
    course.teacher_id = teacher_id
    db.commit()
    db.refresh(course)
    return course

def get_course_details(course_id: int, db: Session):
    """
    Retrieves details of a specific course along with its assigned teacher.

    Parameters:
    - course_id: The ID of the course to retrieve details for.
    - db: The database session.

    Returns:
    - Course: The course details with the associated teacher.

    Raises:
    - HTTPException: If the course does not exist.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with ID {course_id} not found."
        )
    
    return course  # Return the course object which includes the assigned teacher
```