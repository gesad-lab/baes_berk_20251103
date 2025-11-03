'''
Main entry point of the FastAPI application.
'''
from fastapi import FastAPI
from database import engine, SessionLocal
from models import Base
from routers import student_router
# Create the FastAPI app
app = FastAPI()
# Create the database schema on startup
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
# Include the student router
app.include_router(student_router)