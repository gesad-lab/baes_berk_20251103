```python
from src.models import db, Teacher  # Importing the Teacher model
from flask_sqlalchemy import SQLAlchemy

# Initialize the database connection
db = SQLAlchemy()

def init_db(app):
    """Initialize the database with the application."""
    db.init_app(app)
    
    with app.app_context():
        # Create all tables including the new Teacher table
        db.create_all()

        # Add constraints for the Teacher entity
        if not db.engine.has_table('teacher'):
            db.create_all()

class Teacher(db.Model):
    """Model representing a teacher in the system."""
    
    __tablename__ = 'teacher'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Required field
    email = db.Column(db.String(100), nullable=False, unique=True)  # Required and unique field

    def __repr__(self):
        return f"<Teacher(id={self.id}, name='{self.name}', email='{self.email}')>"
```