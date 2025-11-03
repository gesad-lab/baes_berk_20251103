```python
# app/services/teacher_service.py

from typing import Optional, Dict, Any
from app.models.teacher import Teacher  # Assuming Teacher model exists
from app.database import db  # Assuming there is a db session imported

class TeacherService:
    """Service to handle operations related to teachers."""
    
    @staticmethod
    def get_teacher_by_id(teacher_id: int) -> Optional[Dict[str, Any]]:
        """Retrieve a teacher's details by their ID.

        Args:
            teacher_id (int): The ID of the teacher to retrieve.

        Returns:
            Optional[Dict[str, Any]]: A dictionary containing the teacher's details
            (name and email), or None if the teacher is not found.
        """
        # Fetch the teacher from the database
        teacher = db.session.query(Teacher).filter(Teacher.id == teacher_id).first()
        
        if not teacher:
            return None
        
        # Return the teacher's details in a dictionary
        return {
            "id": teacher.id,
            "name": teacher.name,
            "email": teacher.email
        }

    # Other methods related to teacher operations can be added here
```
