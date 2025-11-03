'''
Main entry point of the FastAPI application.
'''
from fastapi import FastAPI
from database import engine
from models import Base
from routers import student_router, course_router
# Create the FastAPI app
app = FastAPI()
# Create the database schema on startup
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)  # This will create both Student and Course tables
# Include the student and course routers
app.include_router(student_router)
app.include_router(course_router)