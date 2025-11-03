```python
# src/services/student_course_service.py

from sqlalchemy.orm import Session
from src.models.student_courses import StudentCourses
from src.models.student import Student
from src.models.course import Course
from sqlalchemy.exc import IntegrityError

def associate_student_with_course(student_id: int, course_id: int, db: Session):
    """
    Associate a student with a course by adding an entry in the StudentCourses table.

    :param student_id: ID of the student to associate.
    :param course_id: ID of the course to associate with the student.
    :param db: Database session for executing the transaction.
    :raises ValueError: If the student or course does not exist.
    :raises IntegrityError: If association already exists or constraints are violated.
    :return: Success message upon association.
    """
    # Check if both the student and course exist
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise ValueError(f"E001: Student with ID {student_id} does not exist.")
    
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise ValueError(f"E002: Course with ID {course_id} does not exist.")

    # Attempt to create a new association in StudentCourses
    try:
        association = StudentCourses(student_id=student_id, course_id=course_id)
        db.add(association)
        db.commit()  # Save the association to the database
    except IntegrityError:
        db.rollback()  # Rollback changes on error
        raise ValueError("E003: This association already exists.")

    return {"message": "Successfully associated student with course."}

def get_student_courses(student_id: int, db: Session):
    """
    Retrieve all courses associated with a given student.

    :param student_id: ID of the student whose courses are to be retrieved.
    :param db: Database session for executing the query.
    :return: List of courses associated with the student.
    :raises ValueError: If the student does not exist.
    """
    # Check if the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise ValueError(f"E001: Student with ID {student_id} does not exist.")

    # Retrieve courses associated with the student
    courses = student.courses  # Assuming student.courses holds the relationship
    return courses
```