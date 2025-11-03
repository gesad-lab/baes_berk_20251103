```python
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

class ErrorHandlerMiddleware:
    """Middleware to handle errors gracefully and return consistent JSON responses."""
    
    async def __call__(self, request: Request, call_next):
        try:
            response = await call_next(request)
            # If response status is an error (4xx or 5xx), modify it
            if response.status_code >= 400:
                return await self.handle_error_response(response)
            return response
        except Exception as e:
            return self.handle_unexpected_error(e)

    async def handle_error_response(self, response):
        """Handle error responses and provide structured JSON error output."""
        error_details = {
            "error": {
                "code": "E001",
                "message": "An error occurred",
                "details": self.get_error_details(response)
            }
        }
        return JSONResponse(
            status_code=response.status_code,
            content=error_details
        )

    def handle_unexpected_error(self, exc):
        """Handle unexpected exceptions."""
        error_details = {
            "error": {
                "code": "E500",
                "message": "Internal Server Error",
                "details": str(exc)  # Log the actual error for debugging
            }
        }
        return JSONResponse(
            status_code=500,
            content=error_details
        )

    def get_error_details(self, response):
        """Provide a human-readable explanation for common error scenarios."""
        if response.status_code == 422:
            return "Validation errors occurred. Please check input data."
        elif response.status_code == 409:
            return "Conflict: An entry with this data already exists."
        return "Unexpected error. Please try again later."
```