# main.py

from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel, EmailStr
from fastapi.middleware.cors import CORSMiddleware

# Database setup
DATABASE_URL = "sqlite:///courses.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# FastAPI setup
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define Teacher model
class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Pydantic model for creating a teacher
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr

# Pydantic model for returning teacher data
class TeacherResponse(BaseModel):
    id: int
    name: str
    email: str

# API Endpoint to create a new Teacher
@app.post("/teachers", response_model=TeacherResponse)
async def create_teacher(teacher: TeacherCreate):
    try:
        db = SessionLocal()
        new_teacher = Teacher(name=teacher.name, email=teacher.email)
        db.add(new_teacher)
        db.commit()
        db.refresh(new_teacher)
        return TeacherResponse(id=new_teacher.id, name=new_teacher.name, email=new_teacher.email)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error creating teacher: " + str(e))
    finally:
        db.close()

# API Endpoint to get teacher details by ID
@app.get("/teachers/{teacher_id}", response_model=TeacherResponse)
async def get_teacher(teacher_id: int):
    db = SessionLocal()
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    db.close()
    
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return TeacherResponse(id=teacher.id, name=teacher.name, email=teacher.email)