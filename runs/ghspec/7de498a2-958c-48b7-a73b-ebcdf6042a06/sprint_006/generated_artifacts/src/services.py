```python
from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models import Course, Teacher

def assign_teacher_to_course(db: Session, course_id: int, teacher_id: int):
    """
    Assign a teacher to a course.

    Parameters:
    - db: Database session.
    - course_id: ID of the course to which the teacher will be assigned.
    - teacher_id: ID of the teacher that will be assigned to the course.

    Returns:
    - The updated Course object.

    Raises:
    - HTTPException: If the course or teacher is not found.
    """
    # Fetch the course and teacher from the database
    course = db.query(Course).filter(Course.id == course_id).first()
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()

    # Check if both course and teacher exist
    if course is None or teacher is None:
        raise HTTPException(status_code=404, detail="Course or Teacher not found")
    
    # Assign the teacher to the course
    course.teacher_id = teacher_id
    db.commit()
    db.refresh(course)  # Refresh the course object to reflect changes
    return course

def remove_teacher_from_course(db: Session, course_id: int):
    """
    Remove the teacher assignment from a course.

    Parameters:
    - db: Database session.
    - course_id: ID of the course from which the teacher will be removed.

    Returns:
    - The updated Course object.

    Raises:
    - HTTPException: If the course is not found.
    """
    # Fetch the course from the database
    course = db.query(Course).filter(Course.id == course_id).first()
    
    # Check if the course exists
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    
    # Remove the teacher assignment
    course.teacher_id = None
    db.commit()
    return course
```