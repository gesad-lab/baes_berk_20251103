```python
# src/services/teacher_service.py

from sqlalchemy.orm import Session
from src.models.teacher import Teacher
from src.schemas.teacher_schemas import TeacherCreate, TeacherUpdate
from fastapi import HTTPException

class TeacherService:
    def create_teacher(self, db: Session, teacher_create: TeacherCreate) -> Teacher:
        """Create a new teacher in the database.

        Args:
            db: Database session.
            teacher_create: Data for creating the teacher.

        Returns:
            The created Teacher object.
        """
        new_teacher = Teacher(name=teacher_create.name, email=teacher_create.email)
        db.add(new_teacher)
        db.commit()
        db.refresh(new_teacher)
        return new_teacher

    def get_teacher(self, db: Session, teacher_id: int) -> Teacher:
        """Retrieve a teacher's details by ID.

        Args:
            db: Database session.
            teacher_id: The unique identifier of the teacher.

        Returns:
            The Teacher object if found.

        Raises:
            HTTPException: If the teacher does not exist.
        """
        teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
        if not teacher:
            raise HTTPException(status_code=404, detail="Teacher not found")
        return teacher

    def update_teacher(self, db: Session, teacher_id: int, teacher_update: TeacherUpdate) -> Teacher:
        """Update an existing teacher's name and/or email.

        Args:
            db: Database session.
            teacher_id: The unique identifier of the teacher.
            teacher_update: Updated fields for the teacher.

        Returns:
            The updated Teacher object.

        Raises:
            HTTPException: If the teacher does not exist.
        """
        teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
        if not teacher:
            raise HTTPException(status_code=404, detail="Teacher not found")
        
        if teacher_update.name:
            teacher.name = teacher_update.name
        if teacher_update.email:
            teacher.email = teacher_update.email

        db.commit()
        db.refresh(teacher)
        return teacher

    def delete_teacher(self, db: Session, teacher_id: int) -> dict:
        """Delete a teacher from the database.

        Args:
            db: Database session.
            teacher_id: The unique identifier of the teacher.

        Returns:
            A confirmation message of the deletion.

        Raises:
            HTTPException: If the teacher does not exist.
        """
        teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
        if not teacher:
            raise HTTPException(status_code=404, detail="Teacher not found")

        db.delete(teacher)
        db.commit()
        return {"message": "Teacher deleted successfully"}
```