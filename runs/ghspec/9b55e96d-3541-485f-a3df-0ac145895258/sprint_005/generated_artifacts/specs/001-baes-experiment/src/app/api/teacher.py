from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Teacher
from database import get_db

router = APIRouter()

@router.post("/teachers", response_model=dict)
async def create_teacher(name: str, email: str, db: Session = Depends(get_db)):
    """
    Create a new Teacher entity.

    Args:
        name (str): The name of the teacher, must be a non-empty string.
        email (str): The email of the teacher, must be a valid email format.

    Returns:
        dict: A dictionary containing a success message and the ID of the created teacher.

    Raises:
        HTTPException: 
            - 400 if name or email is missing.
            - 409 if the email already exists in the database.
    """
    # Validate input
    if not name or not email:
        raise HTTPException(status_code=400, detail={"error": {"code": "E001", "message": "Name and email are required fields."}})
    
    # Check for existing teacher with the same email
    existing_teacher = db.query(Teacher).filter(Teacher.email == email).first()
    if existing_teacher:
        raise HTTPException(status_code=409, detail={"error": {"code": "E002", "message": "Email already exists."}})
    
    # Create a new Teacher entity
    teacher = Teacher(name=name, email=email)
    db.add(teacher)
    db.commit()
    db.refresh(teacher)  # Populate the teacher instance with the newly generated ID
    return {"message": "Teacher created successfully", "teacher_id": teacher.id}

@router.get("/teachers/{teacher_id}", response_model=dict)
async def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    """
    Retrieve information for a specific Teacher entity.

    Args:
        teacher_id (int): The ID of the teacher to retrieve.

    Returns:
        dict: A dictionary containing the teacher's ID, name, and email.

    Raises:
        HTTPException: 404 if the teacher does not exist.
    """
    # Fetch the teacher from the database
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail={"error": {"code": "E003", "message": "Teacher not found."}})
    
    return {"id": teacher.id, "name": teacher.name, "email": teacher.email}