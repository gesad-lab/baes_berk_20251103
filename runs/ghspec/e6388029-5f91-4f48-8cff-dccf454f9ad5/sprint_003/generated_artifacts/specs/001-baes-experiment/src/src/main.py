```python
from fastapi import FastAPI, HTTPException, Depends
from src.models import Course  # Importing the Course model
from sqlalchemy.orm import Session
from src.database import get_db

app = FastAPI()

@app.delete("/courses/{course_id}", status_code=204)
async def delete_course(course_id: int, db: Session = Depends(get_db)):
    """
    Delete a course by its ID.

    Parameters:
    - course_id: int - The ID of the course to delete.

    Returns:
    - 204 No Content: If the deletion was successful.
    
    Raises:
    - HTTPException: If the course ID does not exist.
    """
    course = db.query(Course).filter(Course.id == course_id).first()  # Fetch course by ID
    if not course:
        # If course is not found, raise a 404 error
        raise HTTPException(status_code=404, detail="Course not found.")
    
    db.delete(course)  # Perform deletion
    db.commit()  # Commit the transaction
```