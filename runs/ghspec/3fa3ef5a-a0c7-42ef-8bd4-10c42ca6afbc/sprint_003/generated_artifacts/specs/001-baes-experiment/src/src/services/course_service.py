from sqlalchemy.orm import Session
from models.course import Course
from typing import List, Dict, Any
from sqlalchemy.exc import IntegrityError

class CourseService:
    """Service to handle business logic related to Course entities."""

    @staticmethod
    def create_course(db: Session, name: str, level: str) -> Dict[str, Any]:
        """
        Create a new course with the given name and level.

        Parameters:
        - db: Database session
        - name: Name of the course
        - level: Level of the course

        Returns:
        - A dictionary containing course details or an error message.
        """
        if not name or not level:
            return {"error": "Both name and level are required."}

        new_course = Course(name=name, level=level)

        try:
            db.add(new_course)
            db.commit()
            db.refresh(new_course)
            return {
                "message": "Course created successfully.",
                "course": {
                    "id": new_course.id,
                    "name": new_course.name,
                    "level": new_course.level
                }
            }
        except IntegrityError:
            db.rollback()
            return {"error": "Course with this name already exists."}
        except Exception as e:
            db.rollback()
            return {"error": f"An error occurred: {str(e)}"}

    @staticmethod
    def get_courses(db: Session) -> List[Dict[str, Any]]:
        """
        Retrieve all courses.

        Parameters:
        - db: Database session

        Returns:
        - A list of dictionaries containing course details.
        """
        courses = db.query(Course).all()
        return [
            {
                "id": course.id,
                "name": course.name,
                "level": course.level
            }
            for course in courses
        ]