```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Teacher
from database import get_db

router = APIRouter()

@router.post("/teachers", response_model=dict)
async def create_teacher(name: str, email: str, db: Session = Depends(get_db)):
    """
    Create a new Teacher entity.

    Parameters:
    - name (str): The name of the teacher.
    - email (str): The email of the teacher.

    Returns:
    - dict: Confirmation message and teacher ID if created successfully.
    
    Raises:
    - HTTPException: If name or email is missing, or if the email is already in use.
    """
    # Validate input fields
    if not name or not email:
        raise HTTPException(status_code=400, detail={"error": {"code": "E001", "message": "Name and email are required fields."}})
    
    # Check for existing email
    existing_teacher = db.query(Teacher).filter(Teacher.email == email).first()
    if existing_teacher:
        raise HTTPException(status_code=409, detail={"error": {"code": "E002", "message": "Email already exists."}})
    
    # Create and persist the new teacher instance
    teacher = Teacher(name=name, email=email)
    db.add(teacher)
    db.commit()

    # Return success response with teacher ID
    return {"message": "Teacher created successfully", "teacher_id": teacher.id}

@router.get("/teachers/{teacher_id}", response_model=dict)
async def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a Teacher's information by ID.

    Parameters:
    - teacher_id (int): The ID of the teacher to retrieve.

    Returns:
    - dict: The teacher's ID, name, and email if found.

    Raises:
    - HTTPException: If the teacher does not exist.
    """
    # Retrieve teacher from database
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail={"error": {"code": "E003", "message": "Teacher not found."}})

    # Return found teacher's information
    return {"id": teacher.id, "name": teacher.name, "email": teacher.email}

# Including API documentation
@router.get("/api/docs/", include_in_schema=False)
async def get_api_docs():
    """
    Redirect to the Swagger UI for API documentation.
    """
    return {"message": "API documentation is available at /docs"}
```