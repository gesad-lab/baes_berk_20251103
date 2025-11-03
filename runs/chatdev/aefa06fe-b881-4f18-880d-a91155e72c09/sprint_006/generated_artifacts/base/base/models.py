'''
Defines the SQLAlchemy models for the Student and Course entities.
'''
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database import SessionLocal
Base = declarative_base()
# Association table for the many-to-many relationship
student_courses = Table('student_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # Add email field
    courses = relationship("Course", secondary=student_courses, back_populates="students")
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
    students = relationship("Student", secondary=student_courses, back_populates="courses")
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