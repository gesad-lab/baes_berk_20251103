```python
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    """
    Middleware for centralized error handling.
    
    Catches exceptions raised during request processing and returns
    a standardized JSON error response format.
    """

    async def dispatch(self, request: Request, call_next):
        try:
            # Process the request and get the response
            response = await call_next(request)
            return response
        except HTTPException as http_exc:
            # Handle HTTP exceptions and provide a structured response
            return JSONResponse(
                status_code=http_exc.status_code,
                content={"error": {"code": str(http_exc.status_code), "message": http_exc.detail}},
            )
        except Exception as exc:
            # Handle all other exceptions as server errors
            return JSONResponse(
                status_code=500,
                content={"error": {"code": "E500", "message": "An internal server error occurred."}},
            )
```