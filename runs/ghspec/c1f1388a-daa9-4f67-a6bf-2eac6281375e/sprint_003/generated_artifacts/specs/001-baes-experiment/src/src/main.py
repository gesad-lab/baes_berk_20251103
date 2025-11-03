from fastapi import FastAPI
from src.api.student_routes import router as student_router
from src.api.course_routes import router as course_router  # Import course routes

app = FastAPI()

# Include existing student routes
app.include_router(student_router)

# Include new course routes
app.include_router(course_router)

@app.on_event("startup")
async def startup_event():
    # Setup code to initialize resources if necessary
    pass

@app.on_event("shutdown")
async def shutdown_event():
    # Cleanup code to close resources if necessary
    pass