from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course, Enrollment  # Assuming models are defined in a models.py
from database import get_db  # Assuming there's a database utility for session management
from typing import List

router = APIRouter()

@router.post("/students/{student_id}/enroll")
def enroll_student(student_id: int, course_id: int, db: Session = next(get_db())):
    """
    Enroll a student in a specified course.

    :param student_id: The ID of the student to enroll.
    :param course_id: The ID of the course to enroll the student in.
    :param db: The database session.
    :return: A confirmation message indicating successful enrollment.
    """
    # Check if the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Check if the course exists
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Create an Enrollment instance
    enrollment = Enrollment(student_id=student_id, course_id=course_id)
    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)

    return {"message": "Student enrolled in course successfully"}


@router.get("/students/{student_id}/courses")
def get_student_courses(student_id: int, db: Session = next(get_db())) -> List[Course]:
    """
    Retrieve a list of courses that a student is enrolled in.

    :param student_id: The ID of the student whose courses to retrieve.
    :param db: The database session.
    :return: A list of courses the student is enrolled in.
    """
    # Check if the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Retrieve courses for the student
    courses = db.query(Course).join(Enrollment).filter(Enrollment.student_id == student_id).all()
    return courses


@router.delete("/students/{student_id}/courses/{course_id}")
def remove_student_from_course(student_id: int, course_id: int, db: Session = next(get_db())):
    """
    Remove a student from a specified course.

    :param student_id: The ID of the student to remove from the course.
    :param course_id: The ID of the course to remove the student from.
    :param db: The database session.
    :return: A confirmation message indicating successful removal.
    """
    # Check if the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Check if the course exists
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Find the Enrollment entry
    enrollment = db.query(Enrollment).filter(Enrollment.student_id == student_id, Enrollment.course_id == course_id).first()
    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")

    # Remove the enrollment
    db.delete(enrollment)
    db.commit()

    return {"message": "Student removed from course successfully"}