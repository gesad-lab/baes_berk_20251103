```python
from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

class Course(db.Model):
    """Course model representing a course in the database."""
    
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)  # Course identifier
    name = db.Column(db.String, nullable=False)    # Course name, required field
    level = db.Column(db.String, nullable=False)    # Course level, required field

    def __repr__(self):
        """Return a string representation of the Course instance."""
        return f'<Course {self.name} (Level: {self.level})>'

def init_db(app):
    """Initialize the database with the app context."""
    with app.app_context():
        db.init_app(app)  # Initialize the database with the app
        db.create_all()   # Create all database tables, including 'courses'

def migrate_add_courses_table():
    """Migration function to add the 'courses' table."""
    # Actual migration logic should be implemented here
    # This could involve checking the existence of the 'courses' table
    # and creating it while ensuring no data loss to existing tables
    pass
```