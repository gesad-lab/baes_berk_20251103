```python
# src/validators.py

# Module for input validation related to student operations

import logging
from typing import Dict, Any

# Initialize logger for input validation
logger = logging.getLogger("student_api")

class ValidationError(Exception):
    """Custom exception to indicate validation errors."""
    pass

def validate_student_creation(data: Dict[str, Any]) -> None:
    """
    Validate input data for student creation.

    Parameters:
    - data (dict): The input data containing student attributes.

    Raises:
    - ValidationError: If any validation checks fail.
    """
    logger.debug("Validating student creation data: %s", data)
    
    if not isinstance(data.get('name'), str):
        logger.error("Validation error: Name must be a string.")
        raise ValidationError("E001: Name must be a string.")
    
    if not data['name'].strip():
        logger.error("Validation error: Name is required.")
        raise ValidationError("E002: Name is required.")

    logger.info("Validation successful for student creation: %s", data['name'])
```