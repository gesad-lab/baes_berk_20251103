from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    
    # Adding foreign key relationship to the Teacher model
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)
    
    # Relationship to easily access the associated teacher's information
    teacher = relationship("Teacher")  # relationship back to Teacher

    def __repr__(self):
        return f"<Course(id={self.id}, title={self.title}, teacher_id={self.teacher_id})>"