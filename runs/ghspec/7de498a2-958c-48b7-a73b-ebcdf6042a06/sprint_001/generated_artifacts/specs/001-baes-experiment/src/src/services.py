```python
from sqlalchemy.orm import Session
from models import Student


def delete_student(student_id: int, db: Session):
    """
    Delete a student from the database by their ID.

    Args:
        student_id (int): The ID of the student to delete.
        db (Session): The SQLAlchemy session object.

    Returns:
        bool: True if the student was deleted, False if not found.
    
    Raises:
        Exception: Raises an exception if the database operation fails.
    """
    # Attempt to find the student by ID
    student = db.query(Student).filter(Student.id == student_id).first()

    if student:
        try:
            db.delete(student)  # Remove the student from the session
            db.commit()         # Commit the transaction
            return True
        except Exception as e:
            db.rollback()  # Rollback the transaction in case of error
            raise Exception(f"Failed to delete student: {str(e)}")  # Raise error with context
    else:
        return False  # Student not found
```