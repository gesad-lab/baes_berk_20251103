```python
from fastapi import HTTPException, status
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from src.models import Student

class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Use Pydantic's built-in validation for email

class StudentUpdate(BaseModel):
    name: str = None
    email: EmailStr = None  # Email field can be optional for updates

class StudentService:
    def create_student(self, db: Session, student_create: StudentCreate):
        """Create a new student with validated email."""
        db_student = Student(name=student_create.name, email=student_create.email)
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student

    def update_student(self, db: Session, student_id: int, student_update: StudentUpdate):
        """Update an existing student by ID with validated email."""
        db_student = db.query(Student).filter(Student.id == student_id).first()
        
        if not db_student:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

        if student_update.email:
            db_student.email = student_update.email  # Email validation happens at the model level

        if student_update.name:
            db_student.name = student_update.name

        db.commit()
        db.refresh(db_student)
        return db_student
    
    def validate_student_email(self, email: str):
        """Ensure the email format is valid (handled by Pydantic)."""
        # If further validation is needed that isn't covered by Pydantic
        # it can be handled here, but Pydantic's EmailStr covers standard validation.


# Ensure the following methods for FastAPI integration are updated accordingly to handle
# request and response processing based on new models.

```