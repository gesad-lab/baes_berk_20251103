```python
from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy database instance
db = SQLAlchemy()

class Course(db.Model):
    """Course model to represent educational courses in the system."""
    
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each course
    name = db.Column(db.String, nullable=False)    # Name of the course
    level = db.Column(db.String, nullable=False)   # Level of the course (e.g., Beginner, Intermediate, Advanced)

    def __repr__(self):
        """Return a string representation of the Course object."""
        return f'<Course id={self.id} name={self.name} level={self.level}>'
```