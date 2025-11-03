```python
from fastapi import APIRouter, HTTPException, status
from src.services.student_service import remove_course_from_student
from pydantic import BaseModel
from typing import List

router = APIRouter()

class CourseRemovalResponse(BaseModel):
    message: str

@router.delete("/students/{student_id}/courses/{course_id}", response_model=CourseRemovalResponse, status_code=status.HTTP_204_NO_CONTENT)
async def delete_course_from_student(student_id: int, course_id: int):
    """
    Remove a specific Course from a Student's record.
    
    Parameters:
    - student_id: The ID of the student from whom the course will be removed.
    - course_id: The ID of the course to be removed from the student's record.
    
    Returns:
    A JSON object confirming the course has been removed.
    
    Raises:
    HTTPException: If the student or course is not found, or the removal fails.
    """
    try:
        # Call the service layer to handle the course removal logic
        await remove_course_from_student(student_id, course_id)
    except ValueError as e:  # Catch a specific exception related to value errors
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:  # Log unexpected exceptions for debugging
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occurred while removing the course.")
    
    # On successful removal, return a 204 status code with no content
    return {"message": "Course removed successfully."}  # Note: The response content will not be sent with 204 status code.
```