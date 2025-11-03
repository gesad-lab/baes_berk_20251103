```python
from typing import Any, Dict
from fastapi import HTTPException, status
from models import Course

def validate_course_fields(course_data: Dict[str, Any]) -> None:
    """Validates the course fields to ensure they meet the required criteria.

    Args:
        course_data (Dict[str, Any]): Dictionary containing course information.

    Raises:
        HTTPException: If validation fails, an HTTPException is raised with details.
    """
    name = course_data.get("name")
    level = course_data.get("level")

    # Check if the course name is provided
    if not name or not isinstance(name, str) or not name.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": {"code": "E001", "message": "Invalid course name: must be a non-empty string."}}
        )

    # Check if the course level is provided
    if not level or not isinstance(level, str) or not level.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": {"code": "E002", "message": "Invalid course level: must be a non-empty string."}}
        )
```