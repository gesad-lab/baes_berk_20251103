```python
# File: src/api/teacher.py

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import List
from src.database import database, Teacher  # Assuming Teacher model is defined in database.py

router = APIRouter()

class TeacherCreate(BaseModel):
    name: str
    email: EmailStr

class TeacherOut(BaseModel):
    id: int
    name: str
    email: str

@router.post("/teachers", response_model=TeacherOut, status_code=status.HTTP_201_CREATED)
async def create_teacher(teacher: TeacherCreate):
    # Check if the email already exists
    existing_teacher = await database.fetch_one("SELECT * FROM teachers WHERE email = :email", values={"email": teacher.email})
    if existing_teacher:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered.")
    
    # Insert new teacher into the database
    query = "INSERT INTO teachers (name, email) VALUES (:name, :email)"
    await database.execute(query, values={"name": teacher.name, "email": teacher.email})
    
    # Fetch the newly created teacher to return
    new_teacher = await database.fetch_one("SELECT * FROM teachers WHERE email = :email", values={"email": teacher.email})
    
    return TeacherOut(**new_teacher)

@router.get("/teachers", response_model=List[TeacherOut])
async def get_teachers():
    # Retrieve all teachers from the database
    query = "SELECT * FROM teachers"
    teachers = await database.fetch_all(query)
    
    return [TeacherOut(**teacher) for teacher in teachers]
```

This implementation introduces the necessary GET `/teachers` endpoint, along with the functionality to create a new `Teacher` entity while enforcing email validation and uniqueness, following the prescribed specifications.