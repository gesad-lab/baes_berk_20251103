```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from app.database import Course, SessionLocal
from app.models import Base

app = FastAPI()

# Pydantic model for Course input validation
class CourseCreate(BaseModel):
    name: str
    level: str

class CourseResponse(BaseModel):
    id: int
    name: str
    level: str

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/courses", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = next(get_db())):
    if not course.name or not course.level:
        raise HTTPException(status_code=400, detail="Both name and level are required fields.")
        
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    
    return db_course

@app.get("/courses", response_model=List[CourseResponse])
def get_all_courses(db: Session = next(get_db())):
    courses = db.query(Course).all()
    return courses
```