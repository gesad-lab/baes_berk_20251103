'''
Main entry point for the application.
'''
from fastapi import FastAPI
from routes import student_router
from database import init_db
app = FastAPI()
# Initialize the database
init_db()
# Include the student and course routes
app.include_router(student_router)