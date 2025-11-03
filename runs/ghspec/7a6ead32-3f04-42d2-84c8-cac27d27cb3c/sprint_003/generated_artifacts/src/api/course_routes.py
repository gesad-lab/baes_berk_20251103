```python
from fastapi import FastAPI, HTTPException, Body, Depends
from sqlalchemy.orm import Session
from models import Course, get_db

app = FastAPI()

@app.put("/api/v1/courses/{id}", response_model=Course)
async def update_course(id: int, course: Course = Body(...), db: Session = Depends(get_db)):
    """
    Update an existing Course by ID.

    Parameters:
    - id: The unique identifier of the Course to update.
    - course: The Course data containing the updated name and level.

    Returns:
    - The updated Course details on success.

    Raises:
    - HTTPException with 400 status code if validation fails.
    - HTTPException with 404 status code if Course with the given ID does not exist.
    """
    # Validate request data
    if not course.name or not course.level:
        raise HTTPException(
            status_code=400,
            detail={"error": {"code": "E001", "message": "Name and level are required."}}
        )

    # Fetch the existing course from the database
    existing_course = db.query(Course).filter(Course.id == id).first()
    if not existing_course:
        raise HTTPException(status_code=404, detail="Course not found.")

    # Update course details
    existing_course.name = course.name
    existing_course.level = course.level

    # Commit the changes to the database
    db.commit()
    db.refresh(existing_course)

    # Return updated course details
    return existing_course
```