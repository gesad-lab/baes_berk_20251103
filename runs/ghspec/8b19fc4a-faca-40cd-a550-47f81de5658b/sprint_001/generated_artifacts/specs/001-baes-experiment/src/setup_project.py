from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from pydantic import BaseModel, constr
import os
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")  # Default to SQLite if not set
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# FastAPI instance
app = FastAPI()

# Student model definition
class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# Pydantic model for input validation
class StudentCreate(BaseModel):
    name: constr(min_length=1)  # Name must be at least 1 character long

# Create the database tables
def create_database():
    logger.info("Creating database tables...")
    Base.metadata.create_all(bind=engine)

@app.post("/students", response_model=StudentCreate)
def create_student(student: StudentCreate):
    """Create a new student in the database."""
    db: Session = SessionLocal()
    new_student = Student(name=student.name)
    db.add(new_student)
    
    # Try to commit the student and handle possible exceptions
    try:
        db.commit()
        db.refresh(new_student)
        logger.info(f"Created student with ID: {new_student.id}")
        return new_student
    except Exception as e:
        db.rollback()  # Rollback in case of error
        logger.error(f"Failed to create student: {e}")
        raise HTTPException(status_code=400, detail="Could not create student")  # User-friendly error

@app.get("/students/{id}", response_model=StudentCreate)
def get_student(id: int):
    """Retrieve a student's details by their ID."""
    db: Session = SessionLocal()
    student = db.query(Student).filter(Student.id == id).first()
    
    if student is None:
        logger.warning(f"Student with ID {id} not found")
        raise HTTPException(status_code=404, detail="Student not found")

    logger.info(f"Retrieved student with ID: {id}")
    return student

if __name__ == "__main__":
    create_database()  # Create database tables when script runs
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)  # Run the FastAPI app