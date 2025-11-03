```python
# File: src/api/dependencies.py

from fastapi import Depends, HTTPException, status
from pydantic import BaseModel, EmailStr

# Define a schema for Student creation and updates
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Use Pydantic's EmailStr for email validation

class StudentUpdate(BaseModel):
    email: EmailStr  # Use Pydantic's EmailStr for email validation

# Dependency for email validation
async def validate_student_email(email: str):
    if not email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="E001: Email is a required field."
        )

# Assuming you have routes defined somewhere that need to validate email
async def create_student(student: StudentCreate):
    # Here you would typically call the service to create the student
    await validate_student_email(student.email)
    # Logic to create student in the database goes here...

async def update_student(student_id: int, student: StudentUpdate):
    # Validate email before updating the student
    await validate_student_email(student.email)
    # Logic to update the student's email in the database goes here...
```