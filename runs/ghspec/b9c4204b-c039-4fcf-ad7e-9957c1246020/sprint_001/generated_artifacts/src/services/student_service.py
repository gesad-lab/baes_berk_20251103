```python
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from typing import List
from models import Student  # Assuming Student model is defined in models.py
from schemas import StudentCreate, StudentResponse  # Assuming Pydantic models are in schemas.py

class StudentService:
    """Service class to handle student-related operations."""
    
    def __init__(self, db: Session):
        """
        Initializes the StudentService with a database session.
        
        Args:
            db (Session): The database session for performing operations.
        """
        self.db = db

    def retrieve_students(self) -> List[StudentResponse]:
        """
        Retrieves all students from the database.

        Returns:
            List[StudentResponse]: A list of student data.
        """
        students = self.db.query(Student).all()  # Retrieve all students
        return [StudentResponse.from_orm(student) for student in students]  # Convert to response format

    def retrieve_student_by_id(self, student_id: int) -> StudentResponse:
        """
        Retrieves a specific student by their ID.

        Args:
            student_id (int): The ID of the student to retrieve.

        Returns:
            StudentResponse: The student data.

        Raises:
            ValueError: If the student does not exist.
        """
        try:
            student = self.db.query(Student).filter(Student.id == student_id).one()  # Retrieve the student
            return StudentResponse.from_orm(student)  # Convert to response format
        except NoResultFound:
            raise ValueError(f"E001: Student with ID {student_id} not found")  # Raise error if not found
```