```python
# src/validations/course_validators.py

from fastapi import HTTPException
from src.db.models import Course
from typing import List

def validate_course_ids(course_ids: List[int]) -> None:
    """
    Validate the provided course IDs to ensure they exist in the database.

    Args:
        course_ids (List[int]): A list of course IDs to validate.

    Raises:
        HTTPException: If any course ID is invalid, a 400 Bad Request error is raised
                       with a detailed message indicating the failure.
    """
    # Fetch existing course IDs from the database
    existing_course_ids = {course.id for course in Course.query.all()}

    # Check for any invalid course IDs
    invalid_ids = [course_id for course_id in course_ids if course_id not in existing_course_ids]
    
    if invalid_ids:
        # Create a clear error message for invalid course IDs
        error_message = f"Invalid course IDs: {', '.join(map(str, invalid_ids))}. Ensure they exist."
        raise HTTPException(status_code=400, detail={"error": {"code": "E001", "message": error_message}})
```
