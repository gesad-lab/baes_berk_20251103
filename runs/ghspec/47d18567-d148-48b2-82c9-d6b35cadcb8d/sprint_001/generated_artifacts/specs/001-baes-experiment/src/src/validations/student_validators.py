```python
from pydantic import BaseModel, constr
from fastapi import HTTPException

class StudentCreate(BaseModel):
    """
    Data model for creating a new student.
    Validations:
        - name: Required non-empty string
    """
    name: constr(strip_whitespace=True, min_length=1)

def validate_student_creation(student_data: dict) -> StudentCreate:
    """
    Validates student creation data against the StudentCreate model.
    
    Args:
        student_data (dict): Input data for student creation.
    
    Raises:
        HTTPException: If validation fails, an error is raised with the appropriate message.
    
    Returns:
        StudentCreate: Validated student creation data.
    """
    try:
        validated_student = StudentCreate(**student_data)
        return validated_student
    except ValueError as e:
        # Raise HTTP error with a clear message if the validation fails
        raise HTTPException(status_code=400, detail=str(e))
```