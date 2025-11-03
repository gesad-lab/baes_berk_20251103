```python
# src/api.py

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Student, Course, StudentCourses  # Ensure you have the StudentCourses model in models.py
from database import get_db  # Import the function to get the database session
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.post("/students/{student_id}/enroll")
def enroll_student(student_id: int, course_id: int, db: Session = Depends(get_db)):
    """
    Enroll a student in a specific course.

    :param student_id: ID of the student to enroll.
    :param course_id: ID of the course to enroll the student in.
    :param db: Database session dependency.
    :return: Success message.
    """
    # Verify that the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        logger.error(f"Enrollment failed: Student with ID {student_id} does not exist.")
        raise HTTPException(status_code=404, detail="Student not found.")

    # Verify that the course exists
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        logger.error(f"Enrollment failed: Course with ID {course_id} does not exist.")
        raise HTTPException(status_code=404, detail="Course not found.")

    # Create the association in the StudentCourses intermediary table
    enrollment = StudentCourses(student_id=student_id, course_id=course_id)
    
    try:
        db.add(enrollment)
        db.commit()
        logger.info(f"Student {student_id} successfully enrolled in course {course_id}.")
        return {"message": "Enrollment successful."}
    except Exception as e:
        db.rollback()
        logger.error(f"Enrollment failed due to an error: {e}.")
        raise HTTPException(status_code=500, detail="Enrollment failed due to an internal error.")

@app.get("/students/{student_id}/courses")
def get_student_courses(student_id: int, db: Session = Depends(get_db)):
    """
    Retrieve all courses a specific student is enrolled in.

    :param student_id: ID of the student.
    :param db: Database session dependency.
    :return: List of courses the student is enrolled in.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        logger.error(f"Retrieval failed: Student with ID {student_id} does not exist.")
        raise HTTPException(status_code=404, detail="Student not found.")

    courses = db.query(Course).join(StudentCourses).filter(StudentCourses.student_id == student_id).all()

    logger.info(f"Retrieved courses for student {student_id}: {courses}.")
    return {"courses": [{"id": course.id, "name": course.name, "level": course.level} for course in courses]}
```