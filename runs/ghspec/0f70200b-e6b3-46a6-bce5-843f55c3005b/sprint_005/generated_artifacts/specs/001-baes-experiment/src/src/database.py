```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from src.database import get_teacher_by_id, create_teacher_in_db

app = FastAPI()

class Teacher(BaseModel):
    name: str
    email: EmailStr

@app.post("/teachers", response_model=Teacher, status_code=201)
async def create_teacher(teacher: Teacher):
    """
    Create a new Teacher entity.
    
    Args:
        teacher (Teacher): The teacher details to create.
    
    Returns:
        Teacher: The created teacher's details.
    """
    # Function to create the teacher in the database
    created_teacher = create_teacher_in_db(teacher)
    return created_teacher

@app.get("/teachers/{id}", response_model=Teacher)
async def get_teacher(id: int):
    """
    Retrieve details of a specific Teacher by their ID.
    
    Args:
        id (int): The ID of the teacher to retrieve.
    
    Raises:
        HTTPException: If the teacher is not found.
    
    Returns:
        Teacher: The details of the retrieved teacher.
    """
    teacher = get_teacher_by_id(id)
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher
```