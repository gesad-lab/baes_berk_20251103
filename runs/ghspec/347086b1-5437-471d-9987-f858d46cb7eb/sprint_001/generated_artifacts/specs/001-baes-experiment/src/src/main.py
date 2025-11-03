from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a FastAPI instance
app = FastAPI()

# Database configuration
DATABASE_URL = "sqlite:///./students.db"  # SQLite database for ease of use
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base model for SQLAlchemy
Base = declarative_base()

# Create the database tables
def init_db():
    Base.metadata.create_all(bind=engine)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Student API"}

# Initialize the database tables at startup
@app.on_event("startup")
def startup_event():
    init_db()