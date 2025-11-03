```python
# src/validation/validator.py

from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import Student  # Assuming Student model is in a models module

def validate_student_exists(student_id: int, db: Session):
    """
    Validate that the student with the specified ID exists in the database.

    Parameters:
    - student_id: ID of the student to check.
    - db: The database session.

    Raises:
    - HTTPException: If the student does not exist.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail={
            "error": {
                "code": "E002",
                "message": "Student not found."
            }
        })
    
def delete_student(student_id: int, db: Session):
    """
    Delete a student from the database by ID.

    Parameters:
    - student_id: The ID of the student to delete.
    - db: The database session.
    
    Returns:
    - message: Confirmation message upon successful deletion.
    """
    # Validate that the student exists before attempting deletion
    validate_student_exists(student_id, db)
    
    db.query(Student).filter(Student.id == student_id).delete()
    db.commit()  # Commit the transaction to persist the changes
    return {"message": "Student deleted successfully."}
```