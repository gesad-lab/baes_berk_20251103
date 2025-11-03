```python
from pydantic import BaseModel, EmailStr, ValidationError
from fastapi import HTTPException, Request
import logging

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format='{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s", "context": "%(name)s"}'
)
logger = logging.getLogger(__name__)

class StudentCreateModel(BaseModel):
    """Model for creating a student with validation."""
    
    name: str
    email: EmailStr

def validate_student_input(request: Request):
    """
    Validate incoming student creation request.

    Parameters:
    request (Request): The incoming request containing student data.

    Raises:
    HTTPException: If validation fails, with appropriate error message.
    """
    try:
        student_data = StudentCreateModel.parse_raw(request.body())
    except ValidationError as e:
        logger.error(f'Validation error: {e}', extra={'context': 'student_validator'})
        raise HTTPException(
            status_code=400,
            detail={
                "error": {
                    "code": "E001",
                    "message": "Email is required or invalid format."
                }
            }
        )
    
    return student_data
```