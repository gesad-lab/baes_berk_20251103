```python
# student-management/main.py

from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Create the FastAPI application
app = FastAPI()

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for SQLAlchemy models
Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)  # Auto-incrementing id column
    name = Column(String, nullable=False)  # Name column, required field

# Function to initialize the database and create the schema
def init_db():
    # Create the database schema
    Base.metadata.create_all(bind=engine)

@app.on_event("startup")
async def startup_event():
    """Initialize the database on startup."""
    init_db()

@app.post("/students", response_model=dict)
async def create_student(student: dict):
    """
    Create a new student.

    Args:
        student (dict): The student data containing 'name'.

    Returns:
        JSON response with success message and created student data.
    """
    name = student.get("name")
    if not name:
        raise HTTPException(status_code=400, detail="E001: Student name is required.")

    # Create a new student in the database
    with SessionLocal() as db:
        new_student = Student(name=name)
        db.add(new_student)
        db.commit()
        db.refresh(new_student)

    return {"message": "Student created successfully", "student": {"id": new_student.id, "name": new_student.name}}

@app.get("/students", response_model=list)
async def read_students():
    """
    Retrieve a list of all students.

    Returns:
        JSON array of student objects.
    """
    with SessionLocal() as db:
        students = db.query(Student).all()
        return [{"id": student.id, "name": student.name} for student in students]

# Run the application using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```