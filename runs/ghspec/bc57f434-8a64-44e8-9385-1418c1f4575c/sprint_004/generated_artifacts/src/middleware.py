```python
# src/middleware.py

from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

class ErrorHandlerMiddleware:
    """Middleware for handling errors uniformly across the API."""

    async def __call__(self, request: Request, call_next):
        try:
            # Call the next middleware/endpoint
            response = await call_next(request)
            return response
        except HTTPException as http_exc:
            # Handle HTTP exceptions (e.g., 404, 400)
            return JSONResponse(
                status_code=http_exc.status_code,
                content={"error": {"code": f"E{http_exc.status_code}", "message": http_exc.detail}},
            )
        except ValueError as val_exc:
            # Handle specific value errors
            return JSONResponse(
                status_code=400,
                content={"error": {"code": "E400", "message": str(val_exc)}},
            )
        except Exception as exc:
            # Handle all other exceptions
            return JSONResponse(
                status_code=500,
                content={"error": {"code": "E500", "message": "An unexpected error occurred."}},
            )

# Example usage:
# app.add_middleware(ErrorHandlerMiddleware)
```