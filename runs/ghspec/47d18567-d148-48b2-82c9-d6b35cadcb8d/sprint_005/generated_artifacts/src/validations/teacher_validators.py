```python
# src/validations/teacher_validators.py

from pydantic import BaseModel, EmailStr, ValidationError
from typing import Dict, Any

class TeacherCreateRequest(BaseModel):
    """Data model for creating a teacher profile."""
    
    name: str  # Teacher's name
    email: EmailStr  # Teacher's email, validated for correct format


def validate_teacher_input(data: Dict[str, Any]) -> None:
    """
    Validate the input data for creating a teacher profile.
    
    Args:
        data (Dict[str, Any]): The input data containing teacher information.

    Raises:
        ValueError: If validation fails, an informative message is raised.
    """
    try:
        TeacherCreateRequest(**data)  # Validate and transform the input data
    except ValidationError as e:
        # Extract error details to provide useful feedback
        error_messages = ', '.join([f"{err['loc'][0]}: {err['msg']}" for err in e.errors()])
        raise ValueError(f"Validation error(s): {error_messages}")


def validate_teacher_retrieval(data: Dict[str, Any]) -> bool:
    """
    Validate the response data for retrieving teacher's information.

    Args:
        data (Dict[str, Any]): The data containing teacher's information.

    Returns:
        bool: True if data is valid, False otherwise.
    """
    required_fields = ['name', 'email']
    
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")
    
    return True  # Valid data structure
```