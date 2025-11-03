```python
import json
from typing import Dict, Any

class StudentService:
    def __init__(self, database):
        self.database = database

    def create_student(self, name: str) -> Dict[str, Any]:
        """Create a new student record and return it or raise an error."""
        if not name:
            return self._create_error_response("E001", "Name is required for creating a student.")
        
        # Assume `self.database.save_student` saves the student and returns the created student details
        student = self.database.save_student(name)
        return {"student": student}

    def get_student(self, student_id: int) -> Dict[str, Any]:
        """Retrieve a student record by ID or return an error if not found."""
        student = self.database.get_student_by_id(student_id)
        if student is None:
            return self._create_error_response("E002", f"Student with ID {student_id} not found.")
        
        return {"student": student}

    def _create_error_response(self, code: str, message: str) -> Dict[str, Any]:
        """Format an error response in JSON structure."""
        return {
            "error": {
                "code": code,
                "message": message
            }
        }
```
