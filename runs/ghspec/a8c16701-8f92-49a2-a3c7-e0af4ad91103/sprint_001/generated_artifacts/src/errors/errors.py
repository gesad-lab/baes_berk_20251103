```python
from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from typing import Dict


class ErrorResponse:
    """Class to structure error responses for API requests."""
    
    @staticmethod
    def validation_error(detail: str) -> Dict[str, str]:
        """Creates a structured validation error response.
        
        Args:
            detail (str): Description of the validation error.
        
        Returns:
            Dict[str, str]: Error response containing code and message.
        """
        return {
            "error": {
                "code": "E001",
                "message": detail,
                "details": {}
            }
        }
    
    @staticmethod
    def not_found_error(resource: str) -> HTTPException:
        """Creates an HTTPException for not found errors.
        
        Args:
            resource (str): The resource that was not found.
        
        Returns:
            HTTPException: Exception with 404 status and custom message.
        """
        detail = f"{resource} not found."
        return HTTPException(status_code=HTTP_404_NOT_FOUND, detail=ErrorResponse.validation_error(detail))

    @staticmethod
    def bad_request_error(detail: str) -> HTTPException:
        """Creates an HTTPException for bad request errors.
        
        Args:
            detail (str): Description of the bad request error.
        
        Returns:
            HTTPException: Exception with 400 status and custom message.
        """
        return HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=ErrorResponse.validation_error(detail))
```
