```python
# src/service/teacher_service.py

from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.model.teacher import Teacher  # Assuming the Teacher model exists in the specified path

def get_teacher_by_id(db: Session, teacher_id: int):
    """
    Retrieve a teacher by their unique identifier.

    Parameters:
    - db: Session - Database session for querying.
    - teacher_id: int - The unique identifier of the teacher.

    Returns:
    - Teacher - The Teacher object if found.

    Raises:
    - HTTPException: If the teacher with the specified ID is not found (404 error).
    """
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher is None:
        raise HTTPException(status_code=404, detail={"error": {"code": "E002", "message": "Teacher not found."}})
    return teacher
```