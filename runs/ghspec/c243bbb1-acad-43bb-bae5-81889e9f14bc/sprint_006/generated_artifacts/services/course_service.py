```python
# services/course_service.py

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select, update
from sqlalchemy.exc import NoResultFound
from pydantic import BaseModel, conint
from typing import Optional

# Database setup - adjust connection as needed
DATABASE_URL = 'sqlite:///courses.db'
engine = create_engine(DATABASE_URL)
metadata = MetaData(bind=engine)

# Define the courses table structure
courses_table = Table('courses', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('teacher_id', Integer, nullable=True)  # Updated to include teacher_id
)

class CourseUpdate(BaseModel):
    """Model for updating course details."""
    teacher_id: conint(gt=0)  # Ensures teacher_id is a positive integer

async def associate_teacher(course_id: int, teacher_id: int) -> str:
    """
    Associates a teacher with a course.
    
    Args:
        course_id (int): The ID of the course to update.
        teacher_id (int): The ID of the teacher to associate with the course.

    Returns:
        str: Success message upon successful association.

    Raises:
        ValueError: If no course is found with the provided course_id.
    """
    # Begin a transaction
    with engine.connect() as connection:
        # Check if the course exists
        query = select(courses_table).where(courses_table.c.id == course_id)
        course = connection.execute(query).fetchone()
        
        if course is None:
            raise ValueError(f"No course found with ID {course_id}")

        # Update the course with the teacher ID
        update_query = (
            update(courses_table).
            where(courses_table.c.id == course_id).
            values(teacher_id=teacher_id)
        )
        connection.execute(update_query)

    return f"Course with ID {course_id} successfully updated with Teacher ID {teacher_id}."

async def get_course_details(course_id: int) -> dict:
    """
    Retrieves course details along with associated teacher information.

    Args:
        course_id (int): The ID of the course to retrieve.

    Returns:
        dict: A dictionary containing course details and teacher information, if present.

    Raises:
        ValueError: If no course is found with the provided course_id.
    """
    with engine.connect() as connection:
        query = select(courses_table).where(courses_table.c.id == course_id)
        course = connection.execute(query).fetchone()

        if course is None:
            raise ValueError(f"No course found with ID {course_id}")

        return {
            "id": course.id,
            "name": course.name,
            "teacher_id": course.teacher_id
        }
```