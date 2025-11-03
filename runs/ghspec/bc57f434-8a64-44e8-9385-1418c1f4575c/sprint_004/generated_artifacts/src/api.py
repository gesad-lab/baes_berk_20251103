```python
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .database import get_db
from .models import StudentCourse, Course  # Assuming StudentCourse model is defined in models.py
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/students/{id}/courses", response_description="List of courses for a student")
async def get_student_courses(id: int, db: Session = Depends(get_db)):
    """
    Retrieve a list of courses a student is enrolled in.

    :param id: The ID of the student.
    :param db: The database session.
    :return: JSON response with list of courses.
    """
    # Fetch student courses using a join table
    courses = db.query(Course).join(StudentCourse).filter(StudentCourse.student_id == id).all()

    if not courses:
        raise HTTPException(status_code=404, detail="No courses found for the provided student ID.")

    # Return the list of courses in JSON format
    return JSONResponse(content={"courses": [course.to_dict() for course in courses]})

# Assumed to have a to_dict method in Course model to serialize it to dict
```