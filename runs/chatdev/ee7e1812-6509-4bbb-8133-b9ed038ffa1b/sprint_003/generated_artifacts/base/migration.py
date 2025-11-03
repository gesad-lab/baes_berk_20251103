'''
Handles the database migration to add the email field to the Student entity.
'''
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker
from models import Student
from database import Base
def migrate():
    '''
    Applies the migration to add the email field to the Student entity.
    '''
    engine = create_engine("sqlite:///./students.db")
    Base.metadata.bind = engine
    Base.metadata.create_all(bind=engine)  # This will not drop existing data