from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db_session
from src.models import Student

router = APIRouter()

@router.delete("/students/{id}", response_model=dict)
def delete_student(id: int, db: Session = get_db_session()):
    """
    Delete a Student by ID and return a confirmation response.

    Parameters:
        id (int): The ID of the Student to delete.
        db (Session): The database session.

    Returns:
        dict: A confirmation message indicating successful deletion.
    
    Raises:
        HTTPException: If the Student ID is not found in the database.
    """
    # Attempt to retrieve the student from the database
    student_to_delete = db.query(Student).filter(Student.id == id).first()

    # If no student is found, raise a 404 error
    if not student_to_delete:
        raise HTTPException(status_code=404, detail="Student not found")

    # Delete the student record from the database
    db.delete(student_to_delete)
    db.commit()  # Commit the changes to persist deletion

    return {"message": "Student deleted successfully"}  # Confirmation response