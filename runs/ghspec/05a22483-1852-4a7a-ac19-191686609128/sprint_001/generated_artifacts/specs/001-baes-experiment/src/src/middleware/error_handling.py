```python
from fastapi import Request, Response, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import logging

# Configure the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Add CORS middleware for handling cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your needs in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def error_handling_middleware(request: Request, call_next):
    try:
        # Process the request
        response: Response = await call_next(request)
        return response
    except HTTPException as http_exc:
        # Handle HTTP exceptions directly
        logger.error(f"HTTP exception occurred: {http_exc.detail}")
        return JSONResponse(
            status_code=http_exc.status_code,
            content={"error": {"code": "E001", "message": http_exc.detail}},
        )
    except Exception as exc:
        # Handle all other exceptions
        logger.error(f"Unhandled exception occurred: {str(exc)}")
        # Return a 500 Internal Server Error response
        return JSONResponse(
            status_code=500,
            content={"error": {"code": "E002", "message": "Internal server error."}},
        )
```