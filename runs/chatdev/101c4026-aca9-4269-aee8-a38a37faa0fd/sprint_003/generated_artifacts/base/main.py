'''
Main entry point for the FastAPI application.
'''
from fastapi import FastAPI
from api import router
from database import engine, Base
# Create the FastAPI app
app = FastAPI()
# Create the database schema on startup
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
# Include the API router
app.include_router(router)