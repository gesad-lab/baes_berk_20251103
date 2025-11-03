```python
from sqlalchemy.orm import Session
from fastapi import HTTPException

from .models import Student
from .validators import validate_student_data

def create_student(db: Session, name: str):
    """
    Creates a new student in the database.

    Args:
        db (Session): Database session object.
        name (str): The name of the student to create.

    Raises:
        HTTPException: If the name is invalid or not provided.
    
    Returns:
        Student: The created student object.
    """

    # Validate student name input
    if not name or not name.strip():
        raise HTTPException(
            status_code=400,
            detail={"code": "E001", "message": "Invalid input: Student name is required."}
        )

    # Create a new Student instance
    new_student = Student(name=name.strip())
    
    # Add the student to the session and commit
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    
    return new_student

def get_students(db: Session):
    """
    Retrieves a list of all students from the database.

    Args:
        db (Session): Database session object.

    Returns:
        List[Student]: A list of student objects.
    """
    return db.query(Student).all()
```