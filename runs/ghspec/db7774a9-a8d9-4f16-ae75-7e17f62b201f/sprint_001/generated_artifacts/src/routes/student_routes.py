from fastapi import APIRouter, HTTPException

# Create an instance of APIRouter for student routes
router = APIRouter()

@router.get("/health", summary="Health Check Endpoint")
async def health_check():
    """
    Health check endpoint to verify if the application is running.

    Returns a message indicating the application status.
    """
    try:
        return {"status": "OK", "message": "Application is running smoothly."}
    except Exception as e:
        # Log the error context (if logging is set up)
        raise HTTPException(status_code=500, detail="Internal Server Error") from e

# Ensure that the router is included in the FastAPI app in the main application file
# (Not included in this file; this is just a standalone function definition.)