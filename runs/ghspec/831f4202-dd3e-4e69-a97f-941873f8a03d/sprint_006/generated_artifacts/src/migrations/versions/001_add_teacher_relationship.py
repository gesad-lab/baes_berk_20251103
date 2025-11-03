```python
# src/migrations/versions/001_add_teacher_relationship.py

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from src.database import Base

class Course(Base):
    __tablename__ = 'courses'  # Table name in the database

    id = Column(Integer, primary_key=True, index=True)  # Primary key
    title = Column(String, nullable=False)  # Course title (required)
    description = Column(String, nullable=True)  # Course description
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Link to a Teacher

    # Relationship to the Teacher model
    teacher = relationship("Teacher", back_populates="courses") 


class Teacher(Base):
    __tablename__ = 'teachers'  # Table name in the database

    id = Column(Integer, primary_key=True, index=True)  # Primary key
    name = Column(String, nullable=False)  # Teacher's name (required)
    email = Column(String, unique=True, nullable=False)  # Teacher's email (unique)

    # Relationship to the Course model
    courses = relationship("Course", back_populates="teacher") 


# Adding request/response examples for API functionality
def get_request_examples():
    """
    Provides example requests and expected responses for teacher assignments.
    """

    examples = {
        "assign_teacher": {
            "request": {
                "method": "POST",
                "url": "/api/courses/1/assign_teacher",
                "body": {
                    "teacher_id": 2  # ID of the teacher to assign
                }
            },
            "response": {
                "status": 200,
                "body": {
                    "message": "Teacher assigned successfully",
                    "course_id": 1,
                    "teacher_id": 2
                }
            }
        },
        "view_courses": {
            "request": {
                "method": "GET",
                "url": "/api/courses"
            },
            "response": {
                "status": 200,
                "body": [
                    {
                        "id": 1,
                        "title": "Mathematics",
                        "assigned_teacher": {
                            "id": 2,
                            "name": "John Doe"
                        }
                    },
                    {
                        "id": 2,
                        "title": "History",
                        "assigned_teacher": None  # No teacher assigned
                    }
                ]
            }
        },
        "update_teacher_assignment": {
            "request": {
                "method": "PUT",
                "url": "/api/courses/1/update_teacher",
                "body": {
                    "teacher_id": 3  # New teacher ID to assign
                }
            },
            "response": {
                "status": 200,
                "body": {
                    "message": "Teacher assignment updated",
                    "course_id": 1,
                    "new_teacher_id": 3
                }
            }
        },
        "handle_unassigned_courses": {
            "request": {
                "method": "GET",
                "url": "/api/courses/unassigned"
            },
            "response": {
                "status": 200,
                "body": [
                    {
                        "id": 2,
                        "title": "History",
                        "status": "Unassigned"
                    }
                ]
            }
        }
    }

    return examples
```