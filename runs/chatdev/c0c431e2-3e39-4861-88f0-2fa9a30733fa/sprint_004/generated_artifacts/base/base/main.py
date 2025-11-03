'''
Implements the main application logic.
'''
from fastapi import FastAPI
from routes import router
from database import create_database
app = FastAPI()
# Create the database and tables
create_database()
# Include the router
app.include_router(router)