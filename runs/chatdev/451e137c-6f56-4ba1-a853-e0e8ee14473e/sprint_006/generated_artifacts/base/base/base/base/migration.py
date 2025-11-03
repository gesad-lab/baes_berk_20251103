'''
Migration script to add email column to the Student table.
'''
from sqlalchemy import Column, String
from sqlalchemy.orm import Session
from models import Student
def upgrade(db: Session):
    # Add email column to the Student table
    with db.begin():
        db.execute('ALTER TABLE students ADD COLUMN email STRING NOT NULL')
def downgrade(db: Session):
    # Downgrade logic if needed
    pass