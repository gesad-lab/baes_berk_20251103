```python
# src/services.py

from sqlalchemy.orm import Session
from src.models import Student, Course, StudentCourse
from src.database import get_db_session
from typing import List, Dict, Union

def get_courses_for_student(student_id: int) -> Union[Dict[str, Union[str, List[Dict]]], Dict[str, str]]:
    """
    Retrieve all courses associated with a specific student.
    
    :param student_id: The ID of the student whose courses are to be retrieved.
    :return: A dictionary with a list of courses if the student is enrolled in any, 
             or a message indicating no courses are found.
    """
    # Fetching the current database session
    session: Session = get_db_session()

    # Querying the student along with their courses
    student = session.query(Student).filter(Student.id == student_id).first()

    if not student:
        # If the student does not exist, return an appropriate message
        return {"error": "E001", "message": "Student not found."}

    # Fetching the related courses through the StudentCourse relationship
    courses = (
        session.query(Course)
        .join(StudentCourse)
        .filter(StudentCourse.student_id == student_id)
        .all()
    )

    if courses:
        # Formatting the list of courses to return structured data
        course_details = [{"id": course.id, "name": course.name} for course in courses]
        return {"courses": course_details}
    else:
        # If the student has no associated courses
        return {"message": "No courses found for this student."}
```