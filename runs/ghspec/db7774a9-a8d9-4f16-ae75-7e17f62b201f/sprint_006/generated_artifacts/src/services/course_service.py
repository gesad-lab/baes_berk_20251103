```python
# src/services/course_service.py

from sqlalchemy.orm import Session
from src.models.course import Course
from src.models.teacher import Teacher
from src.schemas.course import CourseResponse, CourseUpdate
from fastapi import HTTPException, status

def assign_teacher_to_course(course_id: int, teacher_id: int, db: Session) -> CourseResponse:
    """
    Assign a teacher to a course.

    Args:
        course_id (int): The ID of the course to which the teacher will be assigned.
        teacher_id (int): The ID of the teacher to be assigned to the course.
        db (Session): The database session object.

    Returns:
        CourseResponse: The updated course object including the teacher_id.

    Raises:
        HTTPException: If the teacher_id does not reference an existing teacher.
    """
    # Check if the teacher exists
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Teacher with ID {teacher_id} does not exist.",
            headers={"X-Error": "E404: Teacher not found"}
        )

    # Fetch the course to be updated
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with ID {course_id} does not exist.",
            headers={"X-Error": "E404: Course not found"}
        )

    # Update the course with the new teacher_id
    course.teacher_id = teacher_id
    db.commit()
    db.refresh(course)
    
    # Return the updated course information
    return CourseResponse.from_orm(course)
```