```python
# /src/services/teacher_service.py

from models.teacher import Teacher  # Importing the Teacher model
from database import SessionLocal  # Importing the database session factory
from sqlalchemy.orm import Session
from fastapi import HTTPException

async def create_teacher(name: str, email: str) -> Teacher:
    """Creates a new teacher record in the database.

    Args:
        name (str): The name of the teacher.
        email (str): The email address of the teacher.

    Returns:
        Teacher: The created Teacher object.

    Raises:
        HTTPException: If there's a database error or validation failure.
    """
    if not name or not email:  # Validate input
        raise HTTPException(status_code=400, detail="Name and email are required.")

    # Creating a new Teacher instance
    new_teacher = Teacher(name=name, email=email)

    # Persisting to the database
    try:
        with SessionLocal() as db:  # Ensuring we handle the session lifecycle
            db.add(new_teacher)
            db.commit()  # Committing the transaction
            db.refresh(new_teacher)  # Refreshing to get the updated instance
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error creating teacher: {}".format(str(e)))

    return new_teacher


async def get_teacher_by_id(teacher_id: int) -> Teacher:
    """Retrieves a teacher record by its ID.

    Args:
        teacher_id (int): The ID of the teacher to retrieve.

    Returns:
        Teacher: The Teacher object corresponding to the ID.

    Raises:
        HTTPException: If the teacher is not found or there's a database error.
    """
    try:
        with SessionLocal() as db:
            teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
            if teacher is None:
                raise HTTPException(status_code=404, detail="Teacher not found.")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error retrieving teacher: {}".format(str(e)))

    return teacher
```