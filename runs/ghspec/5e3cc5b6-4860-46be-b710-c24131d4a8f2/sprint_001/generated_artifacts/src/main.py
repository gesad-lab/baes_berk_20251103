from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import student_routes  # Assuming the routes are in the routers package
import uvicorn

# Initialize the FastAPI application
app = FastAPI(title="Student Management API", description="API for managing student records", version="1.0.0")

# Allow CORS for all origins (this can be restricted to specific origins in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific origins in a production environment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include student routes
app.include_router(student_routes.router)

# Main entry point for running the application
if __name__ == "__main__":
    # Run the application via uvicorn when executing this script
    uvicorn.run(app, host="127.0.0.1", port=8000)

# Swagger UI will be available at: http://127.0.0.1:8000/docs
# ReDoc documentation will be at: http://127.0.0.1:8000/redoc