```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Course(db.Model):
    """Represents a course in the educational system."""
    
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each course
    name = db.Column(db.String, nullable=False)    # The name of the course
    level = db.Column(db.String, nullable=False)   # The educational level of the course

    def __repr__(self):
        return f'<Course {self.name}, Level {self.level}>'
```