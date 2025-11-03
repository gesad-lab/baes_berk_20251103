from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.database.database import create_db_and_tables
from src.routes.student_routes import student_router

# Initialize FastAPI application
app = FastAPI()

# Setup CORS if needed, allowing requests from all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to restrict origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include student-related routes
app.include_router(student_router)

@app.on_event("startup")
async def startup_event():
    """Create the database and tables on startup if they don't exist."""
    await create_db_and_tables()

@app.get("/")
async def read_root():
    """Root endpoint for basic health check."""
    return {"message": "Welcome to the Student API"}

# Entry point for running the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)