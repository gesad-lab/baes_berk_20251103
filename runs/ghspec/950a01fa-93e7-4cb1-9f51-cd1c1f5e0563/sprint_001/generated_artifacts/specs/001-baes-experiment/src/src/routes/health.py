from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

# Create a FastAPI router instance for health checks
router = APIRouter()

@router.get("/health", response_description="Health check status")
async def health_check():
    """
    Health Check Endpoint
    Returns a response to indicate the application is running.
    """
    try:
        # Basic health check logic
        return JSONResponse(content={"status": "healthy"}, status_code=200)
    except Exception as e:
        # Log the error and return an unhealthy status
        # Ideally, you would use logging here
        raise HTTPException(status_code=500, detail="Health check failed") from e