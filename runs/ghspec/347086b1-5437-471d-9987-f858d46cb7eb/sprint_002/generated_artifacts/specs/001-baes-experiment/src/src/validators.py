```python
# src/validators.py

import re
from typing import Dict, Any

EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def validate_student_input(data: Dict[str, Any]) -> None:
    """
    Validate the input data for creating a student.

    Parameters:
    - data (Dict[str, Any]): The input data containing student details.

    Raises:
    - ValueError: If validation fails for any reason.
    """
    if 'name' not in data or not data['name']:
        raise ValueError("E001: Name is required.")
    
    if 'email' not in data or not data['email']:
        raise ValueError("E002: Email is required.")
    
    if not re.match(EMAIL_REGEX, data['email']):
        raise ValueError("E003: Invalid email format.")

    # If we get to this point, validation is successful.
```
