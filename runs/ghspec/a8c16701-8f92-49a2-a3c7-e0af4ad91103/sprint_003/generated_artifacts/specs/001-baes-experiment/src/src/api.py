```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.course import Course

app = FastAPI()

# Pydantic model for request validation
class CourseCreate(BaseModel):
    name: str
    level: str

class CourseResponse(BaseModel):
    id: int
    name: str
    level: str

# Create a new course
@app.post("/courses", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    if not course.name or not course.level:
        raise HTTPException(status_code=400, detail="Both name and level are required.")
    
    new_course = Course(name=course.name, level=course.level)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    
    return new_course

# Retrieve course information by ID
@app.get("/courses/{course_id}", response_model=CourseResponse)
def read_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found.")
    
    return course
```