```python
from fastapi import APIRouter
from app.db import init_db
from fastapi import FastAPI

# Create a new FastAPI instance
app = FastAPI()

# Initialize API router
router = APIRouter()

# Call init_db on application startup to set up the database schema
@app.on_event("startup")
async def startup_event():
    try:
        init_db()  # Initialize the database schema
    except Exception as e:
        # Log error from the database initialization
        print(f"Error during database initialization: {e}")

# Include your API routes here
@app.get("/health")
async def health_check():
    return {"status": "ok"}

# Define your API routes in this file or include them from other files
app.include_router(router)
```