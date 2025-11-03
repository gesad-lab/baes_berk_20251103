'''
Migration script to add Course table and student_courses association table to the database.
'''
from sqlalchemy import Column, String, Integer, Table, ForeignKey
from sqlalchemy.orm import Session
from models import Course, student_courses
def upgrade(db: Session):
    # Create the Course table if it does not exist
    Course.__table__.create(bind=db.bind, checkfirst=True)
    # Create the association table for students and courses
    student_courses.create(bind=db.bind, checkfirst=True)
def downgrade(db: Session):
    # Drop the association table if needed
    student_courses.drop(bind=db.bind, checkfirst=True)
    # Drop the Course table if needed
    Course.__table__.drop(bind=db.bind, checkfirst=True)