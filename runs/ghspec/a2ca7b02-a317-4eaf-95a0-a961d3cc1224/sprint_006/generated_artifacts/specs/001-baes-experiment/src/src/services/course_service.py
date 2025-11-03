```python
# File: src/services/course_service.py

from fastapi import HTTPException
from db.database import Session
from models.course import Course
from models.teacher import Teacher
from validators.course_validator import validate_teacher_id

class CourseService:
    @staticmethod
    async def assign_teacher(course_id: str, teacher_data: dict):
        """
        Assign a teacher to a course.

        This method checks if the provided teacher ID exists, validates
        the course ID, and if the course is empty or allows an update,
        it assigns the teacher to the course.

        Parameters:
        - course_id (str): The ID of the course.
        - teacher_data (dict): Contains "teacher_id" key for the assignment.

        Raises:
        - HTTPException: If the teacher does not exist, if the course
                         does not exist, or if the assignment fails for any reason.

        Returns:
        - Course: The updated course object with the assigned teacher.
        """
        teacher_id = teacher_data.get("teacher_id")
        
        # Validate the teacher ID
        if not teacher_id:
            raise HTTPException(status_code=400, detail="Teacher ID is required.")
        
        # Check if the teacher exists
        with Session() as session:
            teacher = session.query(Teacher).filter(Teacher.id == teacher_id).first()
            if not teacher:
                raise HTTPException(status_code=404, detail="Teacher not found.")

            course = session.query(Course).filter(Course.id == course_id).first()
            if not course:
                raise HTTPException(status_code=404, detail="Course not found.")

            # Check if the course already has a teacher assigned
            if course.teacher_id is not None and course.teacher_id != teacher_id:
                return HTTPException(status_code=400, detail="This course already has a teacher assigned.")

            # Assign the teacher to the course
            course.teacher_id = teacher.id
            
            # Save changes to the database
            session.add(course)
            session.commit()
            session.refresh(course)

        return course

    @staticmethod
    async def get_course(course_id: str):
        """
        Retrieve course details with assigned teacher.

        Parameters:
        - course_id (str): The ID of the course.

        Raises:
        - HTTPException: If the course does not exist.

        Returns:
        - Course: The course object including teacher's name and email.
        """
        with Session() as session:
            course = session.query(Course).filter(Course.id == course_id).first()
            if not course:
                raise HTTPException(status_code=404, detail="Course not found.")

            # Include teacher's details if teacher is assigned
            if course.teacher_id is not None:
                teacher = session.query(Teacher).filter(Teacher.id == course.teacher_id).first()
                course.teacher_name = teacher.name if teacher else None
                course.teacher_email = teacher.email if teacher else None

        return course
```