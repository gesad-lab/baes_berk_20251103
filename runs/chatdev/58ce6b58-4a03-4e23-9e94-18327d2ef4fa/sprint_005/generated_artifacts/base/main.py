'''
Contains the main entry point for the application.
'''
from fastapi import FastAPI
from routes import router
from database import create_database
app = FastAPI()
# Create the database and tables
create_database()
# Include the router for API endpoints
app.include_router(router)