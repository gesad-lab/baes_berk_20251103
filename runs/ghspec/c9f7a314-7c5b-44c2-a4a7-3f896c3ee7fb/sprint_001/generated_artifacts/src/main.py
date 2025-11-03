from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

# Database setup
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Student model
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)

# Pydantic model for student
class StudentCreate(BaseModel):
    name: str

class StudentResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

# Create the database tables
Base.metadata.create_all(bind=engine)

# FastAPI instance
app = FastAPI()

# Create a dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API Routes
@app.post("/students", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate, db: Session = next(get_db())):
    """Create a new student."""
    db_student = Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get("/students/{id}", response_model=StudentResponse)
def retrieve_student(id: int, db: Session = next(get_db())):
    """Retrieve a student by ID."""
    db_student = db.query(Student).filter(Student.id == id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.put("/students/{id}", response_model=StudentResponse)
def update_student(id: int, student: StudentCreate, db: Session = next(get_db())):
    """Update a student's name by ID."""
    db_student = db.query(Student).filter(Student.id == id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db_student.name = student.name
    db.commit()
    db.refresh(db_student)
    return db_student

@app.delete("/students/{id}")
def delete_student(id: int, db: Session = next(get_db())):
    """Delete a student by ID."""
    db_student = db.query(Student).filter(Student.id == id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(db_student)
    db.commit()
    return {"detail": "Student deleted successfully"}