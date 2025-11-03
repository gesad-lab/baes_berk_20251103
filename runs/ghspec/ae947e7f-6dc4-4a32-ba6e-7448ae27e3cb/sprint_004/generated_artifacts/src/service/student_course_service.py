```python
# src/service/student_course_service.py

from typing import List
from fastapi import HTTPException
from src.model.student import Student
from src.model.course import Course
from src.model.student_course import StudentCourse
from sqlalchemy.orm import Session

def get_student_courses(student_id: int, db: Session) -> List[Course]:
    """
    Retrieve all courses associated with a given student.

    Parameters:
    - student_id: The ID of the student to retrieve courses for.
    - db: The database session to use.

    Returns:
    - A list of Course objects associated with the student.

    Raises:
    - HTTPException: If the student does not exist.
    """
    # Check if the student exists in the database
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")

    # Retrieve courses associated with the student
    courses = db.query(Course).join(StudentCourse).filter(StudentCourse.student_id == student_id).all()
    
    return courses
```