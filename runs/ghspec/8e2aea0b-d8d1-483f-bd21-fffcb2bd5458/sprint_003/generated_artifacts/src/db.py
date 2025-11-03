```python
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the database connection
db = SQLAlchemy()

class Course(db.Model):
    """Represents a course in the system."""
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(50), nullable=False)

def init_db():
    """Initialize the database and create tables if they do not exist."""
    with db.app.app_context():
        # Check if the courses table already exists
        if not db.engine.dialect.has_table(db.engine, 'courses'):
            try:
                # Create all tables including the new courses table
                db.create_all()
            except IntegrityError as e:
                # Log error or handle error if needed, but do not quit
                print(f"Error during database migration: {str(e)}")
        else:
            print("Courses table already exists. No migration necessary.")

# Call this function from your application entry point (e.g., in app.py)
# This should be done when the app starts
# init_db()
```