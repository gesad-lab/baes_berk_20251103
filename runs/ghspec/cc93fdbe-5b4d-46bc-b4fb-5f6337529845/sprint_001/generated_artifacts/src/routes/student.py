```python
from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .database import get_session  # Assuming there is a database.py file with the AsyncSession maker
from .models import Student  # Assuming there is a Student model defined in models.py
from .schemas import StudentCreate, StudentResponse  # Assuming appropriate Pydantic schemas are defined

router = APIRouter()

class StudentCreate(BaseModel):
    name: str = Field(..., title="The name of the student", max_length=100)

class StudentResponse(BaseModel):
    id: int
    name: str

@router.post("/students/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
async def create_student(student: StudentCreate, db: AsyncSession = Depends(get_session)):
    """
    Create a new student in the database.

    Args:
        student (StudentCreate): The student data to be created.
        db (AsyncSession): The database session dependency.

    Returns:
        StudentResponse: The created student data.

    Raises:
        HTTPException: If the student creation fails for any reason.
    """
    new_student = Student(name=student.name)
    db.add(new_student)
    
    try:
        await db.commit()
        await db.refresh(new_student)  # Refresh to get the id and other defaults
    except Exception as e:
        await db.rollback()  # Rollback on error
        raise HTTPException(status_code=500, detail="Failed to create student")
    
    return StudentResponse(id=new_student.id, name=new_student.name)


@router.get("/students/{student_id}", response_model=StudentResponse)
async def get_student(student_id: int, db: AsyncSession = Depends(get_session)):
    """
    Retrieve student information by ID.

    Args:
        student_id (int): The ID of the student to be retrieved.
        db (AsyncSession): The database session dependency.

    Returns:
        StudentResponse: The student data retrieved.

    Raises:
        HTTPException: If no student is found or other errors occur.
    """
    query = select(Student).where(Student.id == student_id)
    result = await db.execute(query)
    student = result.scalar_one_or_none()

    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    
    return StudentResponse(id=student.id, name=student.name)
```
