from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from models import Student, Base

# Initialize the FastAPI application
app = FastAPI()

# SQLite database connection settings
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup():
    # Create the database tables
    Base.metadata.create_all(bind=engine)

@app.post("/students/", response_model=Student)
def create_student(student: Student, db: Session = next(get_db())):
    try:
        db.add(student)
        db.commit()
        db.refresh(student)
        return student
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Student already exists")

@app.get("/students/{student_id}", response_model=Student)
def read_student(student_id: int, db: Session = next(get_db())):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# Tests will go here: tests/conduct_final_tests.py
