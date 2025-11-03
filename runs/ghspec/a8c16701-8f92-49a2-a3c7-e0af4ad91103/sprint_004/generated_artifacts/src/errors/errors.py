```python
# src/errors/errors.py

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

# Custom error codes for the application
ERROR_CODES = {
    'E001': 'Invalid course ID provided',
    'E002': 'Student not found',
    'E003': 'Course not found',
    'E004': 'Database integrity error',
}

def handle_invalid_course_id():
    """
    Raises an HTTP exception for an invalid course ID.
    """
    raise HTTPException(status_code=400, detail={
        'error': {
            'code': 'E001',
            'message': ERROR_CODES['E001'],
            'details': {}
        }
    })

def handle_student_not_found():
    """
    Raises an HTTP exception if the student is not found.
    """
    raise HTTPException(status_code=404, detail={
        'error': {
            'code': 'E002',
            'message': ERROR_CODES['E002'],
            'details': {}
        }
    })

def handle_course_not_found():
    """
    Raises an HTTP exception if the specified course does not exist.
    """
    raise HTTPException(status_code=404, detail={
        'error': {
            'code': 'E003',
            'message': ERROR_CODES['E003'],
            'details': {}
        }
    })

def handle_database_integrity_error(exc: IntegrityError):
    """
    Handle database integrity errors and raise a suitable HTTP exception.
    
    Parameters:
    - exc: The IntegrityError exception that occurred.
    """
    # Log exception here if necessary (with details)
    raise HTTPException(status_code=400, detail={
        'error': {
            'code': 'E004',
            'message': ERROR_CODES['E004'],
            'details': {
                'error_message': str(exc.orig)
            }
        }
    })

# These functions can be utilized in the API request handling 
# for associating courses to a student to provide structured and informative error handling.
```