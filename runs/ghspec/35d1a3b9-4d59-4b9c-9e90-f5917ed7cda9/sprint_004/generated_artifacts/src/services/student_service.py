```python
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from src.repository import get_student_courses  # Import the function to retrieve student courses
from src.models import Course  # Assuming Course model exists in models

router = APIRouter()

@router.get("/students/{student_id}/courses", response_model=List[Course])
async def retrieve_student_courses(student_id: int):
    """
    Retrieve all courses associated with a specific student.

    Args:
    - student_id (int): The ID of the student whose courses are to be retrieved.

    Returns:
    - List[Course]: A list of courses the student is enrolled in.

    Raises:
    - HTTPException: If the student has no courses or an invalid student ID is provided.
    """
    courses = await get_student_courses(student_id)
    if courses is None:
        raise HTTPException(status_code=404, detail="No courses found for this student.")

    return courses
```