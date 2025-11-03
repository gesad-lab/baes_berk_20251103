```python
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from src.services.student_service import get_students
from src.repository.models import Student

router = APIRouter()

@router.get("/api/v1/students", response_model=List[Student])
async def retrieve_students():
    """
    Retrieve a list of all students, including their email addresses.

    Returns:
        List[Student]: A list of Student objects containing their id, name, and email.
    
    Raises:
        HTTPException: If an error occurs while retrieving students.
    """
    try:
        students = await get_students()  # Fetch all students including email
        return students
    except Exception as e:
        # Log the exception for debugging purposes (assumed logger is set up)
        raise HTTPException(status_code=500, detail="An error occurred while retrieving students")
```