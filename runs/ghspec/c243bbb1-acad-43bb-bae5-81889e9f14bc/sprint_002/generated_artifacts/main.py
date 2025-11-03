from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, constr
from sqlalchemy import create_engine, MetaData, Table, Column, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer

app = FastAPI()

# Database setup
DATABASE_URL = "sqlite:///students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Student model
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

# Create/update database schema on startup
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

# Request body for creating student
class StudentCreate(BaseModel):
    name: constr(min_length=1)  # Name required
    email: EmailStr  # Valid email format

@app.post("/students", response_model=StudentCreate)
async def create_student(student: StudentCreate):
    """
    Create a new student with name and email.
    Raises HTTP 400 for invalid email formats.
    """
    db = SessionLocal()
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {
        "message": "Student created successfully",
        "student": {"name": db_student.name, "email": db_student.email}
    }

@app.get("/students", response_model=list[StudentCreate])
async def read_students():
    """
    Retrieve all students from the database.
    Returns a list of student objects.
    """
    db = SessionLocal()
    students = db.query(Student).all()
    return [{"name": student.name, "email": student.email} for student in students]