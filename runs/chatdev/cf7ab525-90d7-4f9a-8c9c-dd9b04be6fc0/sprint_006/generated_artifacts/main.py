'''
Main entry point for the application.
'''
from fastapi import FastAPI
from routes import router
from database import create_database
app = FastAPI()
create_database()  # Create the database and tables
app.include_router(router)