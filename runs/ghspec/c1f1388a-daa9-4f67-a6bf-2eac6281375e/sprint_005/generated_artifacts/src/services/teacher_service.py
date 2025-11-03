```python
# src/services/teacher_service.py

from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models.teacher import Teacher  # Importing the Teacher model
from src.schemas.teacher import TeacherCreate, TeacherResponse  # Importing Pydantic schemas for validation

class TeacherService:
    """Service class for managing Teacher entities."""

    @staticmethod
    def create_teacher(db: Session, teacher_data: TeacherCreate) -> TeacherResponse:
        """Create a new teacher record in the database.
        
        Args:
            db (Session): The database session.
            teacher_data (TeacherCreate): The data for the new teacher.

        Returns:
            TeacherResponse: The created teacher's details.

        Raises:
            HTTPException: If the teacher's email already exists in the database.
        """
        existing_teacher = db.query(Teacher).filter(Teacher.email == teacher_data.email).first()
        if existing_teacher:
            raise HTTPException(status_code=400, detail="Email already registered.")

        new_teacher = Teacher(**teacher_data.dict())
        db.add(new_teacher)
        db.commit()
        db.refresh(new_teacher)  # Refresh the instance to get the new ID
        
        return TeacherResponse.from_orm(new_teacher)

    @staticmethod
    def get_teacher(db: Session, teacher_id: int) -> TeacherResponse:
        """Retrieve a teacher's details by ID.
        
        Args:
            db (Session): The database session.
            teacher_id (int): The ID of the teacher to retrieve.

        Returns:
            TeacherResponse: The teacher's details.

        Raises:
            HTTPException: If the teacher is not found.
        """
        teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
        if teacher is None:
            raise HTTPException(status_code=404, detail="Teacher not found.")
        
        return TeacherResponse.from_orm(teacher)
```