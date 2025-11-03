```python
# src/services/teacher_service.py

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from src.repository import Teacher

# Schema for creating and retrieving a teacher
class TeacherCreate(BaseModel):
    name: str = Field(..., description="The name of the teacher")
    email: EmailStr = Field(..., description="The email of the teacher, must be unique")

class TeacherResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

async def create_teacher(teacher_data: TeacherCreate, db: AsyncSession) -> TeacherResponse:
    # Check for existing teacher with the same email
    existing_teacher = await db.execute(
        "SELECT * FROM teachers WHERE email = :email",
        {"email": teacher_data.email}
    )
    if existing_teacher.scalars().first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered."
        )
    
    # Create the new teacher
    new_teacher = Teacher(name=teacher_data.name, email=teacher_data.email)
    db.add(new_teacher)
    await db.commit()
    await db.refresh(new_teacher)  # Refresh to get the ID and other defaults

    return TeacherResponse(id=new_teacher.id, name=new_teacher.name, email=new_teacher.email)

async def get_teacher(teacher_id: int, db: AsyncSession) -> TeacherResponse:
    # Retrieve the teacher by ID
    teacher = await db.execute(
        "SELECT * FROM teachers WHERE id = :id",
        {"id": teacher_id}
    )
    teacher_instance = teacher.scalars().first()
    
    if not teacher_instance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Teacher not found."
        )

    return TeacherResponse(id=teacher_instance.id, name=teacher_instance.name, email=teacher_instance.email)
```