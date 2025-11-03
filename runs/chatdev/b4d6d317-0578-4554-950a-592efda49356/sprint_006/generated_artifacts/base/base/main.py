'''
Main entry point for the application.
'''
from fastapi import FastAPI
from routes import router
from database import create_database
app = FastAPI()
@app.on_event("startup")
def startup_event():
    '''
    Create the database on startup.
    '''
    create_database()
app.include_router(router)