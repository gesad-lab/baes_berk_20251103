from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.exc import SQLAlchemyError
from typing import List

from models import Student, Course, StudentCourse, session


def enroll_student_in_course(student_id: int, course_id: int) -> str:
    """
    Enrolls a student in a specified course.

    :param student_id: The ID of the student to enroll.
    :param course_id: The ID of the course to enroll the student in.
    :return: A message indicating the enrollment status.
    """
    try:
        # Check if the student exists
        student = session.query(Student).filter(Student.id == student_id).first()
        if not student:
            return "E001: Student not found"
        
        # Check if the course exists
        course = session.query(Course).filter(Course.id == course_id).first()
        if not course:
            return "E002: Course not found"
        
        # Create a new StudentCourse relationship and add to the session
        enrollment = StudentCourse(student_id=student_id, course_id=course_id)
        session.add(enrollment)
        session.commit()

        return "Enrollment successful"
    
    except SQLAlchemyError as e:
        session.rollback()  # Rollback session on error
        return f"Error during enrollment: {str(e)}"


def get_student_courses(student_id: int) -> List[int]:
    """
    Retrieves the courses a student is enrolled in.

    :param student_id: The ID of the student whose courses to retrieve.
    :return: A list of course IDs the student is enrolled in.
    """
    try:
        # Retrieve courses for the specified student
        student_courses = session.query(StudentCourse).filter(StudentCourse.student_id == student_id).all()
        return [sc.course_id for sc in student_courses]
    
    except SQLAlchemyError as e:
        return f"Error retrieving courses: {str(e)}"


def remove_course_from_student(student_id: int, course_id: int) -> str:
    """
    Removes a specified course from a student's enrollments.

    :param student_id: The ID of the student from whom the course will be removed.
    :param course_id: The ID of the course to remove.
    :return: A message indicating the removal status.
    """
    try:
        # Find the enrollment record to remove
        enrollment = session.query(StudentCourse).filter(
            StudentCourse.student_id == student_id,
            StudentCourse.course_id == course_id
        ).first()
        
        if not enrollment:
            return "E003: Enrollment not found"
        
        session.delete(enrollment)
        session.commit()

        return "Course removed from student successfully"
    
    except SQLAlchemyError as e:
        session.rollback()  # Rollback session on error
        return f"Error removing course: {str(e)}"