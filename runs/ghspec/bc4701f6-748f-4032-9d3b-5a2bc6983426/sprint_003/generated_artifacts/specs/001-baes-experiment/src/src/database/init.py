```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Base model class for SQLAlchemy
Base = declarative_base()

# Database setup
engine = create_engine('sqlite:///app.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Course model definition
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)  # Create all tables, including Course

# API FastAPI instance
app = FastAPI()

# Pydantic model for the Course
class CourseModel(BaseModel):
    id: int
    name: str
    level: str

    class Config:
        orm_mode = True

# Retrieve a course by ID
@app.get("/courses/{id}", response_model=CourseModel)
def get_course(id: int):
    db = SessionLocal()
    try:
        course = db.query(Course).filter(Course.id == id).first()
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")
        return course
    finally:
        db.close()
```