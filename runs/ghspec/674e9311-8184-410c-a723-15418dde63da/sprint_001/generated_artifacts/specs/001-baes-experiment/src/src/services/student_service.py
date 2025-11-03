```python
from typing import List, Dict
from sqlalchemy.orm import Session
from models.student import Student
from sqlalchemy.exc import IntegrityError

class StudentService:
    """Service layer for managing students in the application."""

    @staticmethod
    def create_student(db: Session, name: str) -> Dict:
        """Create a new student with the specified name.

        Args:
            db (Session): The database session object.
            name (str): The name of the student to create.

        Returns:
            A dictionary containing the created student's information.

        Raises:
            ValueError: If the provided name is empty or invalid.
            IntegrityError: If the student cannot be created due to database constraints.
        """
        # Validate input
        if not name or not isinstance(name, str):
            raise ValueError("Name is required and must be a valid string.")

        # Create the student instance
        new_student = Student(name=name)

        # Attempt to add the student to the database
        try:
            db.add(new_student)
            db.commit()
            db.refresh(new_student)  # Refresh to obtain any auto-generated fields
            return {"id": new_student.id, "name": new_student.name}
        except IntegrityError:
            db.rollback()  # Rollback in case of failure
            raise ValueError("Failed to create student due to a database error.")

    @staticmethod
    def get_all_students(db: Session) -> List[Dict]:
        """Retrieve all students from the database.

        Args:
            db (Session): The database session object.

        Returns:
            A list of dictionaries containing student information.
        """
        students = db.query(Student).all()
        return [{"id": student.id, "name": student.name} for student in students]
```