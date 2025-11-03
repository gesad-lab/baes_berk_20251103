from flask_migrate import Migrate, upgrade, downgrade
from models import db

# Migration script to add the Course table
def upgrade():
    """Create the courses table"""
    db.create_all()  # Create all tables, including the new Course table

def downgrade():
    """Drop the courses table"""
    # Drop only the courses table, preserving existing tables
    db.session.execute('DROP TABLE IF EXISTS courses')  # Avoid errors if the table doesn't exist
    db.session.commit()  # Commit the change to the database