```python
# src/routes/student_course_routes.py

from fastapi import APIRouter, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.models.student import Student
from src.models.course import Course
from src.schemas.student import StudentResponse
from src.database.database import get_db

router = APIRouter()

@router.get("/students", response_model=List[StudentResponse])
def list_all_students(db: Session = next(get_db())):
    """
    List all students with their associated courses.

    Args:
        db (Session): Database session for querying.

    Returns:
        List[StudentResponse]: An array of student objects each including an array of associated course IDs.
    """
    students = db.query(Student).all()  # Fetch all students
    if not students:
        raise HTTPException(status_code=404, detail="No students found")

    # Create a structured response combining student data with course IDs
    response = []
    for student in students:
        student_data = {
            "id": student.id,
            "name": student.name,
            "course_ids": [course.id for course in student.courses],  # Assuming a 'courses' relationship exists
        }
        response.append(student_data)

    return response
```