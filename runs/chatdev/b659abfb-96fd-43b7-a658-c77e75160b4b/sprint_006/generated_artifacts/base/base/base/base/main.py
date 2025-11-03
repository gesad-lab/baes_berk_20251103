'''
Main entry point for the FastAPI application.
'''
from fastapi import FastAPI
from database import engine
from models import Base
from student_router import router as student_router
# Create the FastAPI app
app = FastAPI()
# Create the database tables
Base.metadata.create_all(bind=engine)
# Include the student router
app.include_router(student_router)