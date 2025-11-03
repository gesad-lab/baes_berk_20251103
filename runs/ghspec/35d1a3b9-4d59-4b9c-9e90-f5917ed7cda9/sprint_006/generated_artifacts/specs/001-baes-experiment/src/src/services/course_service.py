```python
# src/services/course_service.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.repository import Course, Teacher  # Import the Course and Teacher models
from fastapi import HTTPException
from sqlalchemy.exc import NoResultFound

class CourseService:
    """Service layer for course management."""

    def __init__(self, db: AsyncSession):
        """Initialize the CourseService with a database session."""
        self.db = db

    async def assign_teacher_to_course(self, course_id: int, teacher_id: int) -> Course:
        """
        Assign a teacher to a course.

        Parameters:
        - course_id: The ID of the course to assign the teacher to.
        - teacher_id: The ID of the teacher to be assigned.

        Returns:
        - The updated Course object with the assigned teacher.

        Raises:
        - HTTPException: If the course or teacher does not exist.
        """
        async with self.db.begin():
            # Fetch the course by ID
            course_query = select(Course).where(Course.id == course_id)
            course_result = await self.db.execute(course_query)
            course = course_result.scalar_one_or_none()

            if course is None:
                raise HTTPException(status_code=404, detail="Course not found")

            # Fetch the teacher by ID
            teacher_query = select(Teacher).where(Teacher.id == teacher_id)
            teacher_result = await self.db.execute(teacher_query)
            teacher = teacher_result.scalar_one_or_none()

            if teacher is None:
                raise HTTPException(status_code=404, detail="Teacher not found")

            # Assign the teacher to the course
            course.teacher_id = teacher_id
            return course

    async def get_course_with_teacher(self, course_id: int) -> Course:
        """
        Retrieve a course's details along with its assigned teacher.

        Parameters:
        - course_id: The ID of the course to retrieve.

        Returns:
        - The Course object with teacher information.

        Raises:
        - HTTPException: If the course does not exist.
        """
        async with self.db.begin():
            # Fetch course with related teacher
            course_query = select(Course).where(Course.id == course_id).options(selectinload(Course.teacher))
            course_result = await self.db.execute(course_query)
            course = course_result.scalar_one_or_none()

            if course is None:
                raise HTTPException(status_code=404, detail="Course not found")

            return course
```