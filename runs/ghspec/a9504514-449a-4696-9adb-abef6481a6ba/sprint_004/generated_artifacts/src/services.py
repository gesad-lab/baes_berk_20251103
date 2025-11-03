```python
from typing import List, Dict
from src.models import StudentCourses, Course
from src.database import db

def get_courses_for_student(student_id: int) -> List[Dict]:
    """
    Retrieve all courses linked to a specific student.

    Args:
        student_id (int): The ID of the student for whom we want to retrieve the courses.

    Returns:
        List[Dict]: A list of dictionaries representing the courses linked to the student,
                     with each dictionary containing the course ID, name, and level.
    
    Raises:
        ValueError: If the student ID is invalid or does not exist.
    """
    # Validate the student ID
    if student_id <= 0:
        raise ValueError("Invalid student ID. Student ID must be a positive integer.")
    
    # Query the StudentCourses table to find courses linked to the student
    courses = db.session.query(Course).\
        join(StudentCourses).\
        filter(StudentCourses.student_id == student_id).\
        all()
    
    # Construct the result as a list of dictionaries
    course_list = [
        {"id": course.id, "name": course.name, "level": course.level}
        for course in courses
    ]
    
    return course_list


def enroll_student_in_course(student_id: int, course_id: str) -> Dict:
    """
    Enroll a student in a given course.

    Args:
        student_id (int): The ID of the student to enroll.
        course_id (str): The ID of the course to enroll the student in (UUID format).

    Returns:
        Dict: A confirmation message with student ID and course ID.
    
    Raises:
        ValueError: If the student ID or course ID is invalid.
    """
    # Validate the IDs
    if student_id <= 0:
        raise ValueError("Invalid student ID. Student ID must be a positive integer.")
    if not isinstance(course_id, str) or len(course_id) == 0:
        raise ValueError("Invalid course ID. Course ID must be a non-empty string.")
    
    # Check if the student and course exist before enrolling
    student_exists = db.session.query(StudentCourses).filter_by(student_id=student_id).first()
    course_exists = db.session.query(Course).filter_by(id=course_id).first()

    if student_exists is None:
        raise ValueError("Student does not exist.")
    if course_exists is None:
        raise ValueError("Course does not exist.")

    # Create the enrollment relationship
    enrollment = StudentCourses(student_id=student_id, course_id=course_id)
    db.session.add(enrollment)
    db.session.commit()
    
    return {"student_id": student_id, "course_id": course_id, "message": "Enrollment successful."}
```