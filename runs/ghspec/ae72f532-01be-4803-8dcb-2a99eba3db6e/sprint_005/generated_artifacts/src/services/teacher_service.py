```python
# src/services/teacher_service.py

from typing import List, Dict, Any
from fastapi import HTTPException
from src.models.teacher import Teacher
from src.dal.teacher_dal import TeacherDAL

class TeacherService:
    """Service class to handle operations related to Teacher records."""

    def __init__(self):
        self.teacher_dal = TeacherDAL()

    def add_teacher(self, name: str, email: str) -> Dict[str, Any]:
        """Adds a new teacher record.

        Args:
            name (str): The name of the teacher.
            email (str): The email address of the teacher.

        Returns:
            Dict[str, Any]: Confirmation of the record creation and newly created Teacher data.

        Raises:
            HTTPException: If name or email is missing.
        """
        if not name or not email:
            raise HTTPException(status_code=400, detail={"error": {"code": "E001", "message": "Name and email must be provided."}})
        
        new_teacher = Teacher(name=name, email=email)
        created_teacher = self.teacher_dal.create_teacher(new_teacher)
        return {
            "message": "Teacher record created successfully.",
            "teacher": created_teacher
        }

    def get_teacher(self, teacher_id: int) -> Dict[str, Any]:
        """Retrieves a teacher's information by ID.

        Args:
            teacher_id (int): The ID of the teacher to retrieve.

        Returns:
            Dict[str, Any]: The details of the teacher.

        Raises:
            HTTPException: If the teacher is not found.
        """
        teacher = self.teacher_dal.get_teacher_by_id(teacher_id)
        if not teacher:
            raise HTTPException(status_code=404, detail={"error": {"code": "E002", "message": "Teacher not found."}})
        
        return {
            "id": teacher.id,
            "name": teacher.name,
            "email": teacher.email
        }

    def delete_teacher(self, teacher_id: int) -> Dict[str, Any]:
        """Deletes a teacher record by ID.

        Args:
            teacher_id (int): The ID of the teacher to delete.

        Returns:
            Dict[str, Any]: Confirmation of the deletion.

        Raises:
            HTTPException: If the teacher is not found.
        """
        deleted = self.teacher_dal.delete_teacher(teacher_id)
        if not deleted:
            raise HTTPException(status_code=404, detail={"error": {"code": "E003", "message": "Teacher not found to delete."}})

        return {"message": "Teacher record deleted successfully."}
```