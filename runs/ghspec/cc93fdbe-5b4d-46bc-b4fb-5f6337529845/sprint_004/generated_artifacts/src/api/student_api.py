```python
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from models import Student, Course, StudentCourse  # Assuming these models are defined in models.py
from database import get_db  # Assuming get_db is a dependency for database session

router = APIRouter()

@router.get("/students/{student_id}/courses")
def get_student_courses(student_id: int, db: Session = next(get_db())):
    """
    Retrieve a list of courses for a specific student.

    Args:
        student_id (int): The ID of the student.

    Returns:
        List[Dict]: A JSON array containing details of the courses the student is enrolled in.
    
    Raises:
        HTTPException: If the student is not found, a 404 error is raised.
    """
    # Verify if the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(
            status_code=404,
            detail={"error": {"code": "E004", "message": "Student not found."}}
        )
    
    # Retrieve courses associated with the student
    courses = db.query(Course).join(StudentCourse).filter(StudentCourse.student_id == student.id).all()
    
    # Format courses into a response-friendly structure
    course_list = [{"id": course.id, "name": course.name, "level": course.level} for course in courses]
    
    return course_list
```