from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

DATABASE_URL = "sqlite:///./students.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()


class StudentModel(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)


Base.metadata.create_all(bind=engine)


class StudentCreate(BaseModel):
    name: str = Field(..., description="The name of the student.")


class StudentOut(BaseModel):
    id: int
    name: str


@app.post("/students", response_model=StudentOut)
async def create_student(student: StudentCreate):
    """Create a new student in the database."""
    if not student.name:
        raise HTTPException(status_code=400, detail="Name field cannot be empty")

    db = SessionLocal()
    new_student = StudentModel(name=student.name)
    db.add(new_student)
    
    try:
        db.commit()
        db.refresh(new_student)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Student with provided data already exists.")

    return new_student


@app.get("/students/{student_id}", response_model=StudentOut)
async def read_student(student_id: int):
    """Retrieve a specific student's details by ID."""
    db = SessionLocal()
    student = db.query(StudentModel).filter(StudentModel.id == student_id).first()
    
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return student