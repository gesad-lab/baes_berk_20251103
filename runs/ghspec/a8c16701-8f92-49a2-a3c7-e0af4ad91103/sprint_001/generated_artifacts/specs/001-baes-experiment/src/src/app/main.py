from fastapi import FastAPI
import uvicorn
from src.db import init_db  # Importing the function to initialize the database

app = FastAPI(title="Student Management API", description="API for managing student information.")

@app.on_event("startup")
async def startup_event():
    """Event to run on application startup: initializes the database."""
    init_db()  # Call the database initialization function

@app.get("/")
async def read_root():
    """Root endpoint."""
    return {"message": "Welcome to the Student Management API"}

if __name__ == "__main__":
    """Run the application using uvicorn if this module is the main program."""
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Starting the server on port 8000