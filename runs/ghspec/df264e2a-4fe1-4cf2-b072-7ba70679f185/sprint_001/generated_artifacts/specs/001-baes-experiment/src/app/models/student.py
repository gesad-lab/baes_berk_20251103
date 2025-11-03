from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

def init_db(engine):
    """Initialize the database schema using SQLAlchemy."""
    Base.metadata.create_all(bind=engine)  # Create tables defined by the Base models if they don't exist.