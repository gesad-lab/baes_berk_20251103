```python
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session

# Model Definitions
Base = declarative_base()

# Existing Student and Course models assumed to be defined already
# from models import Student, Course

class StudentCourses(Base):
    __tablename__ = 'student_courses'
    
    student_id = Column(ForeignKey('students.id'), primary_key=True, nullable=False)
    course_id = Column(ForeignKey('courses.id'), primary_key=True, nullable=False)
    
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

# Initialize FastAPI application
app = FastAPI()

# Database initialization
DATABASE_URL = "your_database_url_here"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Automatically create the new junction table on startup
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

# Enroll Student in Course
class EnrollRequest(BaseModel):
    course_id: str

@app.post("/students/{student_id}/enroll")
def enroll_student(student_id: int, enroll_request: EnrollRequest):
    db: Session = SessionLocal()
    try:
        # Check if the course exists - this should connect to your Course model
        course = db.query(Course).filter(Course.id == enroll_request.course_id).first()
        if not course:
            raise HTTPException(status_code=400, detail="Course not found")
        
        # Create enrollment association
        enrollment = StudentCourses(student_id=student_id, course_id=enroll_request.course_id)
        db.add(enrollment)
        db.commit()
        return JSONResponse(status_code=201, content={"student_id": student_id, "course_id": enroll_request.course_id})
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    finally:
        db.close()

# Retrieve Student's Enrolled Courses
@app.get("/students/{student_id}/courses", response_model=List[Course])
def get_student_courses(student_id: int):
    db: Session = SessionLocal()
    try:
        # Fetch the courses associated with the student
        enrolled_courses = db.query(Course).join(StudentCourses).filter(StudentCourses.student_id == student_id).all()
        return enrolled_courses  # Assume Course model is properly defined to serialize
        
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
        
    finally:
        db.close()
```