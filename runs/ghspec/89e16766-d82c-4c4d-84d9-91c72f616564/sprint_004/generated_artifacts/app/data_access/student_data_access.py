```python
# app/data_access/student_data_access.py

from flask_sqlalchemy import SQLAlchemy
from app.models import Student, Course, StudentCourse
from sqlalchemy.exc import IntegrityError, NoResultFound

db = SQLAlchemy()

class StudentDataAccess:
    """Data Access Layer for Student Course Association"""

    @staticmethod
    def associate_courses(student_id: int, course_ids: list) -> dict:
        """
        Associate courses to a student.

        Args:
            student_id (int): The ID of the student.
            course_ids (list): A list of course IDs to associate.

        Returns:
            dict: Success message and updated student record.

        Raises:
            ValueError: If student ID or course IDs are invalid.
            Exception: If there is an error during the association process.
        """
        # Validate student existence
        student = Student.query.get(student_id)
        if not student:
            raise ValueError(f"Student with ID {student_id} does not exist.")

        # Validate course IDs and associate them
        for course_id in course_ids:
            course = Course.query.get(course_id)
            if not course:
                raise ValueError(f"Course with ID {course_id} does not exist.")
            association = StudentCourse(student_id=student_id, course_id=course_id)
            db.session.add(association)

        try:
            db.session.commit()
            return {
                "message": "Courses successfully associated with student.",
                "student": student.to_dict()  # Assuming a to_dict() method exists in Student model
            }
        except IntegrityError:
            db.session.rollback()
            raise Exception("Could not associate courses due to integrity constraints.")
        except Exception as e:
            db.session.rollback()
            raise Exception("An error occurred while associating courses.") from e

    @staticmethod
    def retrieve_student_with_courses(student_id: int) -> dict:
        """
        Retrieve a student record along with associated courses.

        Args:
            student_id (int): The ID of the student.

        Returns:
            dict: Student record with associated courses.

        Raises:
            ValueError: If student ID is invalid.
        """
        student = Student.query.get(student_id)
        if not student:
            raise ValueError(f"Student with ID {student_id} does not exist.")
        
        return {
            "student": student.to_dict(),  # Assuming a to_dict() method exists in Student model
            "courses": [course.to_dict() for course in student.courses]  # Assuming a relationship 'courses' exists
        }
```