from fastapi import FastAPI, HTTPException
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import List

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Student model definition
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Name field must be non-nullable

# Create the database schema on startup
Base.metadata.create_all(bind=engine)

# FastAPI instance
app = FastAPI()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/students", response_model=Student)
async def create_student(name: str, db: Session = next(get_db())):
    if not name:
        raise HTTPException(status_code=400, detail="Name is required.")
    
    new_student = Student(name=name)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    
    return new_student

@app.get("/students", response_model=List[Student])
async def retrieve_students(db: Session = next(get_db())):
    students = db.query(Student).all()
    return students
