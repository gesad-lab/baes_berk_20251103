```python
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from src.database import get_db
from src.model.teacher import Teacher as TeacherModel  # Assuming a Teacher model exists in your project
from src.service.teacher_service import create_teacher, get_teacher_by_id  # Assuming these service functions exist

router = APIRouter()

class TeacherCreate(BaseModel):
    name: str
    email: EmailStr

@router.post("/teachers")
async def create_teacher_endpoint(
    teacher: TeacherCreate, db: Session = Depends(get_db)
):
    """
    Create a new teacher entity.

    - **teacher**: TeacherCreate object that includes name and email.
    """
    # Check for existing teacher with the same email before creation
    existing_teacher = db.query(TeacherModel).filter_by(email=teacher.email).first()
    if existing_teacher:
        raise HTTPException(
            status_code=400,
            detail={"error": {"code": "E002", "message": "Email already exists."}}
        )

    # Create the new teacher
    try:
        create_teacher(teacher.name, teacher.email, db)
        return {"message": "Teacher created successfully."}
    except Exception as e:
        # Log the error and return a server error response
        print(f"Error while creating teacher: {e}")  # Replace with proper logging in production
        raise HTTPException(
            status_code=500,
            detail={"error": {"code": "E003", "message": "Internal server error during teacher creation."}}
        )

@router.get("/teachers/{teacher_id}")
async def get_teacher_endpoint(teacher_id: int, db: Session = Depends(get_db)):
    """
    Retrieve details of an existing teacher by ID.

    - **teacher_id**: ID of the teacher to retrieve.
    """
    teacher = get_teacher_by_id(teacher_id, db)
    if not teacher:
        raise HTTPException(
            status_code=404,
            detail={"error": {"code": "E004", "message": "Teacher not found."}}
        )
    return teacher
```