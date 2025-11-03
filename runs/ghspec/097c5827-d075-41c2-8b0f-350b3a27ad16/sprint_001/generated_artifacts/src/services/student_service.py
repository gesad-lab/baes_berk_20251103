```python
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from models import Student  # Assuming Student is defined in models.py
from database import get_db  # Assuming a function to get DB session

def retrieve_student(student_id: int) -> dict:
    """
    Retrieve a student from the database by ID.

    Parameters:
        student_id (int): The ID of the student to retrieve.

    Returns:
        dict: A dictionary containing the student's details, or an error message if not found.
    """
    # Obtain a new database session
    db: Session = get_db()
    
    try:
        # Attempt to retrieve the student by ID
        student = db.query(Student).filter(Student.id == student_id).one()
        # Return a dictionary representation of the student
        return {
            "id": student.id,
            "name": student.name
        }, 200  # HTTP 200 OK
    except NoResultFound:
        # If no student was found, raise a 404 error
        return {
            "error": {
                "code": "E404",
                "message": "Student not found."
            }
        }, 404  # HTTP 404 Not Found
    except Exception as e:
        # For any other exceptions, log the error (not shown here) and raise an appropriate error
        return {
            "error": {
                "code": "E500",
                "message": "An unexpected error occurred."
            }
        }, 500  # HTTP 500 Internal Server Error
```