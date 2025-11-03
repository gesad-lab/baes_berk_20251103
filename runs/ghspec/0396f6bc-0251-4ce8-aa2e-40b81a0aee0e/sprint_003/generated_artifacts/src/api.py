```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr
from sqlalchemy.orm import Session
from models import Course, Base  # Assuming Course is imported from your models
from database import get_db  # Assuming you have a function to get DB session

app = FastAPI()

class CourseCreate(BaseModel):
    name: constr(strip_whitespace=True, min_length=1)  # Ensure name is non-empty and stripped of whitespace
    level: constr(strip_whitespace=True, min_length=1)  # Ensure level is non-empty and stripped of whitespace

@app.post("/courses")
def create_course(course: CourseCreate, db: Session = next(get_db())):
    """Create a new course with the given name and level."""
    # Validate that the inputs are correctly sanitized and prepared
    if not course.name or not course.level:
        raise HTTPException(status_code=400, detail="Both name and level must be provided.")

    new_course = Course(name=course.name, level=course.level)

    try:
        db.add(new_course)
        db.commit()
        db.refresh(new_course)
    except Exception as e:
        # Log exception for debugging (ensure sensitive data is not logged)
        # For simplicity, we're printing to console. Replace with proper logging in production.
        print(f"Error creating course: {e}")
        raise HTTPException(status_code=500, detail="Failed to create course.")

    return {"id": new_course.id, "name": new_course.name, "level": new_course.level}

@app.get("/courses/{course_id}")
def get_course(course_id: int, db: Session = next(get_db())):
    """Retrieve a course by its ID."""
    course = db.query(Course).filter(Course.id == course_id).first()
    
    if not course:
        raise HTTPException(status_code=404, detail="Course not found.")
    
    return {"id": course.id, "name": course.name, "level": course.level}
```