```python
from flask_sqlalchemy import SQLAlchemy

# Initialize the database instance
db = SQLAlchemy()

class Teacher(db.Model):
    """Model representing a teacher in the educational management system."""

    __tablename__ = 'teachers'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)  # Teacher's name, cannot be null
    email = db.Column(db.String, nullable=False, unique=True)  # Teacher's email, must be unique and cannot be null

    def __repr__(self):
        """Provide a string representation of the Teacher instance."""
        return f"<Teacher {self.name}, Email: {self.email}>"
```