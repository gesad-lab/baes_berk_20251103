```python
from typing import List, Optional
from sqlalchemy.orm import Session
from .models import Student  # Assuming Student model is defined in models.py
from .schemas import StudentCreate, StudentResponse  # Assuming schemas are defined in schemas.py


class StudentService:
    """Business logic for managing students."""

    def __init__(self, db: Session):
        self.db = db

    def create_student(self, student_data: StudentCreate) -> StudentResponse:
        """Creates a new student in the database.

        Args:
            student_data (StudentCreate): The data for the new student.

        Returns:
            StudentResponse: The created student data.
        
        Raises:
            ValueError: If student name is missing.
        """
        # Validate that a name is provided
        if not student_data.name:
            raise ValueError("Name is required to create a student.")

        # Create a new Student instance
        new_student = Student(name=student_data.name)

        # Add the new student to the session and commit the transaction
        self.db.add(new_student)
        self.db.commit()
        self.db.refresh(new_student)

        # Return the created student response
        return StudentResponse.from_orm(new_student)

    def get_student_by_id(self, student_id: int) -> Optional[StudentResponse]:
        """Retrieves a student from the database by ID.

        Args:
            student_id (int): The ID of the student to retrieve.

        Returns:
            Optional[StudentResponse]: The retrieved student data or None if not found.
        """
        # Query the database for the student based on ID
        student = self.db.query(Student).filter(Student.id == student_id).first()
        if student:
            return StudentResponse.from_orm(student)
        return None

    def get_all_students(self) -> List[StudentResponse]:
        """Retrieves all students from the database.

        Returns:
            List[StudentResponse]: A list of all students.
        """
        # Query all students from the database
        students = self.db.query(Student).all()
        return [StudentResponse.from_orm(student) for student in students]
```