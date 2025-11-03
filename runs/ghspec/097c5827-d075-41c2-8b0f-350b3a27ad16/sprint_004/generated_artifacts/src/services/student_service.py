```python
from typing import List, Dict
from flask import jsonify, request
from src.models import Student, Course, StudentCourses
from src.database import db

def link_courses_to_student(student_id: int, course_ids: List[int]) -> Dict:
    """Link courses to a student by updating the StudentCourses relationship.

    Parameters:
        student_id (int): The ID of the student to link courses to.
        course_ids (List[int]): A list of course IDs to link to the student.

    Returns:
        Dict: The updated student details, including the linked courses.

    Raises:
        ValueError: If any course ID is invalid.
    """
    # Fetch student by ID
    student = Student.query.get(student_id)
    if not student:
        raise ValueError("Student not found.")

    # Validate course IDs and link them
    courses = Course.query.filter(Course.id.in_(course_ids)).all()
    if len(courses) != len(course_ids):
        invalid_ids = set(course_ids) - {course.id for course in courses}
        raise ValueError(f"Invalid course IDs: {', '.join(map(str, invalid_ids))}")

    student.courses.extend(courses)
    db.session.commit()

    return {
        "id": student.id,
        "name": student.name,
        "courses": [{"id": course.id, "name": course.name, "level": course.level} for course in student.courses]
    }


def get_student_courses(student_id: int) -> Dict:
    """Retrieve a student's courses.

    Parameters:
        student_id (int): The ID of the student whose courses to retrieve.

    Returns:
        Dict: The student's details, including their courses.

    Raises:
        ValueError: If the student is not found.
    """
    student = Student.query.get(student_id)
    if not student:
        raise ValueError("Student not found.")

    return {
        "id": student.id,
        "name": student.name,
        "courses": [{"id": course.id, "name": course.name, "level": course.level} for course in student.courses]
    }


def update_student_courses(student_id: int, course_ids: List[int]) -> Dict:
    """Update a student's linked courses.

    Parameters:
        student_id (int): The ID of the student to update.
        course_ids (List[int]): A list of course IDs to link to the student.

    Returns:
        Dict: The updated student details with the new list of courses.

    Raises:
        ValueError: If any course ID is invalid or student is not found.
    """
    student = Student.query.get(student_id)
    if not student:
        raise ValueError("Student not found.")

    # Clear existing courses and validate new course IDs
    student.courses.clear()
    courses = Course.query.filter(Course.id.in_(course_ids)).all()
    if len(courses) != len(course_ids):
        invalid_ids = set(course_ids) - {course.id for course in courses}
        raise ValueError(f"Invalid course IDs: {', '.join(map(str, invalid_ids))}")

    student.courses.extend(courses)
    db.session.commit()

    return {
        "id": student.id,
        "name": student.name,
        "courses": [{"id": course.id, "name": course.name, "level": course.level} for course in student.courses]
    }
```