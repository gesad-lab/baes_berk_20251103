'''
Migration script to add Teacher table to the database.
Preserves existing Student and Course data.
'''
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Session
from models import Teacher
def upgrade(db: Session):
    # Create the Teacher table if it does not exist
    # This operation will not affect existing Student and Course data
    Teacher.__table__.create(bind=db.bind, checkfirst=True)
def downgrade(db: Session):
    # Drop the Teacher table if needed
    # This operation will not affect existing Student and Course data
    Teacher.__table__.drop(bind=db.bind, checkfirst=True)