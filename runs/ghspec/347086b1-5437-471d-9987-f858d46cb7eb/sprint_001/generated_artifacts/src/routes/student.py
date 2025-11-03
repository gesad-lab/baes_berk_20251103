```python
import logging
from fastapi import APIRouter, HTTPException
from src.models.student import Student
from src.database import get_db
from sqlalchemy.orm import Session

# Configure structured logging
logger = logging.getLogger("student_api")
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

router = APIRouter()

@router.post("/students", response_model=Student)
def create_student(student: Student, db: Session = next(get_db())):
    """
    Create a new student record.

    Args:
        student (Student): The student object containing the student name.
        db (Session): Database session for interaction.

    Returns:
        Student: The created student object.

    Raises:
        HTTPException: If the student name is not valid or other errors occur.
    """
    if not student.name:
        logger.error("Validation Error: Student name is empty")
        raise HTTPException(status_code=400, detail="Student name cannot be empty.")

    try:
        db.add(student)
        db.commit()
        db.refresh(student)
        logger.info("Creating student: %s", student.name)  # Structured logging for new student creation
        return student
    except Exception as e:
        logger.error("Error occurred while creating student: %s", str(e))
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to create student.")
```