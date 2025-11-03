```python
# src/services/teacher_service.py
from typing import Optional, List
from pydantic import BaseModel, EmailStr, ValidationError
from sqlalchemy.orm import Session
from src.models.teacher import Teacher  # Import the Teacher model
from src.database.db import get_db  # Assuming a function to get the database session

class TeacherCreate(BaseModel):
    name: str
    email: EmailStr

class TeacherService:
    def __init__(self, db: Session):
        self.db = db

    def create_teacher(self, teacher_data: TeacherCreate) -> Teacher:
        """Create a new teacher record in the database."""
        teacher = Teacher(name=teacher_data.name, email=teacher_data.email)
        self.db.add(teacher)
        self.db.commit()
        self.db.refresh(teacher)  # Refresh to get the new teacher ID
        return teacher

    def get_teacher_by_id(self, teacher_id: int) -> Optional[Teacher]:
        """Retrieve a teacher's details by their ID."""
        return self.db.query(Teacher).filter(Teacher.id == teacher_id).first()

# Dependency to provide a database session
def get_teacher_service(db: Session = next(get_db())) -> TeacherService:
    return TeacherService(db)
```