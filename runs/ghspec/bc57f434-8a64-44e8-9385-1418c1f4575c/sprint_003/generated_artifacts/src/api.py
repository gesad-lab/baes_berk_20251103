```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from your_application.database import get_db  # Update import based on your structure
from your_application.models import Course  # Assuming you have a Course model

app = FastAPI()

class CourseCreate(BaseModel):
    name: str
    level: str

class CourseResponse(BaseModel):
    id: int
    name: str
    level: str

@app.post("/courses", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    """Create a new course with the given name and level."""
    if not course.name or not course.level:
        raise HTTPException(
            status_code=400,
            detail={"error": {"code": "E001", "message": "Both name and level must be provided."}}
        )
    new_course = Course(name=course.name, level=course.level)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

@app.get("/courses/{course_id}", response_model=CourseResponse)
def get_course(course_id: int, db: Session = Depends(get_db)):
    """Retrieve details of a specific course by ID."""
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(
            status_code=404,
            detail={"error": {"code": "E002", "message": "Course not found."}}
        )
    return course
```