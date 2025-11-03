```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import IntegrityError
from fastapi.responses import JSONResponse

DATABASE_URL = "sqlite:///./test.db"  # Use your database URL here
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()


# Teacher model
class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

Base.metadata.create_all(bind=engine)


# Pydantic schema for Teacher creation
class TeacherCreate(BaseModel):
    name: str
    email: EmailStr


@app.post("/api/v1/teachers", response_model=TeacherCreate)
async def create_teacher(teacher: TeacherCreate, db: Session = Depends(SessionLocal)):
    """
    Create a new Teacher.

    Args:
    - teacher (TeacherCreate): The data to create a new teacher.
    - db (Session): Database session dependency.

    Returns:
    - TeacherCreate: The created teacher data including id.
    """
    new_teacher = Teacher(name=teacher.name, email=teacher.email)

    try:
        # Add teacher to the database
        db.add(new_teacher)
        db.commit()
        db.refresh(new_teacher)
        return JSONResponse(status_code=201, content={"id": new_teacher.id, "name": new_teacher.name, "email": new_teacher.email})
    except IntegrityError:
        db.rollback()  # Rollback changes on error
        # Check if the error is due to email uniqueness
        raise HTTPException(status_code=400, detail={"error": {"code": "E002", "message": "Email already registered."}})
    except Exception as e:
        db.rollback()  # Rollback changes on unexpected error
        raise HTTPException(status_code=500, detail={"error": {"code": "E003", "message": str(e)}})


@app.get("/api/v1/teachers/{teacher_id}", response_model=TeacherCreate)
async def get_teacher(teacher_id: int, db: Session = Depends(SessionLocal)):
    """
    Retrieve a Teacher by ID.

    Args:
    - teacher_id (int): The ID of the teacher to retrieve.
    - db (Session): Database session dependency.

    Returns:
    - TeacherCreate: The teacher data.
    """
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail={"error": {"code": "E004", "message": "Teacher not found."}})

    return {"id": teacher.id, "name": teacher.name, "email": teacher.email}
```