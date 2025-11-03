```python
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from src.models import Teacher  # Assuming Teacher model is defined in this module
from src.database import get_db  # Function to get a database session

router = APIRouter()

@router.delete("/teachers/{teacher_id}")
async def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    """
    Delete a teacher from the system by ID.

    Args:
        teacher_id (int): The ID of the teacher to be deleted.
        db (Session): The database session.

    Raises:
        HTTPException: If the teacher with the given ID does not exist.

    Returns:
        dict: Confirmation message indicating successful deletion.
    """
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found.")
    
    db.delete(teacher)
    db.commit()
    
    return {"message": "Teacher deleted successfully."}
```