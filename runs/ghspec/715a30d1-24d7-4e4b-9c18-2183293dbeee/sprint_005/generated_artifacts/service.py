```python
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models import Teacher  # Assume Teacher model is defined in models.py
from repository import teacher_repository  # Assuming a repository layer exists

def create_teacher(db: Session, name: str, email: str):
    """
    Create a new teacher in the database.
    
    Parameters:
    - db: Database session
    - name: Name of the teacher
    - email: Email of the teacher
    
    Returns:
    - The created teacher object.
    
    Raises:
    - HTTPException: If validation fails or on database error.
    """
    if not name or not email:
        # Raise an error if required fields are missing
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing required fields: 'name' and 'email' must be provided.",
        )

    # You could add additional validation for email format if desired
    try:
        new_teacher = Teacher(name=name, email=email)
        db.add(new_teacher)
        db.commit()
        db.refresh(new_teacher)
        return new_teacher
    except Exception as e:
        # Log the exception (if needed) and raise an HTTPException
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while creating the teacher.",
        )


def get_teacher(db: Session, teacher_id: int):
    """
    Retrieve a teacher from the database by their ID.
    
    Parameters:
    - db: Database session
    - teacher_id: ID of the teacher to retrieve

    Returns:
    - The retrieved teacher object.
    
    Raises:
    - HTTPException: If the teacher is not found.
    """
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Teacher with ID {teacher_id} not found.",
        )
    return teacher
```