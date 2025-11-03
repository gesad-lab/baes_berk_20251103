from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

# Create a base class for declarative models
Base = declarative_base()

class Student(Base):
    """Represents a Student entity in the database."""
    
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        """Return a string representation of the Student object."""
        return f"<Student(id={self.id}, name='{self.name}')>"

    @staticmethod
    def create_student(session, name):
        """
        Create a new student record in the database.
        
        Parameters:
        - session: The database session to use for the transaction.
        - name: The name of the student to create.
        
        Returns:
        - A tuple containing the success message and the created student object.
        Raises:
        - ValueError: If the name is empty.
        - IntegrityError: If there is an issue with the database.
        """
        if not name:
            raise ValueError("Student name cannot be empty.")
        
        new_student = Student(name=name)
        session.add(new_student)
        try:
            session.commit()  # Commit the transaction
            return {"message": "Student record created successfully.", "student": new_student}
        except IntegrityError:
            session.rollback()  # Rollback the transaction in case of error
            raise IntegrityError("Failed to create a student record due to a database integrity error.")

# Database setup
def init_db(database_url):
    """Initialize the database with the Student table."""
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)()  # Return a new session to interact with the database

# This file should set up the database connection and model for student records.
# Ensure to handle exceptions and maintain a clean transaction state during operations.