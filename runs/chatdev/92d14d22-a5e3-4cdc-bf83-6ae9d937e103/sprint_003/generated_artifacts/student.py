'''
Migration script to add Course table to the database.
'''
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
# Create the Course table
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
# Create all tables, preserving existing Student data
Base.metadata.create_all(bind=engine)