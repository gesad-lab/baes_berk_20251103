'''
Migration script to add Course table while preserving Student data.
'''
from sqlalchemy import create_engine, MetaData
from sqlalchemy.schema import CreateTable
from models import Course
engine = create_engine("sqlite:///./students.db")
metadata = MetaData(bind=engine)
# Create the Course table
with engine.connect() as connection:
    connection.execute(CreateTable(Course.__table__))