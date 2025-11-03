```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Teacher, TeacherCreate
from src.services.teacher_service import create_teacher as create_teacher_service

router = APIRouter()

@router.post("/teachers", response_model=Teacher)
async def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    """
    Create a new teacher record.

    - **teacher**: A TeacherCreate object containing the teacher's name and email.
    - **db**: Database session dependency.

    Returns the created Teacher object.
    """
    # Validate that name and email are provided
    if not teacher.name or not teacher.email:
        raise HTTPException(status_code=400, detail="Both name and email fields are required.")

    # Validate the email format
    if "@" not in teacher.email or "." not in teacher.email.split("@")[-1]:
        raise HTTPException(status_code=400, detail="Invalid email format.")

    # Call the service layer to create the teacher
    new_teacher = create_teacher_service(teacher, db)
    
    return new_teacher
```