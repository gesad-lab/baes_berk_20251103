```python
from typing import List, Optional
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from .models import Student  # Assuming Student model is defined in models.py
from .database import engine  # Assuming your engine is defined in database.py

# Create a session factory
Session = sessionmaker(bind=engine)

class StudentRepository:
    """Repository to manage student database operations."""
    
    def __init__(self):
        """Initialize the StudentRepository."""
        self.session = Session()

    def create_student(self, name: str) -> Student:
        """Save a new student record in the database.

        Args:
            name (str): The name of the student.

        Returns:
            Student: The created Student object.
        
        Raises:
            Exception: If an error occurs while saving the student.
        """
        new_student = Student(name=name)
        try:
            self.session.add(new_student)
            self.session.commit()
            return new_student
        except SQLAlchemyError as e:
            self.session.rollback()  # Rollback the session on error
            raise Exception("Error occurred while creating a new student.") from e
        finally:
            self.session.close()

    def get_student_by_id(self, student_id: int) -> Optional[Student]:
        """Retrieve a student by ID.

        Args:
            student_id (int): The ID of the student to retrieve.

        Returns:
            Optional[Student]: The Student object if found, otherwise None.
        
        Raises:
            Exception: If an error occurs while fetching the student.
        """
        try:
            student = self.session.query(Student).filter(Student.id == student_id).first()
            return student
        except SQLAlchemyError as e:
            raise Exception("Error occurred while retrieving the student by ID.") from e
        finally:
            self.session.close()

    def list_all_students(self) -> List[Student]:
        """Retrieve all students from the database.

        Returns:
            List[Student]: A list of all Student objects.
        
        Raises:
            Exception: If an error occurs while fetching the students.
        """
        try:
            students = self.session.query(Student).all()
            return students
        except SQLAlchemyError as e:
            raise Exception("Error occurred while listing all students.") from e
        finally:
            self.session.close()
```