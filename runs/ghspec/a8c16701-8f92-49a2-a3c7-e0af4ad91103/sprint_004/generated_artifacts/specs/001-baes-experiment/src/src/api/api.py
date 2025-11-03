```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.db import get_db
from src.models import Student, Course  # Ensure Course model is imported
from typing import List

# Create a router instance
router = APIRouter()

@router.get("/students/{id}/courses", response_model=List[Course])
def get_courses_for_student(id: int, db: Session = Depends(get_db)):
    """
    Retrieve all courses associated with a specific student.

    :param id: The ID of the student.
    :param db: Database session dependency.
    :return: A list of courses associated with the student.
    :raises HTTPException: If student is not found or if there are errors accessing the database.
    """
    # Fetch the student from the database
    student = db.query(Student).filter(Student.id == id).first()
    
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Get the courses associated with the student
    courses = student.courses  # Assuming `courses` relationship is properly set in Student model
    
    return courses
```