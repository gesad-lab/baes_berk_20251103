```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import os

# Load environment variable for the SQLite database URI
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# Initialize the FastAPI application
app = FastAPI()

# Define the SQLAlchemy Base
Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# Create the database engine
engine = create_engine(DATABASE_URL)
# Create all tables in the database (including the Student table)
Base.metadata.create_all(bind=engine)

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Pydantic schema for input validation
class StudentCreate(BaseModel):
    name: str = Field(..., example="John Doe")

class StudentResponse(BaseModel):
    id: int
    name: str

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a Student
@app.post("/students", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate, db: SessionLocal = next(get_db())):
    db_student = Student(name=student.name)
    db.add(db_student)
    
    try:
        db.commit()
        db.refresh(db_student)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Student with this name already exists.")

    return db_student

# Retrieve a Student by ID
@app.get("/students/{student_id}", response_model=StudentResponse)
def read_student(student_id: int, db: SessionLocal = next(get_db())):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# Handle errors for missing fields
@app.exception_handler(ValueError)
def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )
```