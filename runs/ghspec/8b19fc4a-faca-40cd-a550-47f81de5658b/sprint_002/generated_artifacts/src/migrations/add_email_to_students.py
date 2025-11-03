```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.exc import IntegrityError
from fastapi import FastAPI, HTTPException, Field
from pydantic import BaseModel, EmailStr
from database import Base  # Assuming a file named database.py for SQLAlchemy setup
from sqlalchemy.orm import Session

class Student(Base):
    """Model representing a student in the system."""
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New email field added

    def __repr__(self):
        """Provide a string representation of the student object."""
        return f"<Student(id={self.id}, name='{self.name}', email='{self.email}')>"

class StudentCreate(BaseModel):
    """Schema for creating a new student."""
    name: str = Field(..., title="The name of the student")
    email: EmailStr = Field(..., title="The email address of the student")  # Email validation

# FastAPI instance
app = FastAPI()

@app.post("/students", response_model=StudentCreate)
async def create_student(student: StudentCreate, db: Session):
    """Create a new student in the database with validation checks for email."""
    new_student = Student(name=student.name, email=student.email)

    try:
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
    except IntegrityError:
        db.rollback()  # Roll back the session on error
        raise HTTPException(
            status_code=400,
            detail={"code": "E001", "message": "Email already exists", "details": {}}
        )

    return new_student
```