from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.student_service import (
    create_student,
    get_student_by_id,
    get_all_students
)

router = APIRouter()

class StudentCreate(BaseModel):
    """Pydantic model for creating a student."""
    name: str

@router.post("/students", response_model=StudentCreate)
async def add_student(student: StudentCreate):
    """
    Create a new student.

    Args:
        student (StudentCreate): The student information.

    Returns:
        StudentCreate: The created student information.

    Raises:
        HTTPException: If the student could not be created.
    """
    try:
        created_student = await create_student(student.name)
        return created_student
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating student: {str(e)}")

@router.get("/students/{student_id}", response_model=StudentCreate)
async def read_student(student_id: int):
    """
    Retrieve a student by ID.

    Args:
        student_id (int): The ID of the student to retrieve.

    Returns:
        StudentCreate: The student information.

    Raises:
        HTTPException: If the student is not found.
    """
    student = await get_student_by_id(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.get("/students", response_model=list[StudentCreate])
async def list_students():
    """
    Retrieve a list of all students.

    Returns:
        List[StudentCreate]: The list of student information.
    """
    return await get_all_students()

# Make sure to include this router in the main FastAPI application to activate the endpoints.