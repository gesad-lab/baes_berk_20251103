```python
from datetime import datetime
from src import db

class Course(db.Model):
    """Course model to represent a course entity in the database."""
    
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)  # Title of the course
    description = db.Column(db.Text, nullable=True)  # Description of the course
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp when the course was created

    def __repr__(self):
        """Return a string representation of the Course model."""
        return f'<Course {self.title}>'
```