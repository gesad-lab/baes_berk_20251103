```python
# File: src/api/enrollment_api.py

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from models.student import Student
from models.course import Course
from repositories.student_courses_repository import StudentCoursesRepository
from database import get_db

router = APIRouter()

@router.get("/students/{student_id}/courses")
def get_student_courses(student_id: int, db: Session = next(get_db())):
    """
    Retrieve all courses associated with a specific student by their ID.

    Args:
        student_id (int): The ID of the student whose courses are being retrieved.
        db (Session): The database session to use for the query.

    Returns:
        A dictionary containing course IDs and names if the student exists, 
        otherwise raises an HTTP 404 error.
    """
    student_repo = StudentCoursesRepository()
    
    # Validate if the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Retrieve courses for the student
    courses = student_repo.get_courses_by_student(student_id)
    
    # Format the response
    return {"student_id": student_id, "courses": [{"course_id": course.id, "name": course.name} for course in courses]}
```