```python
# src/models.py

from your_app import db  # Ensure to replace with the actual import path

class Teacher(db.Model):
    """Model representing a Teacher entity in the educational management system."""
    
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each teacher
    name = db.Column(db.String, nullable=False)    # Teacher's full name
    email = db.Column(db.String, nullable=False, unique=True)  # Teacher's email address, must be unique
    
    def __repr__(self):
        """Return a string representation of the Teacher instance."""
        return f"<Teacher(id={self.id}, name='{self.name}', email='{self.email}')>"
```