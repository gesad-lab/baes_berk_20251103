from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/health")
async def health_check():
    """
    Health check endpoint for application readiness.
    
    Returns:
        JSONResponse: JSON object indicating application status and health.
    """
    try:
        # You could implement more checks here such as checking database connectivity
        return JSONResponse(content={"status": "healthy"}, status_code=200)
    except Exception as e:
        # Log the error with context for debugging purposes
        # Here you should implement logging, and e could be used to capture the details
        return JSONResponse(content={"status": "unhealthy", "error": str(e)}, status_code=500)