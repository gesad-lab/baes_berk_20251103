```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Initialize FastAPI application
app = FastAPI()

# Initialize database connection and ORM
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Define the Student model
class Student(Base):
    """Represents a student in the system."""
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# Create the database schema if it does not exist
Base.metadata.create_all(bind=engine)

# Pydantic schema for validating input and output data
class StudentCreate(BaseModel):
    """Schema for creating a new student."""
    name: str

class StudentOut(StudentCreate):
    """Schema for returning student data."""
    id: int

    class Config:
        orm_mode = True

# Dependency to get the database session
def get_db():
    """Dependency that provides a database session."""
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/students", response_model=StudentOut, status_code=201)
def create_student(student: StudentCreate, db: Session = next(get_db())):
    """Create a new student record."""
    db_student = Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get("/students", response_model=list[StudentOut], status_code=200)
def read_students(skip: int = 0, limit: int = 100, db: Session = next(get_db())):
    """Retrieve all student records."""
    students = db.query(Student).offset(skip).limit(limit).all()
    return students

@app.put("/students/{id}", response_model=StudentOut, status_code=200)
def update_student(id: int, student: StudentCreate, db: Session = next(get_db())):
    """Update an existing student record."""
    db_student = db.query(Student).filter(Student.id == id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    db_student.name = student.name
    db.commit()
    db.refresh(db_student)
    return db_student

@app.delete("/students/{id}", status_code=204)
def delete_student(id: int, db: Session = next(get_db())):
    """Delete a student record."""
    db_student = db.query(Student).filter(Student.id == id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    db.delete(db_student)
    db.commit()
    return
```