'''
Implements the FastAPI application and includes the database creation on startup.
'''
from fastapi import FastAPI
from database import create_database
from routes import router
app = FastAPI()
@app.on_event("startup")
def startup_event():
    '''
    Event that runs on application startup.
    '''
    create_database()
app.include_router(router)