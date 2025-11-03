'''
Migration script to add Course table to the database.
'''
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Session
from models import Course
def upgrade(db: Session):
    # Create the Course table if it does not exist
    Course.__table__.create(bind=db.bind, checkfirst=True)
def downgrade(db: Session):
    # Drop the Course table if needed
    Course.__table__.drop(bind=db.bind, checkfirst=True)