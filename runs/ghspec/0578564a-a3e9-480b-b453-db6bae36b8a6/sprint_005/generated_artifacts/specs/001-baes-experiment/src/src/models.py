```python
# src/models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Teacher(db.Model):
    """Represents a teacher entity in the system."""
    
    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=255), nullable=False)
    email = db.Column(db.String(length=255), nullable=False, unique=True)

    def __init__(self, name: str, email: str) -> None:
        """
        Initializes a new Teacher instance.

        Parameters:
        - name (str): The name of the teacher.
        - email (str): The email address of the teacher.
        """
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        """String representation of the Teacher model."""
        return f"<Teacher id={self.id}, name={self.name}, email={self.email}>"
```