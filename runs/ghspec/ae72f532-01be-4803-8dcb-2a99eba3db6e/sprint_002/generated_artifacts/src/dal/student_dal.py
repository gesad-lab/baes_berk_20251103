# src/dal/student_dal.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from models.student import Student
from database import engine

# Create a new session for interacting with the database
Session = sessionmaker(bind=engine)

def create_student(name: str, email: str) -> Student:
    """
    Create a new student in the database.

    Parameters:
    - name (str): The name of the student.
    - email (str): The email of the student.

    Returns:
    - Student: The created student entity.
    
    Raises:
    - ValueError: If the name or email is invalid.
    """
    # Input validation
    if not name.strip():
        raise ValueError("Student name is required.")
    if not email.strip():
        raise ValueError("Student email is required.")

    # Create a new instance of Student
    new_student = Student(name=name, email=email)

    # Start a new session to add the student
    with Session() as session:
        try:
            session.add(new_student)
            session.commit()
            # Return the created student
            return new_student
        except IntegrityError:
            session.rollback()
            raise ValueError("A student with this email already exists.")

def get_all_students() -> list:
    """
    Retrieve all students from the database.

    Returns:
    - list: A list of all student entities.
    """
    with Session() as session:
        return session.query(Student).all()

def get_student_by_id(student_id: int) -> Student:
    """
    Retrieve a student by their ID.

    Parameters:
    - student_id (int): The ID of the student.

    Returns:
    - Student: The student entity if found.

    Raises:
    - ValueError: If no student with that ID exists.
    """
    with Session() as session:
        student = session.query(Student).filter_by(id=student_id).first()
        if not student:
            raise ValueError(f"No student found with ID: {student_id}.")
        return student

def update_student(student_id: int, name: str, email: str) -> Student:
    """
    Update an existing student's information.

    Parameters:
    - student_id (int): The ID of the student to update.
    - name (str): The new name for the student.
    - email (str): The new email for the student.

    Returns:
    - Student: The updated student entity.

    Raises:
    - ValueError: If the name or email is invalid or the student does not exist.
    """
    # Input validation
    if not name.strip():
        raise ValueError("Student name is required.")
    if not email.strip():
        raise ValueError("Student email is required.")

    with Session() as session:
        student = session.query(Student).filter_by(id=student_id).first()
        if not student:
            raise ValueError(f"No student found with ID: {student_id}.")

        # Update student fields
        student.name = name
        student.email = email
        
        try:
            session.commit()
            return student
        except IntegrityError:
            session.rollback()
            raise ValueError("A student with this email already exists.")