```python
# src/repositories.py

from sqlalchemy.orm import Session
from models import Course, Teacher
from sqlalchemy.exc import NoResultFound

class CourseRepository:
    """Repository class to manage Course data operations."""

    def __init__(self, session: Session):
        self.session = session

    def assign_teacher_to_course(self, course_id: int, teacher_id: int) -> Course:
        """
        Assign a teacher to a course.

        :param course_id: ID of the course to assign a teacher to.
        :param teacher_id: ID of the teacher to be assigned.
        :return: Updated Course object with assigned teacher.
        :raises NoResultFound: If either the course or the teacher does not exist.
        """
        # Find the course
        course = self.session.query(Course).filter_by(id=course_id).one_or_none()
        if course is None:
            raise NoResultFound(f"Course with id {course_id} not found.")

        # Find the teacher
        teacher = self.session.query(Teacher).filter_by(id=teacher_id).one_or_none()
        if teacher is None:
            raise NoResultFound(f"Teacher with id {teacher_id} not found.")

        # Assign the teacher to the course
        course.teacher_id = teacher_id
        self.session.commit()  # Save changes to the database
        return course

    def remove_teacher_from_course(self, course_id: int) -> Course:
        """
        Remove the teacher assignment from a course.

        :param course_id: ID of the course from which to remove the teacher.
        :return: Updated Course object with teacher assignment removed.
        :raises NoResultFound: If the course does not exist.
        """
        # Find the course
        course = self.session.query(Course).filter_by(id=course_id).one_or_none()
        if course is None:
            raise NoResultFound(f"Course with id {course_id} not found.")

        # Remove the teacher assignment
        course.teacher_id = None
        self.session.commit()  # Save changes to the database
        return course

    def get_course_teacher(self, course_id: int) -> Teacher:
        """
        Get the teacher assigned to a course.

        :param course_id: ID of the course to get the teacher for.
        :return: Teacher object assigned to the course.
        :raises NoResultFound: If the course or assigned teacher does not exist.
        """
        # Find the course
        course = self.session.query(Course).filter_by(id=course_id).one_or_none()
        if course is None:
            raise NoResultFound(f"Course with id {course_id} not found.")

        if course.teacher_id is None:
            raise NoResultFound(f"No teacher assigned to course with id {course_id}.")

        # Find the teacher using the teacher_id from the course
        teacher = self.session.query(Teacher).filter_by(id=course.teacher_id).one_or_none()
        if teacher is None:
            raise NoResultFound(f"Teacher assigned to course with id {course_id} not found.")

        return teacher
```