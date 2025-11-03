'''
Entry point to run the FastAPI application.
'''
from fastapi import FastAPI
from student import router as student_router
from database import engine, Base
# Create the database tables
Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(student_router)