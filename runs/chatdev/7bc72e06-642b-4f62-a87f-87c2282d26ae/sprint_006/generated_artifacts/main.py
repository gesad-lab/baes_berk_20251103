'''
Entry point to run the FastAPI application.
'''
from fastapi import FastAPI
from student import router as student_router
from course import router as course_router
from teacher import router as teacher_router
from database import engine, Base
# Create the database tables
Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(student_router)
app.include_router(course_router)
app.include_router(teacher_router)