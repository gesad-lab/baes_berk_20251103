```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from typing import List, Optional

# Database configuration, creating an SQLite engine
DATABASE_URL = "sqlite:///./students.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class StudentModel(Base):
    """SQLAlchemy model representing a student."""
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# Pydantic schema for creating a new student
class StudentCreate(BaseModel):
    """Schema for creating a new student."""
    name: str

# Pydantic schema for the response returned when creating a student
class StudentResponse(BaseModel):
    """Schema for the student response."""
    id: int
    name: str

    class Config:
        orm_mode = True

# Pydantic schema for retrieving a list of students
class StudentsListResponse(BaseModel):
    """Schema for a list of students."""
    students: List[StudentResponse]

# Create the database tables if they don't exist already
def init_db():
    """Initialize the database and create tables."""
    Base.metadata.create_all(bind=engine)
```
