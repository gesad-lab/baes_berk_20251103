```python
from flask import jsonify, request
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Student, Base

# Set up the SQLite database
DATABASE_URL = "sqlite:///students.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Create the database tables if they do not exist
Base.metadata.create_all(engine)


def create_student(student_data):
    """Create a new student in the database.

    Args:
        student_data (dict): The data for the new student, must include 'name'.

    Returns:
        dict: Created student data with HTTP status code.
    """
    name = student_data.get('name')
    if not name:
        return {"error": {"code": "E001", "message": "Name is required."}}, 400

    session = Session()
    new_student = Student(name=name)
    
    try:
        session.add(new_student)
        session.commit()
        return jsonify(new_student.serialize()), 201  # Return created student data
    except IntegrityError:
        session.rollback()
        return {"error": {"code": "E002", "message": "Student already exists."}}, 409
    except Exception as e:
        session.rollback()
        return {"error": {"code": "E003", "message": str(e)}}, 500
    finally:
        session.close()


def get_student(student_id):
    """Retrieve a student by ID.

    Args:
        student_id (int): The ID of the student to retrieve.

    Returns:
        dict: Retrieved student data with HTTP status code.
    """
    session = Session()
    student = session.query(Student).filter(Student.id == student_id).first()
    
    if student is None:
        return {"error": {"code": "E004", "message": "Student not found."}}, 404
    
    return jsonify(student.serialize()), 200


def update_student(student_id, student_data):
    """Update an existing student by ID.

    Args:
        student_id (int): The ID of the student to update.
        student_data (dict): The updated data for the student.

    Returns:
        dict: Updated student data with HTTP status code.
    """
    name = student_data.get('name')
    if not name:
        return {"error": {"code": "E001", "message": "Name is required."}}, 400

    session = Session()
    student = session.query(Student).filter(Student.id == student_id).first()
    
    if student is None:
        return {"error": {"code": "E004", "message": "Student not found."}}, 404
    
    student.name = name
    session.commit()
    
    return jsonify(student.serialize()), 200


def delete_student(student_id):
    """Delete a student by ID.

    Args:
        student_id (int): The ID of the student to delete.

    Returns:
        dict: Success message with HTTP status code.
    """
    session = Session()
    student = session.query(Student).filter(Student.id == student_id).first()
    
    if student is None:
        return {"error": {"code": "E004", "message": "Student not found."}}, 404
    
    session.delete(student)
    session.commit()
    
    return {"message": "Student deleted successfully."}, 204
```