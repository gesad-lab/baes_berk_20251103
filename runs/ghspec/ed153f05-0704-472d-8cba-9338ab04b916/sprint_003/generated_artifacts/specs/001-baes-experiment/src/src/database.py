```python
from src.database import db

class Course(db.Model):
    """Model representing a Course in the database."""
    
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for the course
    name = db.Column(db.String, nullable=False)    # Name of the course, required field
    level = db.Column(db.String, nullable=False)   # Level of the course, required field

    def __repr__(self):
        """Return a string representation of the Course object."""
        return f"<Course {self.id}: {self.name} ({self.level})>"
```