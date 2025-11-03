```python
# src/api/teachers.py

from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel, EmailStr, constr
from typing import List
import re

router = APIRouter()

# Define a Pydantic model for Teacher input validation
class Teacher(BaseModel):
    name: constr(min_length=1)  # Name must be at least 1 character
    email: EmailStr  # Validated email format

# In-memory storage (placeholder for database interaction)
teachers_db = []

@router.post("/teachers", response_model=Teacher)
async def create_teacher(teacher: Teacher):
    """
    Create a new teacher entry in the database.

    Validates the incoming teacher's name and email before saving to the database.

    Args:
        teacher (Teacher): The teacher details to be created.

    Raises:
        HTTPException: If the email is already registered or validation fails.
    
    Returns:
        Teacher: The created teacher with name and email.
    """
    # Check for duplicate emails in the database (not thread-safe)
    for existing_teacher in teachers_db:
        if existing_teacher.email == teacher.email:
            raise HTTPException(status_code=400, detail="Email already registered.")
    
    # Add the new teacher to the in-memory database
    teachers_db.append(teacher)
    
    return teacher  # Return the created teacher entry as a response

@router.get("/teachers", response_model=List[Teacher])
async def list_teachers():
    """Retrieve a list of all teachers."""
    return teachers_db
```