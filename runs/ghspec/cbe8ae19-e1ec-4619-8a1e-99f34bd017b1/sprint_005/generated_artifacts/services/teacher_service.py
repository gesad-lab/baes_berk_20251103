```python
from models import db, Teacher  # Import the Teacher model for database interaction
from sqlalchemy.exc import IntegrityError  # Import IntegrityError for handling database constraints

def create_teacher(name: str, email: str) -> Teacher:
    """
    Creates a new teacher entry in the database.
    
    Parameters:
        name (str): The name of the teacher. Must be a non-empty string.
        email (str): The email of the teacher. Must be in a valid email format.

    Returns:
        Teacher: The newly created Teacher object.

    Raises:
        ValueError: If the name is empty or the email format is invalid.
        IntegrityError: If a teacher with the same email already exists.

    """
    if not name:
        raise ValueError("Name cannot be empty (E001: Invalid input).")
    if not isinstance(email, str) or "@" not in email:  # Simple email validation
        raise ValueError("Email format is invalid (E002: Invalid email format).")
    
    # Create a new Teacher instance
    new_teacher = Teacher(name=name, email=email)
    
    # Add the new teacher to the session and commit
    try:
        db.session.add(new_teacher)
        db.session.commit()
    except IntegrityError:  # Handle cases where a teacher with the same email already exists
        db.session.rollback()
        raise ValueError("A teacher with this email already exists (E003: Duplicate email).")
    
    return new_teacher

def get_all_teachers() -> list:
    """
    Retrieves all teacher records from the database.

    Returns:
        list: A list of Teacher objects.

    """
    teachers = Teacher.query.all()  # Query to retrieve all teacher records
    return teachers
```