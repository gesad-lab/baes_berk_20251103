'''
Defines the SQLAlchemy models for the Student and Course entities.
'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from database import SessionLocal
Base = declarative_base()
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # Add email field
    def save(self):
        """Save the student instance to the database."""
        try:
            db = SessionLocal()
            db.add(self)
            db.commit()
            db.refresh(self)
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()
    @classmethod
    def get(cls, student_id):
        """Retrieve a student instance by ID."""
        try:
            db = SessionLocal()
            student = db.query(cls).filter(cls.id == student_id).first()
            return student
        except Exception as e:
            raise e
        finally:
            db.close()
class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    def save(self):
        """Save the course instance to the database."""
        try:
            db = SessionLocal()
            db.add(self)
            db.commit()
            db.refresh(self)
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()
    @classmethod
    def get(cls, course_id):
        """Retrieve a course instance by ID."""
        try:
            db = SessionLocal()
            course = db.query(cls).filter(cls.id == course_id).first()
            return course
        except Exception as e:
            raise e
        finally:
            db.close()