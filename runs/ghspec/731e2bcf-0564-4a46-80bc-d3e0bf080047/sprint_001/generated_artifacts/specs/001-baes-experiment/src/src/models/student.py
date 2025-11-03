```python
from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy database instance
db = SQLAlchemy()

class Student(db.Model):
    """Model representing a student in the database."""
    
    __tablename__ = 'students'  # Define the table name for SQLAlchemy

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Primary key, auto-incrementing
    name = db.Column(db.String, nullable=False)  # Student's name, required field

    def __repr__(self):
        """Return a string representation of the Student instance."""
        return f"<Student id={self.id} name={self.name}>"
```