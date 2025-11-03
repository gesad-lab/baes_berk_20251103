```python
# src/models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Course(db.Model):
    """Represents a Course in the student management system."""

    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)  # Course Name (required)
    level = db.Column(db.String, nullable=False)  # Course Level (required)

    def __repr__(self):
        return f"<Course(name={self.name}, level={self.level})>"

    def as_dict(self):
        """Convert Course object to dictionary format for JSON serialization."""
        return {
            'name': self.name,
            'level': self.level
        }
```