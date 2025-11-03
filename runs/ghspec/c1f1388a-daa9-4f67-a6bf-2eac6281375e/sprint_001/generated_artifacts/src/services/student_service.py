```python
from sqlalchemy.orm import Session
from typing import List
from src.models.student import Student
from src.schemas.student import StudentOut
from src.db.database import get_db

def get_all_students(db: Session) -> List[StudentOut]:
    """
    Retrieve all students from the database.

    Args:
        db (Session): The database session to use for the query.

    Returns:
        List[StudentOut]: A list of StudentOut schemas representing all students.
    """
    try:
        # Query the database for all Student records
        students = db.query(Student).all()
        # Convert ORM model list to schema list
        return [StudentOut(id=student.id, name=student.name) for student in students]
    except Exception as e:
        # Log error and raise exception for handling elsewhere
        # Ideally, a logging mechanism should be in place.
        print(f"Error retrieving students: {str(e)}")  # Replace with proper logging
        raise
```