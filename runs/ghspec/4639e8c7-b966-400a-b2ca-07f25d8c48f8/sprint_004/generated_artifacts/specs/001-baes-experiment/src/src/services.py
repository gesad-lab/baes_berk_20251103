```python
# src/services.py

from src.models import Student, Course, StudentCourse  # Import necessary models
from flask import abort

def associate_student_with_course(student_id: int, course_id: int) -> None:
    """Associates a student with a course.

    Args:
        student_id (int): The ID of the student to associate.
        course_id (int): The ID of the course to associate.

    Raises:
        ValueError: If the student or course does not exist.
    """
    # Validate that the student exists
    student = Student.query.get(student_id)
    if not student:
        abort(404, description=f"Student with ID {student_id} not found.")

    # Validate that the course exists
    course = Course.query.get(course_id)
    if not course:
        abort(404, description=f"Course with ID {course_id} not found.")

    # Check if the association already exists
    existing_association = StudentCourse.query.filter_by(student_id=student_id, course_id=course_id).first()
    if existing_association:
        abort(400, description="This student is already associated with this course.")

    # Create and add the new association
    new_association = StudentCourse(student_id=student_id, course_id=course_id)
    try:
        # Assuming there is an existing session to add the new association
        db.session.add(new_association)
        db.session.commit()
    except Exception as e:
        # Rollback the session in case of error to maintain integrity
        db.session.rollback()
        abort(500, description=f"An error occurred while associating student with course: {str(e)}") 

def get_courses_for_student(student_id: int):
    """Retrieves a list of courses associated with a student.

    Args:
        student_id (int): The ID of the student whose courses to retrieve.

    Returns:
        List[Course]: A list of courses associated with the student.

    Raises:
        ValueError: If the student does not exist.
    """
    student = Student.query.get(student_id)
    if not student:
        abort(404, description=f"Student with ID {student_id} not found.")

    # Retrieve all course associations for the student
    student_courses = StudentCourse.query.filter_by(student_id=student_id).all()
    courses = [course for association in student_courses for course in Course.query.filter_by(id=association.course_id).all()]

    return courses
```