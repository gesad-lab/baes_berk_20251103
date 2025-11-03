```python
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

# Create a router for grouping routes
router = APIRouter()

@router.get("/health")
async def health_check() -> JSONResponse:
    """
    Health check endpoint to monitor system status.
    Returns a 200 OK response when the system is healthy.

    Returns:
        JSONResponse: A response indicating system health.
    """
    return JSONResponse(content={"status": "healthy"}, status_code=200)

# Include the router in the main FastAPI app (this should be done in the main application file)
# Example:
# from fastapi import FastAPI
# from .health_check import router as health_router
# app.include_router(health_router)
```