from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models import db

class StudentCourses(db.Model):
    """
    Represents the association between students and courses.

    Attributes:
        id (int): The unique identifier for the association (Primary Key).
        student_id (int): The unique identifier of the student (Foreign Key).
        course_id (int): The unique identifier of the course (Foreign Key).
    """

    __tablename__ = 'student_courses'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)

    student = relationship('Student', back_populates='courses')
    course = relationship('Course', back_populates='students')


def associate_student_with_courses(student_id: int, course_ids: list[int]) -> str:
    """
    Associates a student with specified courses.

    Parameters:
        student_id (int): The ID of the student.
        course_ids (list[int]): A list of course IDs to associate with the student.

    Returns:
        str: Confirmation message indicating the successful association of courses to the student.
    """
    for course_id in course_ids:
        association = StudentCourses(student_id=student_id, course_id=course_id)
        db.session.add(association)
    db.session.commit()
    return f"Student {student_id} has been successfully associated with courses {course_ids}."


def get_courses_for_student(student_id: int) -> list[dict]:
    """
    Retrieves all courses associated with a given student.

    Parameters:
        student_id (int): The ID of the student.

    Returns:
        list[dict]: A list of course names and levels for the associated courses.
    """
    courses = db.session.query(StudentCourses).filter_by(student_id=student_id).all()
    course_details = []
    for association in courses:
        course = db.session.query(Course).get(association.course_id)
        course_details.append({"name": course.name, "level": course.level})
    return course_details


def list_all_students_with_courses() -> list[dict]:
    """
    Lists all students along with their respective course enrollments.

    Returns:
        list[dict]: A list of students and their associated courses.
    """
    students = db.session.query(Student).all()
    student_enrollments = []

    for student in students:
        courses = get_courses_for_student(student.id)
        student_enrollments.append({"student_id": student.id, 
                                     "name": student.name, 
                                     "courses": courses})
    return student_enrollments