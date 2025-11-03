```python
from app import db

class Teacher(db.Model):
    """Represents a Teacher entity in the system."""

    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each teacher
    name = db.Column(db.String(100), nullable=False)  # Teacher's name, required field
    email = db.Column(db.String(100), nullable=False, unique=True)  # Teacher's email, must be unique

    def __repr__(self):
        return f'<Teacher {self.name} - {self.email}>'
```