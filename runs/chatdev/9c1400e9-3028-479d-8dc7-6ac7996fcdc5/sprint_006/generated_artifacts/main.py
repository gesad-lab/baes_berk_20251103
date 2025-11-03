'''
Main entry point for the FastAPI application.
'''
from fastapi import FastAPI
from database import engine
from models import Base
from student_router import router as student_router
from course_router import router as course_router
from teacher_router import router as teacher_router
from alembic import command
from alembic.config import Config
# Create the FastAPI app
app = FastAPI()
# Create the database schema on startup
@app.on_event("startup")
def startup():
    # Run migrations
    alembic_cfg = Config("alembic.ini")  # Ensure you have an alembic.ini file configured
    command.upgrade(alembic_cfg, "head")  # This will apply all migrations
    Base.metadata.create_all(bind=engine)
# Include the student, course, and teacher routers
app.include_router(student_router)
app.include_router(course_router)
app.include_router(teacher_router)