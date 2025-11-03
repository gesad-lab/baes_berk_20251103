from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from src.models import Course  # Assuming Course model is defined in models.py
from src.schemas import CourseCreate  # Assuming CourseCreate schema is defined in schemas.py

app = FastAPI()

@app.get("/health", response_model=dict)
async def health_check():
    """
    Health check endpoint to validate service availability.
    
    This endpoint does not take any input and returns a JSON response indicating the service 
    status. A status of 'OK' confirms that the service is running as expected.
    
    Returns:
        dict: JSON response with the health status.
    """
    return JSONResponse(content={"status": "OK"})

# Other existing endpoints for Course entity will follow here...