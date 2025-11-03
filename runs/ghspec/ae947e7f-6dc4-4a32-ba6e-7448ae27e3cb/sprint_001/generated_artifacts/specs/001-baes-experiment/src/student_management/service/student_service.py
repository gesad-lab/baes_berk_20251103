```python
# student_management/service/student_service.py

from typing import Optional
from student_management.model import Student
from student_management.data_access import get_student_by_id as fetch_student_by_id
from student_management.exceptions import StudentNotFoundError

class StudentService:
    """
    Service class for managing student entities.
    Contains methods to create and retrieve student records.
    """
    
    @staticmethod
    def get_student_by_id(student_id: int) -> Student:
        """
        Retrieves a student by ID.

        Parameters:
            student_id (int): The ID of the student to retrieve.

        Returns:
            Student: The student entity if found.

        Raises:
            StudentNotFoundError: If no student is found with the provided ID.
        """
        student: Optional[Student] = fetch_student_by_id(student_id)
        
        if student is None:
            raise StudentNotFoundError(f"Student with ID {student_id} not found.")
        
        return student
```