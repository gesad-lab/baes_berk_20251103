'''
Main entry point for the FastAPI application.
'''
from fastapi import FastAPI
from database import engine
from models import Base
from student_router import router as student_router
from course_router import router as course_router
# Create the FastAPI app
app = FastAPI()
# Create the database tables
Base.metadata.create_all(bind=engine)
# Include the student and course routers
app.include_router(student_router)
app.include_router(course_router)