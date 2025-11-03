'''
Main application file for the FastAPI Student application.
'''
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student
from database import engine, get_db
from schemas import StudentCreate, StudentResponse
from fastapi.middleware.cors import CORSMiddleware
# Initialize FastAPI app
app = FastAPI()
# Allow CORS for the frontend application
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Create the database tables on startup
@app.on_event("startup")
def startup():
    '''
    Create the database tables when the application starts.
    '''
    import models
    models.Base.metadata.create_all(bind=engine)
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    '''
    Create a new student record in the database.
    '''
    db_student = Student(name=student.name, email=student.email)  # Added email field
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
@app.get("/students/", response_model=list[StudentResponse])
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''
    Retrieve a list of students from the database.
    '''
    students = db.query(Student).offset(skip).limit(limit).all()
    return students