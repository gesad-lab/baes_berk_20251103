```python
from typing import List
from sqlalchemy.orm import Session
from models import Student, Course, StudentCourse
from fastapi import HTTPException, status

def enroll_student_in_courses(student_id: int, course_ids: List[int], db: Session):
    """
    Enroll a student in one or more courses.

    Args:
        student_id (int): The ID of the student to enroll.
        course_ids (List[int]): A list of course IDs to enroll the student in.
        db (Session): The database session to use for the operation.

    Returns:
        Student: The updated student object with enrolled courses.

    Raises:
        HTTPException: If the student does not exist or if a course ID is invalid.
    """
    # Fetch the student from the database
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Student with ID {student_id} not found.")

    # Validate each course ID and associate it with the student
    for course_id in course_ids:
        course = db.query(Course).filter(Course.id == course_id).first()
        if not course:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=f"Course with ID {course_id} does not exist.")
        
        # Create a new association entry for the StudentCourse relationship
        student_course = StudentCourse(student_id=student_id, course_id=course_id)
        db.add(student_course)

    # Commit the transaction to save relationships
    db.commit()
    db.refresh(student)  # Fetch the updated student data

    return student  # Return the updated student object
```