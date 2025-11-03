```python
from app import db

class Teacher(db.Model):
    """Model representing a Teacher entity."""
    
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)  # Required field
    email = db.Column(db.String, nullable=False, unique=True)  # Required field and must be unique

    def __repr__(self):
        return f"<Teacher {self.name} ({self.email})>"
```