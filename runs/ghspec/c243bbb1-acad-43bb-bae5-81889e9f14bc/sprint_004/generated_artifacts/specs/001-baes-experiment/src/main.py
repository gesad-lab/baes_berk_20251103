```python
# main.py

import logging
from fastapi import FastAPI
from api.courses import courses_bp

# Initialize the FastAPI application
app = FastAPI()

# Set up logging for API interactions
logging.basicConfig(level=logging.INFO,  # Set log level to INFO
                    format='%(asctime)s - %(levelname)s - %(message)s')

@app.middleware("http")
async def log_requests(request, call_next):
    """
    Middleware to log each API request and response.
    Logs request details and the response status code.
    """
    logging.info(f"Request: {request.method} {request.url}")
    
    response = await call_next(request)

    logging.info(f"Response: status_code={response.status_code}")
    return response

# Include blueprint for courses
app.include_router(courses_bp, prefix="/api/v1/courses", tags=["courses"])

# Optional: Add a health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
```