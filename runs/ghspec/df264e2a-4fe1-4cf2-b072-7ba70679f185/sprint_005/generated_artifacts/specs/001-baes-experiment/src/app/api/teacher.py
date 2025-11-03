"""
Module: app/api/teacher.py
-----------------------------------
This module handles HTTP requests for Teacher operations, specifically:
- POST /teachers: Create a new Teacher entity.
- GET /teachers/{id}: Retrieve details of a specific Teacher by their ID.

Endpoints:
1. POST /teachers
   - Accepts a JSON body containing:
     - `name`: The name of the teacher (string, required).
     - `email`: The email of the teacher (string, required).
   - Returns a JSON response confirming the creation of the teacher entity or an error message if required fields are missing.

2. GET /teachers/{id}
   - Retrieves the details of a Teacher identified by their ID.
   - Returns the Teacher's details (name and email) in JSON format.
   - Responds with a 404 error if the Teacher is not found.

Use Cases:
- Creating a new Teacher allows for better management and organization of educator-related information.
- Retrieving Teacher details provides a way to view and manage specific educators in the system.
"""

from fastapi import APIRouter, HTTPException
from app.schemas.teacher import TeacherCreate, TeacherResponse
from app.services.teacher_service import create_teacher, get_teacher_by_id

router = APIRouter()

@router.post("/teachers", response_model=TeacherResponse)
async def post_teacher(teacher: TeacherCreate):
    """
    Create a new Teacher entity.

    Parameters:
    - teacher (TeacherCreate): A model containing the teacher's name and email.

    Returns:
    - JSON response with the created teacher's details or an error message.
    """
    try:
        new_teacher = await create_teacher(teacher.name, teacher.email)
        return new_teacher
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/teachers/{id}", response_model=TeacherResponse)
async def get_teacher(id: int):
    """
    Retrieve a Teacher's details by their ID.

    Parameters:
    - id (int): The ID of the teacher to retrieve.

    Returns:
    - JSON response containing the teacher's name and email.

    Raises:
    - HTTPException: 404 if the teacher is not found.
    """
    teacher = await get_teacher_by_id(id)
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher
