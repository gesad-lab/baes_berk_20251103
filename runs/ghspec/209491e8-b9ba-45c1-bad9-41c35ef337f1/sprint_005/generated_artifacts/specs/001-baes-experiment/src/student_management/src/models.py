from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'

    # Unique identifier for the teacher
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Name of the teacher
    name = Column(String, nullable=False)

    # Email of the teacher
    email = Column(String, nullable=False)

    def __repr__(self):
        return f"<Teacher(id={self.id}, name={self.name}, email={self.email})>"