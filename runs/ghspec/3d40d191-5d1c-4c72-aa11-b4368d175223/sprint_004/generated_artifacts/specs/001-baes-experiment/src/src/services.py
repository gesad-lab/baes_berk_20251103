```python
# src/services.py

from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models import StudentCourse  # Assuming the StudentCourse model is defined in models.py

def enroll_student_service(student_id: int, course_id: int, session: Session):
    """
    Enroll a student in a specified course.

    Args:
        student_id (int): The ID of the student to enroll.
        course_id (int): The ID of the course to enroll the student in.
        session (Session): The database session to use for this operation.

    Returns:
        dict: A message confirming the enrollment and the IDs of the student and course.

    Raises:
        HTTPException: If the student_id or course_id is invalid or missing.
    """
    if not course_id:
        raise HTTPException(status_code=400, detail="E001: Missing course_id")
    
    # Create a new StudentCourse entry
    enrollment = StudentCourse(student_id=student_id, course_id=course_id)
    session.add(enrollment)
    
    # Commit changes to the database
    session.commit()
    return {"message": "Enrollment successful", "student_id": student_id, "course_id": course_id}

def get_student_courses_service(student_id: int, session: Session):
    """
    Retrieve all courses that a specified student is enrolled in.

    Args:
        student_id (int): The ID of the student whose courses to retrieve.
        session (Session): The database session to use for this operation.

    Returns:
        list: A list of dictionaries representing the courses, each containing 'id', 'name', and 'level'.

    Raises:
        HTTPException: If the student_id is not found in the database.
    """
    student_courses = session.query(StudentCourse).filter(StudentCourse.student_id == student_id).all()
    
    if not student_courses:
        raise HTTPException(status_code=404, detail="Student not found or no courses enrolled")

    # Construct response data
    course_list = [{"id": sc.course.id, "name": sc.course.name, "level": sc.course.level} for sc in student_courses]
    
    return course_list
```