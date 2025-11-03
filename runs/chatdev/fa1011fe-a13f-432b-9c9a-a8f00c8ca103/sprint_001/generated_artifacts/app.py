'''
Main entry point for the FastAPI application.
'''
from fastapi import FastAPI
from api import student_router
from database import init_db
app = FastAPI()
# Initialize the database
init_db()
app.include_router(student_router)