```python
from sqlalchemy.orm import Session
from src.models import Teacher  # Import the Teacher model
from src.schemas import TeacherCreate  # Import the schema for teacher creation
from src.exceptions import ValidationError  # Import custom exception for validation errors
import re  # Regular expression module for email validation

def create_teacher(teacher: TeacherCreate, db: Session) -> Teacher:
    """
    Create a new teacher record in the database.

    Args:
        teacher (TeacherCreate): The teacher data containing name and email.
        db (Session): The database session.

    Returns:
        Teacher: The created Teacher instance.

    Raises:
        ValidationError: If the name or email is invalid.
    """
    # Validate the input for non-empty name
    if not teacher.name:
        raise ValidationError("E001: Name is required.")

    # Validate the email format
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    if not re.match(email_regex, teacher.email):
        raise ValidationError("E002: Invalid email format.")

    # Check for existing teacher with the same email
    existing_teacher = db.query(Teacher).filter(Teacher.email == teacher.email).first()
    if existing_teacher:
        raise ValidationError("E003: Email already in use.")

    # Create a new Teacher instance
    db_teacher = Teacher(name=teacher.name, email=teacher.email)

    # Add the new teacher to the session and commit to the database
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)

    return db_teacher
```