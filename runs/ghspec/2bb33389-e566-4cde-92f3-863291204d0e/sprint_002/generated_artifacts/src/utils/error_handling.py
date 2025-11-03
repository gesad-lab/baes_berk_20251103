```python
# src/utils/error_handling.py

from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

def validate_student_email(request: Request) -> None:
    """
    Validate the email field in the student creation request.

    Parameters:
    - request: The FastAPI request object containing the JSON body.

    Raises:
    - HTTPException: If the email field is missing from the request.
    """
    body = await request.json()
    
    # Check if email field is absent in the request body
    if 'email' not in body or not body['email']:
        # Raise a 400 Bad Request error with a meaningful message
        raise HTTPException(
            status_code=400,
            detail={
                "error": {
                    "code": "E001",
                    "message": "Missing email field. Please provide an email address.",
                    "details": {}
                }
            }
        )

    # Further validation could be added here (e.g., email format)


def handle_database_migration_error(e: Exception) -> JSONResponse:
    """
    Handle exceptions during database migration.

    Parameters:
    - e: The exception raised during migration.

    Returns:
    - JSONResponse: Standardized error response for migration-related issues.
    """
    # Log the specific database migration error for debugging
    # (Assuming there's a logging mechanism set up, e.g., logging.error(e))
    
    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "code": "E002",
                "message": "Database migration failed. Please check the logs for details.",
                "details": {}
            }
        }
    )
```