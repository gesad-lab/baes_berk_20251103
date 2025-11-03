```python
# src/services/student_course.py

from db.database import db_session
from models.student_course import StudentCourse
from models.student import Student
from models.course import Course
from sqlalchemy.exc import NoResultFound

def unenroll_student_from_course(student_id: int, course_id: int) -> dict:
    """
    Unenroll a student from a specified course.
    
    Args:
        student_id (int): The ID of the student to unenroll.
        course_id (int): The ID of the course to unenroll from.
    
    Returns:
        dict: A message confirming the removal or an error.
    """
    # Validate student and course existence
    try:
        student = db_session.query(Student).filter_by(id=student_id).one()
        course = db_session.query(Course).filter_by(id=course_id).one()
    except NoResultFound:
        return {"error": {"code": "E001", "message": "Invalid student or course ID."}}, 404

    # Remove the enrollment from the database
    enrollment = db_session.query(StudentCourse).filter_by(student_id=student.id, course_id=course.id).first()
    
    if enrollment:
        db_session.delete(enrollment)
        db_session.commit()
        return {"message": "Student unenrolled from course successfully."}, 200
    else:
        return {"error": {"code": "E002", "message": "Student is not enrolled in the specified course."}}, 404
```