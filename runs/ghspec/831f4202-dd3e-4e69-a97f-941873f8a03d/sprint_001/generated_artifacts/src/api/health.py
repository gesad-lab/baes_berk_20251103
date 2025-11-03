from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/health")
async def health_check():
    """
    Health Check Endpoint

    Returns:
        JSON response containing the health status of the application.
    """
    try:
        # Sample health check logic; this could be enhanced
        return JSONResponse(content={"status": "healthy"}, status_code=200)
    except Exception as e:
        # Log the exception details for debugging purposes
        # In a real application, you may want to log this to a file or logging service
        return JSONResponse(content={"error": {"code": "E500", "message": "Internal Server Error"}}, status_code=500)