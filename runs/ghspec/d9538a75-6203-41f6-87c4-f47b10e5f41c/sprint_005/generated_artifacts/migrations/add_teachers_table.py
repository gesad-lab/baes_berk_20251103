import os
from flask_sqlalchemy import SQLAlchemy

# Assuming the db object has been created in the main application code
db = SQLAlchemy()

class Teacher(db.Model): 
    """Represents a teacher in the system."""
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Auto-incrementing ID
    name = db.Column(db.String, nullable=False)  # Teacher's name, required field
    email = db.Column(db.String, nullable=False, unique=True)  # Teacher's email, required and unique field

def upgrade(): 
    """Apply the migration to add the teachers table."""
    # Create the teachers table with necessary fields
    db.create_all()  # Create the tables if they do not exist
    db.session.commit()  # Commit the changes to the database

def downgrade(): 
    """Revert the migration by dropping the teachers table."""
    # Drop the teachers table if it exists
    db.drop_all()  # This will drop the teachers table along with other tables.
    db.session.commit()  # Commit the changes to revert the database state

if __name__ == "__main__": 
    # Ensure the script can be run standalone
    from app import app  # Import app object
    with app.app_context():  # Set up application context for operations
        upgrade()  # Run the upgrade function to apply the migration.