from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from src.models.student import Student
from src.database.database import get_db

router = APIRouter()

@router.delete("/students/{student_id}", status_code=204)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    """
    Delete a student by ID.

    Args:
    - student_id (int): The ID of the student to delete.
    - db (Session): Database session for accessing the student records.

    Returns:
    - HTTP status code 204 if deletion is successful.
    - Raises a 404 error if the student does not exist.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    # Delete the student from the database
    db.delete(student)
    db.commit()  # Commit the changes to the database

    return None  # Implicitly returns nothing for 204 status