```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database setup
DATABASE_URL = "sqlite:///./database.db"  # Example SQLite database URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Teacher model definition
class Teacher(Base):
    """Model representing a Teacher in the database."""
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Pydantic model for creating a Teacher
class TeacherCreate(BaseModel):
    """Schema for creating a new Teacher."""
    name: str
    email: str

class TeacherResponse(BaseModel):
    """Schema for the response after creating or retrieving a Teacher."""
    id: int
    name: str
    email: str

@app.post("/teachers", response_model=TeacherResponse)
def create_teacher(teacher: TeacherCreate):
    """
    Create a new Teacher record.

    - **name**: The name of the Teacher (required).
    - **email**: The email of the Teacher (required).
    
    Returns a JSON response confirming the creation of the Teacher record,
    including their Teacher ID, name, and email.
    
    Raises HTTPException if the email is already in use.
    """
    db = SessionLocal()
    existing_teacher = db.query(Teacher).filter(Teacher.email == teacher.email).first()
    if existing_teacher:
        raise HTTPException(status_code=400, detail="Email already in use.")
    
    new_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    
    return TeacherResponse(id=new_teacher.id, name=new_teacher.name, email=new_teacher.email)

@app.get("/teachers/{teacher_id}", response_model=TeacherResponse)
def get_teacher(teacher_id: int):
    """
    Retrieve a Teacher's information by ID.

    - **teacher_id**: The ID of the Teacher to retrieve.
    
    Returns a JSON object containing the Teacher's details, including 
    their ID, name, and email.

    Raises HTTPException if the Teacher is not found.
    """
    db = SessionLocal()
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found.")
    
    return TeacherResponse(id=teacher.id, name=teacher.name, email=teacher.email)
```