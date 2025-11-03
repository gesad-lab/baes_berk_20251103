'''
Main entry point for the Student application.
'''
from fastapi import FastAPI
from routes import student_router
from models import Base
from database import engine
app = FastAPI()
# Create the database tables
Base.metadata.create_all(bind=engine)
# Include the student router
app.include_router(student_router)