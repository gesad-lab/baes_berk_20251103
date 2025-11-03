from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """Represents a student record in the database."""

    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New email field added
    
    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', email='{self.email}')>"


def create_student(session, name: str, email: str):
    """
    Create a new student record in the database.

    Parameters:
    - session: SQLAlchemy session object
    - name: Name of the student
    - email: Email of the student (validated before calling this function)

    Returns:
    - The newly created student object
    """
    new_student = Student(name=name, email=email)
    session.add(new_student)
    session.commit()
    session.refresh(new_student)  # Fetch the newly generated ID and other fields
    return new_student


def update_student_email(session, student_id: int, email: str):
    """
    Update the email address of an existing student record.

    Parameters:
    - session: SQLAlchemy session object
    - student_id: ID of the student to update
    - email: New email address for the student

    Returns:
    - Updated student object if the update was successful, otherwise None
    """
    student = session.query(Student).filter(Student.id == student_id).first()
    if student:
        student.email = email
        session.commit()
        session.refresh(student)
        return student
    return None

# Note: The above functions can be tested to ensure they work as expected with validation elsewhere.