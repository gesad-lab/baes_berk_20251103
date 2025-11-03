from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Create FastAPI application
app = FastAPI()

# Setup SQLite database connection
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create SQLAlchemy base model
Base = declarative_base()

# Define Student model
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# Create database tables
Base.metadata.create_all(bind=engine)

# Define request model for creating a student
class StudentCreate(BaseModel):
    name: constr(min_length=1, max_length=100)  # Validating name length

# Dependency to get database session
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/students", response_model=StudentCreate)
def create_student(student: StudentCreate, db: Session = next(get_db())):
    """Create a new student."""
    # Create a new student instance and add to the database
    db_student = Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get("/students/{student_id}", response_model=StudentCreate)
def read_student(student_id: int, db: Session = next(get_db())):
    """Retrieve a student by ID."""
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# Error handling for requests without a name
@app.exception_handler(ValueError)
def value_error_exception_handler(request, exc):
    return HTTPException(status_code=400, detail=str(exc))