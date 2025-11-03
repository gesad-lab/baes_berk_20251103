```python
from fastapi import APIRouter, HTTPException, status
from src.models import Teacher  # Import the Teacher model
from src.db import get_db_session  # Import the function to get the database session

router = APIRouter()

@router.get("/teachers/{teacher_id}", response_model=Teacher)
async def get_teacher(teacher_id: int):
    """
    Retrieve details of a specific Teacher by their unique identifier.

    Args:
        teacher_id (int): The unique identifier of the Teacher.

    Raises:
        HTTPException: If the Teacher with the provided id is not found.

    Returns:
        Teacher: The Teacher object containing id, name, and email.
    """
    session = get_db_session()  # Get a database session
    try:
        teacher = session.query(Teacher).filter(Teacher.id == teacher_id).first()
        if teacher is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Teacher with id {teacher_id} not found"
            )
        return teacher
    except Exception as e:
        # Log the exception for debugging purposes
        print(f"Error retrieving teacher with id {teacher_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
    finally:
        session.close()  # Ensure session is closed after the operation
```