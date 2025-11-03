```python
# src/error_handlers/error_responses.py

from fastapi import HTTPException
import logging

# Configure logging
logger = logging.getLogger(__name__)

class ErrorResponse:
    """Class to encapsulate error response formats."""
    
    @staticmethod
    def validation_error(message: str):
        """Generate a validation error response."""
        logger.error(f"Validation error: {message}")
        raise HTTPException(status_code=400, detail={"error": {"code": "E001", "message": message}})

    @staticmethod
    def not_found_error(entity: str, entity_id: str):
        """Generate a not found error response."""
        message = f"{entity.capitalize()} with ID {entity_id} not found."
        logger.warning(message)
        raise HTTPException(status_code=404, detail={"error": {"code": "E002", "message": message}})

    @staticmethod
    def generic_error(message: str):
        """Generate a generic error response."""
        logger.error(f"Generic error: {message}")
        raise HTTPException(status_code=500, detail={"error": {"code": "E003", "message": message}})

def get_students(students_list):
    """
    Retrieve and format the list of students for the API response.

    Args:
        students_list (List[Student]): A list of Student objects.
    
    Returns:
        List[Dict]: A List of dictionaries representing each student's data including ID, name, and email.
    """
    if not students_list:
        return []

    # Prepare the response data including email field
    response_data = []
    for student in students_list:
        response_data.append({
            "id": student.id,
            "name": student.name,
            "email": student.email  # Including email field in the response
        })
    
    return response_data
```