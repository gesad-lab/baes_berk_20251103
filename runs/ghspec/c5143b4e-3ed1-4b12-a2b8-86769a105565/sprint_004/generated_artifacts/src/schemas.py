```python
from typing import List
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.models import Student, Course


class StudentWithCourses(BaseModel):
    id: str
    name: str
    courses: List[str]

    class Config:
        orm_mode = True


def get_student_with_courses(student_id: str, db: Session) -> StudentWithCourses:
    """
    Retrieve a student along with their enrolled courses.

    Parameters:
        student_id (str): The ID of the student to retrieve.
        db (Session): The database session to use for the query.

    Returns:
        StudentWithCourses: A StudentWithCourses object containing student details
                            and their enrolled course IDs.

    Raises:
        ValueError: If the student is not found in the database.
    """
    # Retrieve the student record from the database
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise ValueError(f"Student with ID {student_id} does not exist.")
    
    # Fetch course IDs that the student is enrolled in
    course_ids = [course.id for course in student.courses]  # Assuming 'courses' relationship is set up

    return StudentWithCourses(id=student.id, name=student.name, courses=course_ids)
```