```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Database setup
DATABASE_URL = 'sqlite:///students.db'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# Create the database schema on startup
def init_db():
    Base.metadata.create_all(bind=engine)

# Pydantic model for request body
class StudentCreate(BaseModel):
    name: str = Field(..., description="The name of the student")

app = FastAPI(on_startup=[init_db])

@app.post("/students", response_model=StudentCreate)
async def create_student(student: StudentCreate):
    # Check if the name is provided
    if not student.name:
        raise HTTPException(
            status_code=400,
            detail={
                "error": {
                    "code": "E001",
                    "message": "Name is required."
                }
            }
        )
    # Create a new student instance
    new_student = Student(name=student.name)
    
    # Add the student to the session and commit
    with SessionLocal() as db:
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
    
    return new_student
```