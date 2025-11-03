from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

class Student(db.Model):
    """Model for the Student entity."""
    
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each student
    name = db.Column(db.String(100), nullable=False)  # Name of the student, required field

    def __init__(self, name: str):
        """Initialize a new Student instance.

        Args:
            name (str): The name of the student.
        """
        self.name = name

    def to_dict(self) -> dict:
        """Convert the Student instance to a dictionary for JSON serialization.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        return {
            'id': self.id,
            'name': self.name
        }