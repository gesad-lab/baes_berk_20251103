```python
from typing import List
from sqlalchemy.orm import Session
from src.models import Student, Course, StudentCourse  # Assuming the association table is defined as StudentCourse
from src.database import get_db


def associate_student_with_courses(student_id: int, course_ids: List[int], db: Session) -> None:
    """
    Associate a student with one or more courses by creating entries in the student_courses association table.

    Parameters:
        student_id (int): The ID of the student to associate with courses.
        course_ids (List[int]): A list of course IDs to associate with the student.
        db (Session): SQLAlchemy session object for database operations.

    Raises:
        ValueError: If the student or any specified course does not exist in the database.
    """
    # Validate student existence
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise ValueError(f"Student with ID {student_id} does not exist.")

    # Validate course existence
    courses = db.query(Course).filter(Course.id.in_(course_ids)).all()
    if len(courses) != len(course_ids):
        raise ValueError("One or more course IDs do not exist.")

    # Create associations in the database
    for course in courses:
        association = StudentCourse(student_id=student.id, course_id=course.id)
        db.add(association)
    
    db.commit()  # Commit the transaction to save the changes
```