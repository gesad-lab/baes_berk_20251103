```python
# src/validations/student_validators.py

import re
from fastapi import HTTPException, status

EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

def validate_student_request(data: dict) -> None:
    """Validate student creation request data."""
    # Check if the required fields are present
    if "name" not in data or not data["name"].strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": {"code": "E001", "message": "Name field is required."}}
        )
    
    if "email" not in data or not data["email"].strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": {"code": "E002", "message": "Email field is required."}}
        )
    
    # Validate email format
    email = data["email"]
    if not re.match(EMAIL_REGEX, email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": {"code": "E003", "message": "Invalid email format."}}
        )

    # Add any additional validation logic as necessary
```