```python
from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Course
from typing import List

router = APIRouter()

@router.delete("/courses/{course_id}", status_code=204)
async def delete_course(course_id: int, db: Session = Depends(get_db)):
    """
    Delete a course by its ID.

    Args:
        course_id (int): The ID of the course to be deleted.
        db (Session): Database session dependency.

    Raises:
        HTTPException: If the course does not exist.

    Returns:
        None: Executes a successful deletion, returning a 204 status code.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": {"code": "E404", "message": "Course not found."}}
        )

    db.delete(course)
    db.commit()
```