```python
from models import Student
from sqlalchemy.orm import Session
from fastapi import HTTPException

def create_student(session: Session, name: str):
    """Creates a new student in the database.

    Args:
        session (Session): The database session.
        name (str): The name of the student to be created.

    Returns:
        Student: The created student object.

    Raises:
        HTTPException: If the name is empty or not provided (400 Bad Request).
    """
    if not name:
        # Raise an exception if the name is not provided
        raise HTTPException(status_code=400, detail="E001: Missing required field 'name'.")

    student = Student(name=name)
    session.add(student)
    session.commit()
    session.refresh(student)
    return student

def get_students(session: Session):
    """Retrieves all students from the database.

    Args:
        session (Session): The database session.

    Returns:
        List[Student]: A list of all student objects.
    """
    return session.query(Student).all()
```