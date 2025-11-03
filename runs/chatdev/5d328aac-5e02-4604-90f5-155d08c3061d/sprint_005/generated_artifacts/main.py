'''
Main entry point for the FastAPI application.
'''
from fastapi import FastAPI
from database import engine, SessionLocal
from models import Base
from routers import router as student_router
# Create the FastAPI app
app = FastAPI()
# Create the database tables automatically on startup
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
# Include the student, course, and teacher router
app.include_router(student_router)