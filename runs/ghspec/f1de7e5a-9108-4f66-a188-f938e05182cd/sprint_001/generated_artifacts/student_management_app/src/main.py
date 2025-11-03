```python
from fastapi import FastAPI, HTTPException
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from schemas import StudentCreate

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the FastAPI app
app = FastAPI()

# Database setup
DATABASE_URL = 'sqlite:///students.db'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException):
    """
    Global exception handler for HTTPException

    Args:
        request: The request that caused the exception.
        exc: The HTTPException instance.

    Returns:
        A JSON response with the error details.
    """
    logger.error(f"HTTPException occurred: {exc.detail}")  # Log the error details
    return {
        "error": {
            "code": str(exc.status_code),
            "message": exc.detail
        }
    }

@app.post("/students", status_code=201)
async def create_student(student: StudentCreate):
    """
    Create a new student entry.

    Args:
        student: The student data to create.

    Returns:
        The created student object.
    """
    if not student.name:
        raise HTTPException(status_code=400, detail="Name must not be empty.")
    
    # Logic to add the student to the database goes here
    # ...
    return {"name": student.name}  # This should return the created student object (stub for now)

@app.get("/students")
async def get_students():
    """
    Retrieve a list of all students.

    Returns:
        A list of student objects.
    """
    # Logic to retrieve students from the database goes here
    # ...
    return []  # This should return the list of students (stub for now)
```