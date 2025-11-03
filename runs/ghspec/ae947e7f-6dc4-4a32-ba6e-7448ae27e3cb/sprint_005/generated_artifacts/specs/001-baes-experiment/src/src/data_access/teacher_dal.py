```python
# src/data_access/teacher_dal.py

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import Teacher  # Assuming Teacher is defined in the models module
from fastapi import HTTPException

class TeacherDAL:
    """Data Access Layer for Teacher entity."""

    def __init__(self, db: Session):
        self.db = db

    def create_teacher(self, name: str, email: str) -> Teacher:
        """Creates a new teacher and adds it to the database.

        Args:
            name (str): The name of the teacher.
            email (str): The email of the teacher.

        Returns:
            Teacher: The created Teacher object.

        Raises:
            HTTPException: If the input data is invalid or the email already exists.
        """
        if not name or not email:
            raise HTTPException(
                status_code=400,
                detail={"code": "E001", "message": "Name and email fields are required."}
            )

        new_teacher = Teacher(name=name, email=email)

        try:
            self.db.add(new_teacher)
            self.db.commit()
            self.db.refresh(new_teacher)
            return new_teacher
        except IntegrityError:
            self.db.rollback()
            raise HTTPException(
                status_code=400,
                detail={"code": "E002", "message": "Email already in use."}
            )

    def get_teacher_by_id(self, teacher_id: int) -> Teacher:
        """Retrieves a teacher by their ID.

        Args:
            teacher_id (int): The ID of the teacher to retrieve.

        Returns:
            Teacher: The Teacher object corresponding to the ID.

        Raises:
            HTTPException: If no teacher is found with the provided ID.
        """
        teacher = self.db.query(Teacher).filter(Teacher.id == teacher_id).first()
        if not teacher:
            raise HTTPException(
                status_code=404,
                detail={"code": "E003", "message": "Teacher not found."}
            )
        return teacher
```