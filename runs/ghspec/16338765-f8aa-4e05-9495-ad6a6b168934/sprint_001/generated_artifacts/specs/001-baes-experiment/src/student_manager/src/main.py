from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize FastAPI application
app = FastAPI()

# Database configuration
DATABASE_URL = "sqlite:///./students.db"

# Create SQLite database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our models
Base = declarative_base()

# Include our routers
# from api.student_api import router as student_router
# app.include_router(student_router)

# Startup event to create databases
@app.on_event("startup")
def startup():
    # Create all tables in the database
    Base.metadata.create_all(bind=engine)

# Example root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Manager API"}