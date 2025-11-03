```python
# src/db.py

from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy database instance
db = SQLAlchemy()

class Teacher(db.Model):
    """Model for the Teacher entity."""
    __tablename__ = 'teachers'
    
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier
    name = db.Column(db.String, nullable=False)    # Teacher's name
    email = db.Column(db.String, nullable=False, unique=True)  # Teacher's email

def init_db():
    """Initialize the database and create tables."""
    with db.app.app_context():
        db.create_all()  # Create all tables
        # Additional migrations can be handled here if needed

def migrate_teachers_table():
    """Perform database migration to ensure the Teacher table exists without affecting existing data."""
    with db.app.app_context():
        # Check if the 'teachers' table already exists
        if not db.engine.dialect.has_table(db.engine, 'teachers'):
            db.create_all()  # Creates the 'teachers' table only if it does not exist

        # Confirm migration is successful (This can be replaced with logging or a more robust check)
        if db.engine.dialect.has_table(db.engine, 'teachers'):
            print("Migration successful: Teachers table added.")
        else:
            print("Migration failed: Teachers table not found.")
```