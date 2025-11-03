```python
# student_management/src/services/student_service.py

from sqlalchemy.orm import Session
from models.student import Student
from pydantic import BaseModel, EmailStr, validator
from typing import List, Optional

class StudentCreateRequest(BaseModel):
    name: str
    email: EmailStr

    @validator('name')
    def validate_name(cls, value):
        if len(value.strip()) == 0:
            raise ValueError("Name must not be empty")
        return value

class StudentService:
    def __init__(self, db: Session):
        self.db = db

    def create_student(self, student_data: StudentCreateRequest) -> Student:
        self.check_email_uniqueness(student_data.email)
        
        # Create a new Student object
        new_student = Student(name=student_data.name, email=student_data.email)
        self.db.add(new_student)
        self.db.commit()
        self.db.refresh(new_student)
        
        return new_student

    def check_email_uniqueness(self, email: str) -> None:
        """ Check if the email already exists in the database. """
        existing_student = self.db.query(Student).filter(Student.email == email).first()
        if existing_student:
            raise ValueError("Email already registered")

    def get_student_by_email(self, email: str) -> Optional[Student]:
        """ Retrieve a student by their email. """
        return self.db.query(Student).filter(Student.email == email).first()

    def list_students(self) -> List[Student]:
        """ Return a list of all students in the database. """
        return self.db.query(Student).all()

# Note: This file assumes that SQLAlchemy is set up properly with the database,
# and the Student model has already been defined with the necessary fields in models.student.
```