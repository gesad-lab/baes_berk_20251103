```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes import student  # Import the new router for handling student course assignments

app = FastAPI()

# CORS configuration (if required)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the student router to handle course assignments
app.include_router(student.router)

# Other existing app configuration and routes...

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}
```