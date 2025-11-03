from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse

router = APIRouter()

@router.get("/health", response_class=JSONResponse)
async def health_check():
    """
    Health Check Endpoint

    Returns the status of the service.
    """
    try:
        # TODO: Add any necessary checks (e.g. database connectivity) later
        return JSONResponse(status_code=200, content={"status": "healthy"})
    except Exception as e:
        # Log the error for debugging purposes (not user-facing)
        # In a real application, you might want to log this to a file or monitoring system
        raise HTTPException(status_code=500, detail={"error": {"code": "E003", "message": "Internal server error."}})