from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from models import Student  # Assuming this is where the Student model is defined
from services import get_db  # Assuming this is a function to get the database session

router = APIRouter()

@router.delete("/students/{student_id}", response_model=dict)
def delete_student(student_id: int, db: Session = get_db()):
    """
    Delete a student by ID.

    Parameters:
    - student_id: The ID of the student to delete.
    - db: The database session (injected via dependency).

    Returns:
    - A confirmation message if deletion is successful.
    - An error message if the student is not found.
    """
    # Attempt to retrieve the student by ID
    student = db.query(Student).filter(Student.id == student_id).first()
    
    if student is None:
        # Student not found, raise HTTP 404 error
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Proceed to delete the student
    db.delete(student)
    db.commit()
    
    # Return confirmation message
    return {"message": "Student deleted successfully"}