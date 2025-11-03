import time
from fastapi import FastAPI, HTTPException
from src.routes.student_routes import student_router
from src.routes.course_routes import course_router
from src.db.database import engine
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()

# Include the student and course routers in the application
app.include_router(student_router)
app.include_router(course_router)

@app.on_event("startup")
async def startup_event():
    # Example of logging the startup time
    start_time = time.time()
    logging.info("Application startup initiated.")
    
    # Assuming some initialization tasks go here...
    
    startup_duration = time.time() - start_time
    logging.info(f"Startup completed in {startup_duration:.2f} seconds.")

@app.on_event("shutdown")
async def shutdown_event():
    # Log application shutdown event
    logging.info("Application shutdown initiated.")
    
    # Clean up tasks can be performed here...

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Student Management Application!"}