```python
from fastapi import FastAPI, HTTPException, Path
from sqlalchemy.orm import Session
from .models import Course, Teacher, get_db  # Assuming get_db is a dependency for database session

app = FastAPI()

@app.get("/courses/{course_id}", response_model=dict)
def get_course(course_id: int, db: Session = Depends(get_db)):
    """
    Retrieve the details of a specific course, including the assigned teacher's details.

    Args:
        course_id (int): The ID of the course to retrieve.
        db (Session): Database session dependency.

    Returns:
        dict: Course details including teacher's name and email.

    Raises:
        HTTPException: 404 Not Found if the course does not exist.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Prepare the course response with teacher info if assigned
    course_details = {
        "course_id": course.id,
        "course_name": course.name,
        "teacher": {
            "name": course.teacher.name if course.teacher else None,
            "email": course.teacher.email if course.teacher else None
        } if course.teacher else None
    }
    return course_details
```