```python
from typing import List
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models import Student, Course, StudentCourse  # Assuming StudentCourse model has been defined

def add_enrollment(student_id: int, course_ids: List[int], db: Session):
    """
    Enroll a student in given course IDs.

    Args:
        student_id (int): The ID of the student to enroll.
        course_ids (List[int]): A list of course IDs to enroll the student in.
        db (Session): The database session to use for queries.

    Raises:
        HTTPException: If the student or any course does not exist or if
        there's an attempt to enroll in an invalid course.
        
    Returns:
        dict: Updated student information including enrolled courses.
    """
    
    # Fetch the student from the database
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID {student_id} does not exist."
        )
    
    # Validate course IDs and keep track of valid courses
    valid_courses = []
    for course_id in course_ids:
        course = db.query(Course).filter(Course.id == course_id).first()
        if not course:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Course with ID {course_id} does not exist."
            )
        valid_courses.append(course)

    # Create associations in StudentCourse relation
    for course in valid_courses:
        student_course = StudentCourse(student_id=student.id, course_id=course.id)
        db.add(student_course)

    # Commit the changes to the database
    db.commit()
    db.refresh(student)

    # Return updated student information
    return {
        "student_id": student.id,
        "name": student.name,  # Assuming the Student model has a 'name' field
        "enrolled_courses": [course.id for course in valid_courses]
    }
```