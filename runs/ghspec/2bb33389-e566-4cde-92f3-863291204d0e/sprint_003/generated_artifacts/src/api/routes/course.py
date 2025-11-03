```python
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Course  # Assuming Course model is defined in src/models.py

router = APIRouter()

@router.get("/courses", response_model=list[Course])  # Assuming Course has a proper Pydantic model
def get_courses(db: Session = Depends(get_db)):
    """
    Retrieve a list of all courses.

    Args:
        db (Session): The database session.
    
    Returns:
        list[Course]: A list of courses containing their IDs, names, and levels.
    
    Raises:
        HTTPException: If there is an error fetching courses.
    """
    try:
        courses = db.query(Course).all()  # Fetch all courses from the database
        return courses
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")  # Log or handle error appropriately

# Make sure to add this router to the main app in your FastAPI application setup
```
