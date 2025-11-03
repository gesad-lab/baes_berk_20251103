```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from typing import List

app = FastAPI()
Base = declarative_base()

# Define the Teacher model
class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

# Pydantic model for teacher creation
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr

# Dependency to get the database session
# (Assuming you have setup for SQLAlchemy session)
def get_db():
    # Acquire and return the database session here
    ...

@app.post("/teachers", status_code=201)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    # Validate that the teacher with the same email doesn't already exist
    existing_teacher = db.query(Teacher).filter(Teacher.email == teacher.email).first()
    if existing_teacher:
        raise HTTPException(status_code=400, detail="Email already registered: E001")

    new_teacher = Teacher(name=teacher.name, email=teacher.email)
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    
    return new_teacher

@app.get("/teachers", response_model=List[Teacher])
def get_teachers(db: Session = Depends(get_db)):
    # Retrieve a list of all teachers
    return db.query(Teacher).all()
```