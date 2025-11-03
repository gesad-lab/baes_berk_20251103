```python
# student_management/src/models.py

from src.database import db

class Student(db.Model):
    """Model representing a student."""
    
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)  # New required field for email

    def __repr__(self):
        """Return a string representation of the Student model."""
        return f'<Student {self.name}, Email: {self.email}>'
```