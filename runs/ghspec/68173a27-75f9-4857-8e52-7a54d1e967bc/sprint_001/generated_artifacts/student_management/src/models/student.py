from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize the FastAPI application
app = FastAPI()

# Database configuration
DATABASE_URL = "sqlite:///./students.db"  # SQLite database file
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for SQLAlchemy models
Base = declarative_base()

# Health Check Endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Student Management API!"}

# Additional configuration for initializing models can be added here
# Example: Base.metadata.create_all(bind=engine) to create tables

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)