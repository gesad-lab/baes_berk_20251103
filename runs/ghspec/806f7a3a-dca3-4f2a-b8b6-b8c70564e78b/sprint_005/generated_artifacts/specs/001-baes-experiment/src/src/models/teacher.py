```python
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Initialize the database
db = SQLAlchemy()

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'  # Name of the database table

    id = Column(Integer, primary_key=True, autoincrement=True)  # Primary Key
    name = Column(String, nullable=False)  # Teacher's name
    email = Column(String, nullable=False, unique=True)  # Teacher's email, must be unique

    def __repr__(self):
        return f"<Teacher(id={self.id}, name={self.name}, email={self.email})>"
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Validates the email format"""
        import re
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

# Exception for invalid teacher operations
class TeacherError(Exception):
    """Custom exception for Teacher-related errors"""
    pass

def create_teacher(name: str, email: str) -> Teacher:
    """Create a new Teacher and return the instance.

    Args:
        name (str): Name of the teacher.
        email (str): Email of the teacher.

    Returns:
        Teacher: The created Teacher instance.

    Raises:
        TeacherError: If the operation fails.
    """
    if not name or not email:
        raise TeacherError("Both name and email are required.")  # Validate inputs

    if not Teacher.validate_email(email):
        raise TeacherError("Invalid email format.")  # Validate email format
        
    new_teacher = Teacher(name=name, email=email)  # Create Teacher instance
    db.session.add(new_teacher)  # Add to session
    db.session.commit()  # Commit to database
    return new_teacher  # Return new Teacher instance

def get_teacher_by_id(teacher_id: int) -> Teacher:
    """Retrieve a Teacher by their ID.

    Args:
        teacher_id (int): The ID of the Teacher.

    Returns:
        Teacher: The Teacher instance if found.

    Raises:
        TeacherError: If the teacher is not found.
    """
    teacher = Teacher.query.get(teacher_id)  # Querying using the primary key
    if not teacher:
        raise TeacherError(f"Teacher with ID {teacher_id} not found.")
    return teacher  # Return the found Teacher instance
```