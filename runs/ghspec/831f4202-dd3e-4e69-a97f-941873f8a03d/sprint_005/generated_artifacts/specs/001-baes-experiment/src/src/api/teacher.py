```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List
from src.database import database  # Assuming there is a database module to interact with
from src.models import Teacher  # Importing the Teacher model

router = APIRouter()

class TeacherCreate(BaseModel):
    name: str
    email: EmailStr

class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str

@router.post("/teachers", response_model=TeacherResponse)
async def create_teacher(teacher: TeacherCreate):
    """
    Create a new teacher record.
    
    Args:
        teacher (TeacherCreate): The teacher data to create.

    Returns:
        TeacherResponse: The created teacher with an ID.
    
    Raises:
        HTTPException: If the teacher could not be created.
    """
    # Check if a teacher with the same email already exists
    existing_teacher = await database.fetch_one(
        "SELECT * FROM teachers WHERE email = :email", {"email": teacher.email}
    )
    if existing_teacher:
        raise HTTPException(status_code=400, detail="Email already registered.")

    # Insert the new teacher into the database
    new_teacher = await database.execute(
        "INSERT INTO teachers (name, email) VALUES (:name, :email)", 
        {"name": teacher.name, "email": teacher.email}
    )

    # Fetch and return the created teacher data
    created_teacher = await database.fetch_one(
        "SELECT * FROM teachers WHERE id = :id", {"id": new_teacher}
    )
    
    return TeacherResponse(id=created_teacher["id"], name=created_teacher["name"], email=created_teacher["email"])

@router.get("/teachers", response_model=List[TeacherResponse])
async def get_teachers():
    """
    Retrieve all existing teachers.

    Returns:
        List[TeacherResponse]: A list of existing teachers.
    """
    teachers = await database.fetch_all("SELECT * FROM teachers")
    return [TeacherResponse(id=teacher["id"], name=teacher["name"], email=teacher["email"]) for teacher in teachers]
```