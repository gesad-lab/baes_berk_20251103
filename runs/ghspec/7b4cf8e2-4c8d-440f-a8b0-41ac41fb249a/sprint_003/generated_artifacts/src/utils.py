```python
# src/course_service.py

from typing import Optional, Dict
from src.models import Course  # Assuming Course is defined in models
from src.database import get_db_session

def update_course(course_id: int, update_data: Dict[str, str]) -> Optional[Course]:
    """
    Update an existing course with the specified data.

    Parameters:
    - course_id (int): The ID of the course to update.
    - update_data (Dict[str, str]): A dictionary of fields to update, e.g., {'name': 'New Course Name', 'level': 'Advanced'}.

    Returns:
    - Optional[Course]: The updated course object if successful, None if the course does not exist.
    """
    with get_db_session() as session:
        # Fetch the existing course
        course = session.query(Course).filter(Course.id == course_id).first()
        
        # If the course does not exist, return None
        if course is None:
            return None
        
        # Update the course fields with provided data
        for field, value in update_data.items():
            setattr(course, field, value)
        
        # Commit the changes to the database
        session.commit()
        
        return course
```