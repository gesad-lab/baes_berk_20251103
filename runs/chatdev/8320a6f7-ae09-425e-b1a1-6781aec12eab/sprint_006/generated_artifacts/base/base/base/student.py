'''
Defines the SQLAlchemy model for the Student entity.
'''
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # Added email field
# Create the new table with the email field
Base.metadata.create_all(engine)