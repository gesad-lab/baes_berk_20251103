from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.student import Student
from db.database import get_db
from schemas.student_schemas import StudentEmailUpdate, StudentResponse
from services.student_service import get_student_by_id, update_student_email

router = APIRouter()


@router.put("/students/{id}/email", response_model=StudentResponse)
def update_email(id: int, email_update: StudentEmailUpdate, db: Session = Depends(get_db)):
    """
    Update a student's email by ID.

    Args:
        id (int): The ID of the student whose email is to be updated.
        email_update (StudentEmailUpdate): The new email to be set.
        db (Session): The database session.

    Returns:
        StudentResponse: The updated student details if successful.

    Raises:
        HTTPException: 404 if the student is not found.
    """
    student = get_student_by_id(student_id=id, db=db)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Update the student's email
    student.email = email_update.email
    db.add(student)
    db.commit()
    db.refresh(student)

    return student