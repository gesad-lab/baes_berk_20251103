```python
from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models import Teacher
from src.schemas import TeacherCreate  # Assuming schemas.py has been created

def create_teacher_service(teacher: TeacherCreate, session: Session):
    """Create a new Teacher entity in the database.
    
    Args:
        teacher (TeacherCreate): The teacher data containing name and email.
        session (Session): The database session to use.
        
    Returns:
        Teacher: The created Teacher entity.
        
    Raises:
        HTTPException: If name or email is missing.
    """
    if not teacher.name or not teacher.email:
        raise HTTPException(status_code=400, detail="Missing required fields: name and/or email")

    new_teacher = Teacher(name=teacher.name, email=teacher.email)
    session.add(new_teacher)
    session.commit()
    session.refresh(new_teacher)  # Ensures we return the new entity with any defaults set by the database
    return new_teacher


def get_teacher_service(teacher_id: int, session: Session):
    """Retrieve a Teacher entity by its unique identifier.
    
    Args:
        teacher_id (int): The ID of the teacher to retrieve.
        session (Session): The database session to use.
        
    Returns:
        Teacher: The Teacher entity with the specified ID.

    Raises:
        HTTPException: If the teacher is not found.
    """
    teacher = session.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher
```