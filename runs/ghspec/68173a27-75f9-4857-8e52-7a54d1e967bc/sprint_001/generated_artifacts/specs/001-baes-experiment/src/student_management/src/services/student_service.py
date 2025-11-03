```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

Base = declarative_base()

class Student(Base):
    """Represents a student entity."""
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

class StudentRepository:
    """Handles CRUD operations for Student entities."""

    def __init__(self, db: Session):
        self.db = db

    def create_student(self, name: str) -> Student:
        """Create a new student and add it to the database.

        Args:
            name (str): The name of the student.

        Returns:
            Student: The created student object.
        """
        new_student = Student(name=name)
        self.db.add(new_student)
        self.db.commit()
        self.db.refresh(new_student)
        return new_student

    def get_student(self, student_id: int) -> Student:
        """Retrieve a student by ID.

        Args:
            student_id (int): The ID of the student to retrieve.

        Returns:
            Student: The student object if found.

        Raises:
            NoResultFound: If no student with the given ID exists.
        """
        student = self.db.query(Student).filter(Student.id == student_id).first()
        if student is None:
            raise NoResultFound(f"Student with ID {student_id} not found.")
        return student

    def update_student(self, student_id: int, name: str) -> Student:
        """Update a student's name.

        Args:
            student_id (int): The ID of the student to update.
            name (str): The new name for the student.

        Returns:
            Student: The updated student object.

        Raises:
            NoResultFound: If no student with the given ID exists.
        """
        student = self.get_student(student_id)
        student.name = name
        self.db.commit()
        self.db.refresh(student)
        return student

    def delete_student(self, student_id: int) -> None:
        """Delete a student from the database.

        Args:
            student_id (int): The ID of the student to delete.

        Raises:
            NoResultFound: If no student with the given ID exists.
        """
        student = self.get_student(student_id)
        self.db.delete(student)
        self.db.commit()
```
