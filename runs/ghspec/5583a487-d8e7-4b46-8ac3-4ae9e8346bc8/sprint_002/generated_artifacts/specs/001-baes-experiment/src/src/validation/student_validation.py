```python
# src/validation/student_validation.py

import re
from flask import request
from typing import Tuple, Optional

# Email regex pattern for basic validation
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def validate_student_data(data: dict) -> Tuple[bool, Optional[str]]:
    """
    Validates the student input data.

    Parameters:
    - data (dict): A dictionary containing student data with 'name' and 'email'

    Returns:
    - Tuple[bool, Optional[str]]: A tuple where the first element indicates 
      if the validation passed, and the second element contains an error message 
      if it failed.
    """
    if 'name' not in data or not isinstance(data['name'], str) or not data['name']:
        return False, "E001: 'name' field is required and must be a non-empty string."

    if 'email' not in data or not isinstance(data['email'], str) or not data['email']:
        return False, "E002: 'email' field is required and must be a non-empty string."

    if not re.match(EMAIL_REGEX, data['email']):
        return False, "E003: Invalid email format."

    # If all validations pass
    return True, None
```