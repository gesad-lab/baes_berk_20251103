from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.middleware.cors import CORSMiddleware
import os

# Set up database configuration and create SQLAlchemy engine
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./students.db")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
Base = declarative_base()

# Create FastAPI instance
app = FastAPI()

# Middleware for managing CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import and include API routes (will be implemented in a separate file)
from .api.student_routes import router as student_router

# Include student routes
app.include_router(student_router, prefix="/students", tags=["students"])

def init_db():
    # Create all tables in the database (if they don't exist)
    Base.metadata.create_all(bind=engine)

@app.on_event("startup")
async def startup_event():
    """
    Run initialization tasks, such as database setup, during application startup.
    """
    init_db()  # Ensure the database schema is created upon startup
    

@app.on_event("shutdown")
async def shutdown_event():
    """
    Cleanup tasks during application shutdown (if necessary).
    """
    # Add any necessary cleanup code here

# Default root route
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Student Management API!"}