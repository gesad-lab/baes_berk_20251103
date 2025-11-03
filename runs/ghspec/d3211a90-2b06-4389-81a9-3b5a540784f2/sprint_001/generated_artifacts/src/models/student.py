from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Define the base class for declarative models
Base = declarative_base()

class Student(Base):
    """Represent a student entity in the database."""
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Required field for student name
    
    def __repr__(self):
        """Return a string representation of the Student object."""
        return f"<Student(id={self.id}, name='{self.name}')>"

    @classmethod
    def create(cls, session, name: str):
        """Create a new Student instance and add it to the session.

        Parameters:
            session: SQLAlchemy session to interact with the database.
            name (str): The name of the student.

        Returns:
            Student: The created Student instance.
        """
        student = cls(name=name)
        session.add(student)
        session.commit()  # Commit the session to save changes
        return student
    
    @classmethod
    def retrieve(cls, session, student_id: int):
        """Retrieve a Student instance by ID.

        Parameters:
            session: SQLAlchemy session to interact with the database.
            student_id (int): The ID of the student to retrieve.

        Returns:
            Student: The retrieved Student instance or None if not found.
        """
        return session.query(cls).filter(cls.id == student_id).first()  # Return the student or None if not found