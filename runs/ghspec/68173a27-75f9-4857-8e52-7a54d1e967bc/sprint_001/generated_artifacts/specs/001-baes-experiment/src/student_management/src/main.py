```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Initialize FastAPI
app = FastAPI()

# Configure SQLite database connection with SQLAlchemy
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define Student model
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)

# Create database schema on application startup
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

# Pydantic model for student input
class StudentCreate(BaseModel):
    name: str
    age: int

# Service to handle student operations
def get_students(db: Session, skip: int = 0, limit: int = 10) -> List[Student]:
    return db.query(Student).offset(skip).limit(limit).all()

def create_student(db: Session, student: StudentCreate) -> Student:
    db_student = Student(name=student.name, age=student.age)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# API routes
@app.post("/students/", response_model=Student)
def create_student_route(student: StudentCreate):
    db = SessionLocal()
    try:
        return create_student(db, student)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()

@app.get("/students/", response_model=List[Student])
def read_students(skip: int = 0, limit: int = 10):
    db = SessionLocal()
    try:
        return get_students(db, skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()
```