```python
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the SQLAlchemy database object
db = SQLAlchemy()

class Teacher(db.Model):
    """Model representing a Teacher entity in the educational system."""
    
    __tablename__ = 'teachers'
    
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each teacher
    name = db.Column(db.String(100), nullable=False)  # Required teacher name
    email = db.Column(db.String(120), unique=True, nullable=False)  # Required unique email address
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for when the record was created
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Timestamp for record updates

    def __init__(self, name: str, email: str):
        """Initialize a new Teacher instance."""
        self.name = name
        self.email = email

    def __repr__(self):
        """Represent the Teacher object as a string."""
        return f'<Teacher {self.name} ({self.email})>'

    @staticmethod
    def create_teacher(name: str, email: str):
        """Create and persist a new Teacher to the database.
        
        Args:
            name (str): The name of the teacher.
            email (str): The email of the teacher.

        Returns:
            Teacher: The created Teacher object.

        Raises:
            ValueError: If name or email is missing.
            IntegrityError: If the email already exists in the database.
        """
        if not name or not email:
            raise ValueError("Both name and email are required fields.")
        
        new_teacher = Teacher(name=name, email=email)
        try:
            db.session.add(new_teacher)
            db.session.commit()
            return new_teacher
        except IntegrityError:
            db.session.rollback()
            raise ValueError("The email provided is already in use.")

    @staticmethod
    def get_teacher(teacher_id: int):
        """Retrieve a Teacher from the database by their ID.

        Args:
            teacher_id (int): The ID of the teacher to retrieve.

        Returns:
            Teacher: The Teacher object if found.

        Raises:
            ValueError: If no teacher with the given ID exists.
        """
        teacher = Teacher.query.get(teacher_id)
        if not teacher:
            raise ValueError("No teacher found with the provided ID.")
        return teacher
```