```python
# src/services/student_course_service.py

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from src.models import Student, Course, StudentCourses  # Assuming StudentCourses model is defined in src/models/student_courses.py
from flask import jsonify

def assign_courses_to_student(student_id: int, course_ids: list[int], db: Session) -> dict:
    """
    Assigns one or more courses to a student.

    Parameters:
    - student_id (int): The ID of the student to whom courses are being assigned.
    - course_ids (list[int]): A list of course IDs to assign to the student.
    - db (Session): The database session for performing operations.

    Returns:
    - dict: A response containing success status and updated student data.
    """
    try:
        student = db.query(Student).filter(Student.id == student_id).one()
        for course_id in course_ids:
            course = db.query(Course).filter(Course.id == course_id).one()
            student_course_entry = StudentCourses(student_id=student.id, course_id=course.id)
            db.add(student_course_entry)
        db.commit()
        return jsonify({"status": "success", "student_id": student_id, "course_ids": course_ids}), 200
    except IntegrityError:
        db.rollback()  # Rollback transaction on integrity error
        return jsonify({"error": {"code": "E002", "message": "Failed to assign courses, check for duplicates or invalid courses."}}), 400
    except Exception as e:
        db.rollback()
        return jsonify({"error": {"code": "E003", "message": "An unexpected error occurred.", "details": str(e)}}), 500

def remove_course_from_student(student_id: int, course_id: int, db: Session) -> dict:
    """
    Removes a course from a student's enrollment.

    Parameters:
    - student_id (int): The ID of the student from whom the course is being removed.
    - course_id (int): The ID of the course to be removed.
    - db (Session): The database session for performing operations.

    Returns:
    - dict: A response indicating the success of the removal operation.
    """
    try:
        student = db.query(Student).filter(Student.id == student_id).one()
        student_course_entry = db.query(StudentCourses).filter(
            StudentCourses.student_id == student.id,
            StudentCourses.course_id == course_id
        ).one()
        db.delete(student_course_entry)
        db.commit()
        return jsonify({"status": "success", "message": f"Course {course_id} removed from student {student_id}."}), 200
    except Exception as e:
        db.rollback()
        return jsonify({"error": {"code": "E004", "message": "Failed to remove course.", "details": str(e)}}), 500

def retrieve_student_with_courses(student_id: int, db: Session) -> dict:
    """
    Retrieves a student's details along with their enrolled courses.

    Parameters:
    - student_id (int): The ID of the student whose details are to be retrieved.
    - db (Session): The database session for performing operations.

    Returns:
    - dict: A response containing student information and enrolled courses.
    """
    try:
        student = db.query(Student).filter(Student.id == student_id).one()
        courses = db.query(Course).join(StudentCourses).filter(StudentCourses.student_id == student.id).all()
        course_list = [{"id": course.id, "name": course.name} for course in courses]
        return jsonify({"student_id": student.id, "name": student.name, "courses": course_list}), 200
    except Exception as e:
        return jsonify({"error": {"code": "E005", "message": "Failed to retrieve student information.", "details": str(e)}}), 500
```