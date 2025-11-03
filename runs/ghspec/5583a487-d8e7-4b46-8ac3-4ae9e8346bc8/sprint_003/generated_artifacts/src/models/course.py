```python
from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy instance
db = SQLAlchemy()

class Course(db.Model):
    """Course entity representing a course available for enrollment."""
    
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each course
    name = db.Column(db.String(100), nullable=False)  # Name of the course, required field
    level = db.Column(db.String(50), nullable=False)  # Level of the course, required field

    def __repr__(self):
        return f'<Course {self.name} - Level: {self.level}>'
```