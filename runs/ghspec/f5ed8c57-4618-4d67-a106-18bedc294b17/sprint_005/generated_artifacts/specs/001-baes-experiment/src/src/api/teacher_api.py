```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import Teacher  # Import the Teacher model
import logging

# Setup logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/teachers", response_model=Teacher)
def create_teacher(teacher: Teacher, db: Session = Depends(get_db)):
    """
    Create a new Teacher entity in the database.

    Args:
        teacher (Teacher): The teacher entity to be created.
        db (Session): The database session.

    Returns:
        Teacher: The created teacher entity.
    
    Raises:
        HTTPException: If the teacher could not be created.
    """
    # Log the incoming request
    logger.info(f"Creating teacher: {teacher.email}")
    
    # Check if the teacher already exists in the system
    existing_teacher = db.query(Teacher).filter(Teacher.email == teacher.email).first()
    if existing_teacher:
        logger.error(f"Teacher with email {teacher.email} already exists.")
        raise HTTPException(status_code=400, detail="Teacher with this email already exists.")
    
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    
    # Log successful creation
    logger.info(f"Teacher created: {teacher.email}")
    return teacher

@router.get("/teachers/{teacher_id}", response_model=Teacher)
def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a teacher entity by ID.

    Args:
        teacher_id (int): The ID of the teacher to retrieve.
        db (Session): The database session.

    Returns:
        Teacher: The requested teacher entity.

    Raises:
        HTTPException: If the teacher is not found.
    """
    logger.info(f"Retrieving teacher with ID: {teacher_id}")
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    
    if teacher is None:
        logger.error(f"Teacher with ID {teacher_id} not found.")
        raise HTTPException(status_code=404, detail="Teacher not found.")
    
    logger.info(f"Teacher retrieved: {teacher.email}")
    return teacher

@router.put("/teachers/{teacher_id}", response_model=Teacher)
def update_teacher(teacher_id: int, updated_teacher: Teacher, db: Session = Depends(get_db)):
    """
    Update an existing teacher entity by ID.

    Args:
        teacher_id (int): The ID of the teacher to update.
        updated_teacher (Teacher): The updated teacher data.
        db (Session): The database session.

    Returns:
        Teacher: The updated teacher entity.

    Raises:
        HTTPException: If the teacher is not found or cannot be updated.
    """
    logger.info(f"Updating teacher with ID: {teacher_id}")
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    
    if teacher is None:
        logger.error(f"Teacher with ID {teacher_id} not found.")
        raise HTTPException(status_code=404, detail="Teacher not found.")
    
    for key, value in updated_teacher.dict(exclude_unset=True).items():
        setattr(teacher, key, value)

    db.commit()
    db.refresh(teacher)

    logger.info(f"Teacher updated: {teacher.email}")
    return teacher

@router.delete("/teachers/{teacher_id}")
def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    """
    Delete a teacher entity by ID.

    Args:
        teacher_id (int): The ID of the teacher to delete.
        db (Session): The database session.

    Raises:
        HTTPException: If the teacher is not found.
    """
    logger.info(f"Deleting teacher with ID: {teacher_id}")
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()

    if teacher is None:
        logger.error(f"Teacher with ID {teacher_id} not found.")
        raise HTTPException(status_code=404, detail="Teacher not found.")
    
    db.delete(teacher)
    db.commit()

    logger.info(f"Teacher deleted with ID: {teacher_id}")
    return {"detail": "Teacher deleted successfully."}
```