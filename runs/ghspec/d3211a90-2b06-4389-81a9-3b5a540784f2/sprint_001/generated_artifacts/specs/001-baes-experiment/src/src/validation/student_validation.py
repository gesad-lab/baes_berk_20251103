```python
# src/validation/student_validation.py

class StudentValidationError(Exception):
    """Custom exception for student validation errors."""
    pass

def validate_student_data(data: dict):
    """
    Validate incoming student data.
    
    Parameters:
    - data (dict): A dictionary containing student data.
    
    Raises:
    - StudentValidationError: If validation fails.
    
    Returns:
    None
    """
    # Check if 'name' is in the data and not empty
    if 'name' not in data or not data['name'].strip():
        raise StudentValidationError("Name field is required.")

    # If validation passed, do nothing
    return
```