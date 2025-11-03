```python
from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from src.models import Teacher  # Assuming Teacher model is defined in src/models
from src.database import get_db  # Assuming get_db is a dependency for getting a database session

router = APIRouter()

@router.delete("/teachers/{teacher_id}", response_description="Delete a teacher", status_code=status.HTTP_204_NO_CONTENT)
def delete_teacher(teacher_id: int, db: Session = next(get_db())):
    """
    Delete a teacher by ID.

    Args:
        teacher_id (int): The ID of the teacher to delete.
        db (Session): The database session.

    Raises:
        HTTPException: If the teacher is not found.

    Returns:
        None: Successful deletion returns a 204 status.
    """
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    
    if not teacher:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"error": {"code": "E004", "message": "Teacher not found"}})
    
    db.delete(teacher)
    db.commit()
```