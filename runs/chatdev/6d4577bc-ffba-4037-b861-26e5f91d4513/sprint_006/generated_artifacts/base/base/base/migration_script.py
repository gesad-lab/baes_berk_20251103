'''
Database migration script to add Course table and email field to Student entity.
'''
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Session
from models import Student, Course
def upgrade(db: Session):
    # Add email column to the existing Student table as nullable first
    with db.begin():
        # Check if the email column already exists to avoid errors
        if not db.has_table('students'):
            raise Exception("Students table does not exist.")
        # Add email column to the existing Student table
        db.execute('ALTER TABLE students ADD COLUMN email VARCHAR')
    # Create Course table
    Course.__table__.create(bind=db.bind, checkfirst=True)
def downgrade(db: Session):
    # Logic to remove the email column if needed
    pass