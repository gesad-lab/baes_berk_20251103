'''
Database migration script to add email field to Student entity.
'''
from sqlalchemy import Column, String
from sqlalchemy.orm import Session
from models import Student
def upgrade(db: Session):
    # Add email column to the existing Student table as nullable first
    with db.begin():
        db.execute('ALTER TABLE students ADD COLUMN email VARCHAR')
    # Optionally, update existing records with a default value or handle them accordingly
    # db.execute('UPDATE students SET email = "default@example.com" WHERE email IS NULL')
    # Then, if you want to enforce NOT NULL, you can do it in a separate migration step
    # db.execute('ALTER TABLE students ALTER COLUMN email SET NOT NULL')
def downgrade(db: Session):
    # Logic to remove the email column if needed
    pass