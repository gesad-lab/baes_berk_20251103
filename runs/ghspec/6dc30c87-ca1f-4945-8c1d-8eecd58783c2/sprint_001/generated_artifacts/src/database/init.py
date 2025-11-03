```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database setup
DATABASE_URL = "sqlite:///./test.db"  # Example SQLite database URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # name is a required field


Base.metadata.create_all(bind=engine)  # Create database schema at startup

# FastAPI application
app = FastAPI()


class StudentCreate(BaseModel):
    name: str = Field(..., title="Name of the student", max_length=50)

    # Additional validation can be added here if necessary


@app.post("/students", response_model=StudentCreate, status_code=201)
async def create_student(student: StudentCreate):
    """
    Create a new student in the database.

    Args:
        student (StudentCreate): The student object containing the name.

    Returns:
        StudentCreate: The created student object.

    Raises:
        HTTPException: If validation fails.
    """
    # Validate the incoming student data
    if not student.name:
        raise HTTPException(
            status_code=400,
            detail={"error": {"code": "E001", "message": "Name field is required."}},
        )

    # Normally we would save the student to the database here
    # Example of what saving would look like (commented out for demonstration):
    # db = SessionLocal()
    # db_student = Student(name=student.name)
    # db.add(db_student)
    # db.commit()
    # db.refresh(db_student)

    return {"name": student.name}  # Return the created student data


@app.get("/students/{student_id}", response_model=StudentCreate)
async def get_student(student_id: int):
    """
    Retrieve a student by their ID.

    Args:
        student_id (int): The ID of the student to retrieve.

    Returns:
        StudentCreate: The student object retrieved from the database.

    Raises:
        HTTPException: If the student is not found.
    """
    # Normally we would retrieve the student from the database here
    # Mock database logic for demonstration:
    # db = SessionLocal()
    # student = db.query(Student).filter(Student.id == student_id).first()

    student = None  # Replace this with actual database retrieval logic

    if not student:
        raise HTTPException(status_code=404, detail={"error": {"code": "E002", "message": "Student not found."}})

    return {"name": student.name}  # Return the student data
```