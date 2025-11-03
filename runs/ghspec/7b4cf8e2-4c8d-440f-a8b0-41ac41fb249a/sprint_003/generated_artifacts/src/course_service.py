```python
from fastapi import APIRouter, HTTPException
from typing import Optional
from src.models import Course  # Assuming a Course model exists
from src.database import get_course_by_id, update_course_in_db  # Assuming these functions exist

router = APIRouter()

@router.put("/courses/{id}", response_model=Course)
async def update_course(id: int, name: Optional[str] = None, level: Optional[str] = None):
    """
    Update an existing course's name or level by ID.

    Parameters:
    - id: Unique identifier for the course
    - name: New name for the course (optional)
    - level: New level for the course (optional)

    Returns:
    - Course: The updated Course object
    
    Raises:
    - HTTPException: If the course is not found or if no fields are provided for update.
    """
    # Retrieve the existing course from the database
    existing_course = await get_course_by_id(id)
    
    # If the course does not exist, raise a 404 error
    if not existing_course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    # Update course fields with the provided values
    if name is not None:
        existing_course.name = name
    if level is not None:
        existing_course.level = level
    
    # Save the updated course back to the database
    updated_course = await update_course_in_db(existing_course)
    
    return updated_course  # Return the updated course data
```