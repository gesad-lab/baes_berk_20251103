```python
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException

from src.models import Student
from src.schemas import StudentCreate  # Assuming you have a schema for request validation

class StudentService:
    @staticmethod
    def create_student(db: Session, student_create: StudentCreate) -> Student:
        """Create a new student with the provided name and email.

        Args:
            db (Session): The database session.
            student_create (StudentCreate): The student data input including name and email.

        Returns:
            Student: The created student instance.
        
        Raises:
            HTTPException: If the email is missing or invalid.
        """
        if not student_create.email:
            raise HTTPException(
                status_code=400,
                detail={"error": {"code": "E001", "message": "Email field is required."}}
            )
        
        new_student = Student(name=student_create.name, email=student_create.email)  
        
        # Add the new student to the session and commit to the database
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        
        return new_student

    @staticmethod
    def get_student(db: Session, student_id: int) -> Optional[Student]:
        """Retrieve a student by their ID.

        Args:
            db (Session): The database session.
            student_id (int): The unique identifier for the student.

        Returns:
            Optional[Student]: The student instance if found, otherwise None.
        """
        return db.query(Student).filter(Student.id == student_id).first()
```