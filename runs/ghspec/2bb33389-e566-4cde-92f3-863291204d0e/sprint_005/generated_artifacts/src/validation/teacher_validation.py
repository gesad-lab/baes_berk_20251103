```python
# src/validation/teacher_validation.py

from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, Field

class TeacherCreateRequest(BaseModel):
    name: str = Field(..., example="Jane Doe", description="The name of the teacher.")
    email: EmailStr = Field(..., example="jane.doe@example.com", description="The email of the teacher.")

def validate_teacher_creation(data: TeacherCreateRequest) -> TeacherCreateRequest:
    """
    Validate the creation of a teacher. Raises an HTTPException for invalid input.

    Args:
        data (TeacherCreateRequest): The data to validate.

    Returns:
        TeacherCreateRequest: The validated data.

    Raises:
        HTTPException: If validation fails, with 400 status code and a relevant error message.
    """
    if not data.name:
        raise HTTPException(status_code=400, detail={"error": {"code": "E001", "message": "Name field is required."}})
    
    if not data.email:
        raise HTTPException(status_code=400, detail={"error": {"code": "E002", "message": "Email field is required."}})
    
    return data
```