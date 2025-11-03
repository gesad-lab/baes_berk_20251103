```python
# src/database.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the database instance
db = SQLAlchemy()

def init_db():
    """Initialize the database and apply migrations."""
    with db.app.app_context():
        try:
            # Create all tables and apply migrations
            db.create_all()
            apply_migrations()
        except SQLAlchemyError as e:
            # Log the detailed error context for debugging, but don't expose to the user
            print(f"Error initializing database: {e}")

def apply_migrations():
    """Apply the necessary schema changes to accommodate the new teacher relationship in courses."""
    # Migration for adding teacher_id to the Course table
    with db.engine.connect() as connection:
        # Start a transaction
        trans = connection.begin()
        try:
            # Execute migration commands to alter the Course table
            connection.execute('''
                ALTER TABLE Course
                ADD COLUMN teacher_id UUID REFERENCES Teacher(id) ON DELETE SET NULL
            ''')
            # Commit the transaction
            trans.commit()
        except SQLAlchemyError as e:
            # Rollback in case of error
            trans.rollback()
            print(f"Error applying migrations: {e}")
            raise  # Re-raise exception after logging

# Add any additional methods related to database management here if necessary
```