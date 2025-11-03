from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

# Database setup
DATABASE_URL = "sqlite:///./students.db"  # SQLite database URI
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Student model definition
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# Create the database schema
Base.metadata.create_all(bind=engine)

# FastAPI instance
app = FastAPI()

# Pydantic model for student input
class StudentCreate(BaseModel):
    name: str

@app.post("/students", response_model=StudentCreate)
async def create_student(student: StudentCreate):
    """
    Create a new student in the database.

    Args:
    student (StudentCreate): Data for the new student.

    Raises:
    HTTPException: If a database error occurs.

    Returns:
    StudentCreate: The created student data.
    """
    db = SessionLocal()
    try:
        db_student = Student(name=student.name)
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error creating student - validation conflict.")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
    finally:
        db.close()

@app.get("/students/{student_id}", response_model=StudentCreate)
async def read_student(student_id: int):
    """
    Retrieve a student by ID from the database.

    Args:
    student_id (int): The ID of the student to retrieve.

    Raises:
    HTTPException: If the student's ID is not found.

    Returns:
    StudentCreate: The student's data.
    """
    db = SessionLocal()
    try:
        student = db.query(Student).filter(Student.id == student_id).first()
        if student is None:
            raise HTTPException(status_code=404, detail="Student not found.")
        return student
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
    finally:
        db.close()