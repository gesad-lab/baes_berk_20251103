'''
Main application file for the FastAPI backend.
'''
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db
from models import Student
from schemas import StudentCreate, StudentResponse
app = FastAPI()
# Create the database tables only if they do not exist
if not inspect(engine).has_table("students"):  # Updated to use inspect
    from database import Base
    Base.metadata.create_all(bind=engine)
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    '''
    Create a new student in the database.
    '''
    # Check if a student with the same name already exists
    existing_student = db.query(Student).filter(Student.name == student.name).first()
    if existing_student:
        raise HTTPException(status_code=400, detail="Student with this name already exists.")
    db_student = Student(name=student.name, email=student.email)  # Updated to include email
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return StudentResponse(id=db_student.id, name=db_student.name, email=db_student.email)  # Updated return statement
@app.get("/students/", response_model=list[StudentResponse])
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''
    Retrieve a list of students from the database.
    '''
    students = db.query(Student).offset(skip).limit(limit).all()
    return students