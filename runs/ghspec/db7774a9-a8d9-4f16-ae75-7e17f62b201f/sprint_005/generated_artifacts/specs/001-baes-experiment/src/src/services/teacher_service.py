```python
# src/services/teacher_service.py

from sqlalchemy.orm import Session
from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, Field
from src.models.teacher import Teacher  # Assuming Teacher model is defined in models
from src.schemas.teacher import TeacherCreate, TeacherResponse  # Assuming these schemas are created
from typing import List

class TeacherService:
    """Service to handle business logic related to teachers."""

    @staticmethod
    def create_teacher(db: Session, teacher: TeacherCreate) -> TeacherResponse:
        """Create a new teacher in the database and return the created teacher's data.
        
        Args:
            db: Database session.
            teacher: TeacherCreate schema with name and email fields.

        Returns:
            TeacherResponse: The created teacher object with an `id` field.
        """
        # Check if the email already exists
        existing_teacher = db.query(Teacher).filter(Teacher.email == teacher.email).first()
        if existing_teacher:
            raise HTTPException(status_code=400, detail="Email already in use.")

        # Create a new Teacher object
        new_teacher = Teacher(name=teacher.name, email=teacher.email)
        
        # Add to the session and commit to the database
        db.add(new_teacher)
        db.commit()
        db.refresh(new_teacher)
        
        return TeacherResponse(id=new_teacher.id, name=new_teacher.name, email=new_teacher.email)

    @staticmethod
    def get_teacher(db: Session, teacher_id: int) -> TeacherResponse:
        """Retrieve a teacher by ID.

        Args:
            db: Database session.
            teacher_id: ID of the teacher to retrieve.

        Returns:
            TeacherResponse: The requested teacher object.
        
        Raises:
            HTTPException: If the teacher with the specified ID does not exist.
        """
        teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
        if not teacher:
            raise HTTPException(status_code=404, detail="Teacher not found.")
        return TeacherResponse(id=teacher.id, name=teacher.name, email=teacher.email)

    @staticmethod
    def list_teachers(db: Session) -> List[TeacherResponse]:
        """List all teachers from the database.

        Args:
            db: Database session.

        Returns:
            List[TeacherResponse]: List of teacher objects.
        """
        teachers = db.query(Teacher).all()
        return [TeacherResponse(id=teacher.id, name=teacher.name, email=teacher.email) for teacher in teachers]
```