```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

Base = declarative_base()
app = FastAPI()
DATABASE_URL = 'sqlite:///students.db'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Define the Student model
class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# Pydantic model for request validation and response serialization
class StudentCreate(BaseModel):
    name: str

class StudentResponse(BaseModel):
    id: int
    name: str

# Automatic database schema creation
def initialize_database():
    Base.metadata.create_all(engine)

@app.post("/students", status_code=201, response_model=StudentResponse)
def create_student(student: StudentCreate):
    """Create a new student record."""
    if not student.name:
        raise HTTPException(status_code=400, detail="E001: Missing student name")
    
    db = SessionLocal()
    new_student = Student(name=student.name)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    db.close()
    return new_student

@app.get("/students/{id}", response_model=StudentResponse)
def read_student(id: int):
    """Retrieve a student record by ID."""
    db = SessionLocal()
    student = db.query(Student).filter(Student.id == id).first()
    db.close()
    
    if not student:
        raise HTTPException(status_code=404, detail="E002: Student not found")
    
    return student

# Run database initialization on startup
initialize_database()
```