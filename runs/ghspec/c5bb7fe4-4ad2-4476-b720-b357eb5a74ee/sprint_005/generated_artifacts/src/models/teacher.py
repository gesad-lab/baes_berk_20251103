```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Teacher(db.Model):
    """Model representing a teacher in the system."""
    
    __tablename__ = 'teachers'  # Specify the table name

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Auto-incrementing primary key
    name = db.Column(db.String, nullable=False)  # Teacher's name, required field
    email = db.Column(db.String, nullable=False, unique=True)  # Teacher's email, required and must be unique

    def __init__(self, name: str, email: str) -> None:
        """Initialize a Teacher instance.

        Args:
            name (str): The name of the teacher.
            email (str): The email of the teacher.
        """
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        """Return a string representation of the Teacher instance."""
        return f"<Teacher id={self.id}, name={self.name}, email={self.email}>"

    def to_dict(self) -> dict:
        """Convert the Teacher instance to a dictionary representation.

        Returns:
            dict: A dictionary containing teacher details.
        """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }
```