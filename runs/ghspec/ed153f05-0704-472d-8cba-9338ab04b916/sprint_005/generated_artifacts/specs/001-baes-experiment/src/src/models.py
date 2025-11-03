```python
# src/models.py

from src.database import db

class Teacher(db.Model):
    """Define the Teacher model for the database."""
    
    __tablename__ = 'teachers'  # Set the table name
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    name = db.Column(db.String, nullable=False)  # Teacher's name, must not be null
    email = db.Column(db.String, nullable=False, unique=True)  # Teacher's email, must be unique and not null

    def __repr__(self):
        """Represent the Teacher model as a string."""
        return f"<Teacher id={self.id} name={self.name} email={self.email}>"
```