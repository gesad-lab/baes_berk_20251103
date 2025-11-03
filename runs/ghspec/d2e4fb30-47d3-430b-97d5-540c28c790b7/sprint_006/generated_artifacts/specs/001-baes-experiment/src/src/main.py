```python
# src/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import courses  # Import the newly created courses routes

app = FastAPI()

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as necessary for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include existing routers
app.include_router(courses.router)  # Include the courses routes

# You can include other routers here as needed
# e.g., app.include_router(another_router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Educational Application API!"}

# Other application-level configurations and routes...
```