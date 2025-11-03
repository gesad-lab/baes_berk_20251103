```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List
import aiosqlite

# Define the request model for creating a teacher
class TeacherCreateRequest(BaseModel):
    """Model for creating a new teacher."""
    name: str
    email: EmailStr  # Ensures the email is in the correct format

class TeacherResponse(BaseModel):
    """Model for representing a teacher's details in responses."""
    id: int
    name: str
    email: str

router = APIRouter()

@router.post("/teachers", response_model=TeacherResponse)
async def create_teacher(teacher: TeacherCreateRequest):
    """Create a new Teacher entity in the database.

    Args:
        teacher (TeacherCreateRequest): Teacher information to create.

    Raises:
        HTTPException: If the email already exists in the database.
        
    Returns:
        TeacherResponse: The created teacher's information.
    """
    async with aiosqlite.connect("database.db") as db:
        # Check for existing email to avoid duplicates
        async with db.execute("SELECT id FROM teacher WHERE email = ?", (teacher.email,)) as cursor:
            existing_teacher = await cursor.fetchone()
            if existing_teacher:
                raise HTTPException(status_code=400, detail="Email already exists.")

        # Insert the new teacher into the database
        cursor = await db.execute("INSERT INTO teacher (name, email) VALUES (?, ?)", 
                                   (teacher.name, teacher.email))
        await db.commit()
        teacher_id = cursor.lastrowid

        return TeacherResponse(id=teacher_id, name=teacher.name, email=teacher.email)

@router.get("/teachers", response_model=List[TeacherResponse])
async def list_teachers():
    """Retrieve a list of all teachers from the database.

    Returns:
        List[TeacherResponse]: A list of all teachers.
    """
    async with aiosqlite.connect("database.db") as db:
        cursor = await db.execute("SELECT id, name, email FROM teacher")
        teachers = await cursor.fetchall()
        return [TeacherResponse(id=row[0], name=row[1], email=row[2]) for row in teachers]
```