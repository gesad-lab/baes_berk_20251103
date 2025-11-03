```python
# src/repositories/student_repository.py

from typing import List, Optional
from sqlalchemy.orm import Session
from src.models.student import Student  # Assuming Student model is defined with the necessary fields
from src.schemas.student import StudentCreate, StudentRead  # Assuming these schemas exist for validation and serialization
from sqlalchemy.exc import IntegrityError

class StudentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_student(self, student_data: StudentCreate) -> StudentRead:
        """Create a new student in the database.
        
        Args:
            student_data (StudentCreate): The data for the new student.
        
        Returns:
            StudentRead: The created student.
        
        Raises:
            ValueError: If the email is not valid or missing.
        """
        if not self.is_valid_email(student_data.email):
            raise ValueError("Invalid email format.")
        
        new_student = Student(name=student_data.name, email=student_data.email)
        
        try:
            self.db.add(new_student)
            self.db.commit()
            self.db.refresh(new_student)
            return StudentRead.from_orm(new_student)
        except IntegrityError:
            self.db.rollback()
            raise ValueError("Student with this email already exists.")

    def get_all_students(self) -> List[StudentRead]:
        """Retrieve all students from the database.
        
        Returns:
            List[StudentRead]: A list of students.
        """
        students = self.db.query(Student).all()
        return [StudentRead.from_orm(student) for student in students]

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Validate the email format.
        
        Args:
            email (str): The email to validate.
        
        Returns:
            bool: True if valid, False otherwise.
        """
        import re
        # Simple regex for email validation
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None
```