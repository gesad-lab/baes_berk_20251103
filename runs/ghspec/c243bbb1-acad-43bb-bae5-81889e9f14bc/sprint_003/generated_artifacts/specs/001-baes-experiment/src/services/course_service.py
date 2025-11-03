```python
# services/course_service.py

from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer
from sqlalchemy.exc import IntegrityError
from flask import jsonify
from pydantic import BaseModel, ValidationError
from typing import List
import os

# Create a SQLite database engine
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///courses.db')
engine = create_engine(DATABASE_URL)
metadata = MetaData(bind=engine)

# Course table definition
courses_table = Table('courses', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String, nullable=False),
    Column('level', String, nullable=False)
)

# Create the courses table on startup if it does not exist
def create_courses_table():
    metadata.create_all(engine)

class Course(BaseModel):
    name: str
    level: str

def create_course(course_data: dict) -> dict:
    """Create a new course and return its data."""
    try:
        # Validate input using Pydantic
        course = Course(**course_data)

        # Insert the new course into the database
        with engine.connect() as connection:
            result = connection.execute(courses_table.insert().values(
                name=course.name,
                level=course.level
            ))
            course_id = result.inserted_primary_key[0]

        return {"message": "Course created successfully", "course": {"id": course_id, "name": course.name, "level": course.level}}

    except IntegrityError:
        return {"error": {"code": "E001", "message": "Course with this name already exists."}}, 400
    except ValidationError as e:
        # Return validation error details
        return {"error": {"code": "E002", "message": "Invalid input", "details": e.errors()}}, 400
    except Exception as e:
        # General error handling
        return {"error": {"code": "E003", "message": "An unexpected error occurred", "details": str(e)}}, 500

def get_courses() -> List[dict]:
    """Retrieve all courses from the database."""
    with engine.connect() as connection:
        result = connection.execute(courses_table.select())
        courses = [{"id": row['id'], "name": row['name'], "level": row['level']} for row in result]
    return courses
```