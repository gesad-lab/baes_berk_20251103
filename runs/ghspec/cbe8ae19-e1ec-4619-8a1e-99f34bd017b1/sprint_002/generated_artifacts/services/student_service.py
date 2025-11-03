```python
from models import Student, db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

def get_student_by_id(student_id: int) -> dict:
    """Retrieve a student record by ID including their email.

    Args:
        student_id (int): The unique identifier of the student.

    Returns:
        dict: A dictionary containing student ID, name, and email.
        
    Raises:
        ValueError: If no student is found with the given ID.
    """
    student = db.session.query(Student).get(student_id)  # Fetch the student by ID
    
    if not student:
        raise ValueError(f"No student found with ID {student_id}")  # Raise an error if not found

    # Return student data including email
    return {
        "id": student.id,
        "name": student.name,
        "email": student.email  # Include email in the response
    }

def add_student(name: str, email: str) -> dict:
    """Add a new student record.

    Args:
        name (str): The name of the student.
        email (str): The email of the student (must be unique).

    Returns:
        dict: A dictionary containing the newly created student's ID, name, and email.

    Raises:
        ValueError: If email is not valid or already exists.
    """
    # Validate email format (basic validation for the purpose of this example)
    if not isinstance(email, str) or "@" not in email:
        raise ValueError("Invalid email format")
    
    # Create a new student instance
    new_student = Student(name=name, email=email)

    try:
        db.session.add(new_student)    # Add the student to the session
        db.session.commit()             # Commit the session to save the student
    except IntegrityError:
        db.session.rollback()           # Rollback the session on error
        raise ValueError("Email already exists")  # Raise a meaningful error if email is duplicated

    return {
        "id": new_student.id,
        "name": new_student.name,
        "email": new_student.email
    }

def get_all_students() -> list:
    """Retrieve all student records including their email.

    Returns:
        list: A list of dictionaries containing student IDs, names, and emails.
    """
    students = db.session.query(Student).all()  # Fetch all students
    return [{
        "id": student.id,
        "name": student.name,
        "email": student.email  # Include email in each student's response
    } for student in students]
```