```python
from sqlalchemy.orm import Session
from models import Student  # Assuming Student ORM model is defined in models.py
from sqlalchemy.exc import NoResultFound

class StudentService:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, student_id: int) -> dict:
        """
        Retrieve a student by their ID.

        Parameters:
            student_id (int): The ID of the student to retrieve.

        Returns:
            dict: A dictionary containing the student's details.

        Raises:
            ValueError: If the student ID is not valid (non-positive).
            NoResultFound: If no student matches the given ID.
        """
        if student_id <= 0:
            raise ValueError("The student ID must be a positive integer.")

        # Attempt to retrieve the student from the database
        student = self.db.query(Student).filter(Student.id == student_id).one_or_none()
        
        if student is None:
            raise NoResultFound(f"No student found with ID: {student_id}")

        # Convert the student object to a dictionary for returning as JSON
        return {
            "id": student.id,
            "name": student.name,
            # Include other fields as necessary
        }
```