```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Student
from src.schemas import StudentCreate, StudentUpdate  # Assuming schemas are defined in src/schemas.py
from src.services.student_service import delete_student  # Existing service for handling deletes

router = APIRouter()

@router.delete("/students/{student_id}", status_code=204)
def remove_student(student_id: int, db: Session = Depends(get_db)):
    """Delete a student record by ID and ensure associated email is removed.

    Args:
        student_id (int): The ID of the student to delete.
        db (Session): Database session dependency.

    Raises:
        HTTPException: If the student with the given ID does not exist.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)  # Remove the student record, including email
    db.commit()  # Commit the delete transaction to the database
```

This implementation updates the DELETE endpoint for student records to ensure that when a record is deleted, the associated email field is also removed. It checks if the student exists and raises an appropriate HTTP exception if not. After deletion, it commits the transaction to the database.