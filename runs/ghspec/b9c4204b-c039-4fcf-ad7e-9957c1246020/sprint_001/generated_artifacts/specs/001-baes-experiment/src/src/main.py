from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from time import time
import json

# Database setup
DATABASE_URL = "sqlite:///./students.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)


# Create database tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI()


class StudentCreate(BaseModel):
    name: str


@app.post("/students/", response_model=StudentCreate)
async def create_student(student: StudentCreate):
    start_time = time()  # Start timing the request

    if not student.name:
        raise HTTPException(status_code=400, detail="Name field is required")
    
    db = SessionLocal()
    new_student = Student(name=student.name)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    db.close()

    response_time = time() - start_time  # Calculate response time
    print(f"Response time for create_student: {response_time:.4f} seconds")  # Log response time

    return new_student


@app.get("/students/", response_model=list[StudentCreate])
async def list_students():
    start_time = time()  # Start timing the request
    
    db = SessionLocal()
    students = db.query(Student).all()
    db.close()
    
    response_time = time() - start_time  # Calculate response time
    print(f"Response time for list_students: {response_time:.4f} seconds")  # Log response time

    return students