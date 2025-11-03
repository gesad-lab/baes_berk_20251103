```python
# File: src/database.py

from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

class Course(db.Model):
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    level = db.Column(db.String, nullable=False)

# Function to handle the migration that preserves existing data
def migrate_database():
    # Check if the 'courses' table already exists
    if not db.engine.dialect.has_table(db.engine, 'courses'):
        # Begin migration process
        with db.engine.begin() as conn:
            # Preserving existing data in other tables during the migration.
            # Here you can implement any specific logic needed to preserve data.
            try:
                # Create the 'courses' table
                Course.__table__.create(conn)
            except Exception as e:
                print(f"Error during migration: {e}")  # Log the error for debugging

# Call the migration function to ensure the database is up to date
def initialize_database(app):
    with app.app_context():
        db.create_all()  # Create all tables
        migrate_database()  # Run migration to preserve existing data
```