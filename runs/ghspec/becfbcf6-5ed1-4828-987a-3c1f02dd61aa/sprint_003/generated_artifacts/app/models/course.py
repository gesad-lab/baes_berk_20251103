```python
from app import db

class Course(db.Model):
    """Represents a course entity in the application.

    Attributes:
        id (int): Unique identifier for the course.
        name (str): The title of the course (required).
        level (str): The difficulty level of the course (required).
    """
    
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Course {self.name} - Level: {self.level}>'
```