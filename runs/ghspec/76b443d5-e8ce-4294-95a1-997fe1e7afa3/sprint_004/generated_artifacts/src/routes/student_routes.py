```python
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Student, Course  # Assuming the appropriate models are defined in src/models.py

router = APIRouter()

@router.get("/students/{student_id}/courses")
def get_student_courses(student_id: int, db: Session = next(get_db())):
    """
    Retrieve all courses for a specific student.

    Args:
        student_id (int): The ID of the student to retrieve courses for.
        db (Session): The database session.

    Returns:
        JSON object containing a list of courses the student is enrolled in.
    
    Raises:
        HTTPException: If the student is not found.
    """
    # Fetch the student from the database by ID
    student = db.query(Student).filter(Student.id == student_id).first()
    
    # If student is not found, raise a 404 error
    if not student:
        raise HTTPException(status_code=404, detail={"error": {"code": "E003", "message": "Student not found."}})

    # Retrieve courses associated with the student
    courses = student.courses  # Assuming a many-to-many relationship exists

    # Prepare the response data
    course_list = [{"id": course.id, "name": course.name, "level": course.level} for course in courses]

    return {"courses": course_list}

```