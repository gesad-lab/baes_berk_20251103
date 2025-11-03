```python
from app import db

class Course(db.Model):
    """Course model to represent a course entity in the system."""
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)  # The name of the course, must be provided
    level = db.Column(db.String, nullable=False)  # The level of the course, must be provided

    def __repr__(self):
        """Representation of the Course object."""
        return f'<Course id={self.id} name={self.name} level={self.level}>'
```