from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://user:password@localhost/dbname"  # Update with your database URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)


# Initialize FastAPI app
app = FastAPI()

# Pydantic model for creating a student
class StudentCreate(BaseModel):
    name: str = Field(..., example="John Doe")

@app.on_event("startup")
def startup():
    # Create database schema on startup
    Base.metadata.create_all(bind=engine)

@app.post("/students", response_model=StudentCreate)
def create_student(student: StudentCreate):
    # Validate if the name is provided
    if not student.name:
        raise HTTPException(status_code=400, detail="Name field is required.")
    
    db: Session = SessionLocal()
    db_student = Student(name=student.name)
    
    # Add the new student to the database
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    
    return db_student

@app.get("/students", response_model=list[StudentCreate])
def get_students():
    db: Session = SessionLocal()
    students = db.query(Student).all()  # Retrieve all students
    return students