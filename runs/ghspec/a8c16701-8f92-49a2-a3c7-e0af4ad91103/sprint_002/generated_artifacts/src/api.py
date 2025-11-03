from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from src.models import Student, get_db  # Importing existing models and DB session
from src import migrations  # Assuming migrations handle the database setup

app = FastAPI()

# Update the request model to include email
class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Use EmailStr to enforce email format

# Update existing POST endpoint to accept email
@app.post("/students", response_model=Student)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)
    
    # Add the new student to the database
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    
    return db_student

# Update the GET endpoint to include email
@app.get("/students/{student_id}", response_model=Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    return db_student

# Make sure to run the migration at startup to incorporate the new email field
@app.on_event("startup")
def startup_event():
    migrations.run_migrations()  # Function should handle migrations as defined earlier