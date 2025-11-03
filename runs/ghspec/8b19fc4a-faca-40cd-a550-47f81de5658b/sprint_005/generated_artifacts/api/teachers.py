```python
# api/teachers.py

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from models.teacher import Teacher
from db import get_db  # Assumed import for the database session
from api.errors import CourseErrors  # Assuming we will use similar error codes

router = APIRouter()

@router.get('/teachers/{teacher_id}')
async def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    """Retrieve details for a specific Teacher by ID.
    
    Args:
        teacher_id (int): The ID of the Teacher to retrieve.
        db (Session): The database session to use.
        
    Returns:
        dict: A dictionary containing the Teacher's details.
        
    Raises:
        HTTPException: If the Teacher does not exist.
    """
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher is None:
        raise HTTPException(status_code=404, detail={"error": {"code": "E404", "message": "Teacher not found."}})

    return {"id": teacher.id, "name": teacher.name, "email": teacher.email}
```