```python
from models import Student
from sqlalchemy.orm import Session
from typing import List

class StudentService:
    """Service to manage student operations."""

    def __init__(self, db: Session):
        """Initialize the service with a database session.
        
        Args:
            db: SQLAlchemy database session to interact with the database.
        """
        self.db = db

    def retrieve_students(self) -> List[Student]:
        """Retrieve all students from the database.

        Returns:
            A list of Student objects.

        Raises:
            Exception: If there is an error retrieving students from the database.
        """
        try:
            students = self.db.query(Student).all()  # Fetch all student records
            return students
        except Exception as e:
            # Log the exception (implementation of logging not shown here)
            raise Exception("Error retrieving students from the database.") from e
```