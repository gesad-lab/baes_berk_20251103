'''
Main application entry point.
'''
from fastapi import FastAPI
from routes import student_router, course_router, teacher_router
from database import create_database
app = FastAPI()
# Create the database
create_database()
# Include routers
app.include_router(student_router)
app.include_router(course_router)
app.include_router(teacher_router)