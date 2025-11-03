```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr
from typing import List

# Initialize FastAPI application
app = FastAPI()

# SQLite database setup
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define Student model
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# Create the database schema
def init_db():
    Base.metadata.create_all(bind=engine)

# Call the function to create the database.
init_db()

# Pydantic model for creating a new student
class StudentCreate(BaseModel):
    name: constr(strip_whitespace=True, min_length=1)  # input sanitization with constraints

# Endpoint to create a new student
@app.post("/students", response_model=StudentCreate)
async def create_student(student: StudentCreate):
    # Open a new database session
    db = SessionLocal()
    try:
        # Create a new student instance
        db_student = Student(name=student.name)
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student
    except Exception as e:
        # Raise HTTP exception in case of an error
        raise HTTPException(status_code=400, detail="Could not create student: " + str(e))
    finally:
        db.close()

# Endpoint to retrieve all students
@app.get("/students", response_model=List[StudentCreate])
async def get_students():
    # Open a new database session
    db = SessionLocal()
    try:
        students = db.query(Student).all()
        return students
    except Exception as e:
        # Raise HTTP exception in case of an error
        raise HTTPException(status_code=500, detail="Could not retrieve students: " + str(e))
    finally:
        db.close()
```