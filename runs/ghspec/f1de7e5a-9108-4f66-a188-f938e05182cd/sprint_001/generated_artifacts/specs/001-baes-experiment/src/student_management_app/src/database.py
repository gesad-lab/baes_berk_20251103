```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import List

# SQLAlchemy setup
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Student model
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

# Create the database and tables at startup
Base.metadata.create_all(bind=engine)

# Pydantic model for input validation
class StudentCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)

# FastAPI instance
app = FastAPI()

@app.post("/students", response_model=StudentCreate, status_code=201)
def create_student(student: StudentCreate):
    """Create a new student."""
    db: Session = SessionLocal()
    db_student = Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    db.close()
    return db_student

@app.get("/students", response_model=List[StudentCreate])
def get_students():
    """Retrieve all students."""
    db: Session = SessionLocal()
    students = db.query(Student).all()
    db.close()
    return students
```