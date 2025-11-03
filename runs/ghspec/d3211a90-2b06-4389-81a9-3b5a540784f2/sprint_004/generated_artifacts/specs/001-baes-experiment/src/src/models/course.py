```python
# src/models/course.py

"""
Course Model

This module defines the Course entity as part of the application.

Functional Requirements:
1. **Course Association**: The application allows users to associate multiple Course entities with a Student entity using student ID and an array of course IDs. On successful association, the application returns a confirmation message indicating the successful linking of courses to the student.

2. **Retrieve Student Details**: Users can retrieve a Student entity by its ID along with all associated Course IDs. The response returns the Student's name, email, and an array of Course IDs.

3. **Database Schema Update**: The database schema has been updated to establish a many-to-many relationship between Students and Courses. This involves a new junction table `student_courses` which contains `student_id` and `course_id`, with a migration ensuring no data loss.

4. **JSON Response Format**: All API responses related to student-course associations are in valid JSON format, including appropriate status codes and messages for errors.

Success Criteria:
- Enables association of multiple courses with a student, providing confirmation responses with details of associated courses.
- Fetches student details along with associated courses, returning accurate JSON responses.
- Handles non-existent student associations, delivering clear error messages.
- Updates the schema to include a junction table without losing data, maintaining integrity.

Assumptions:
- Users accessing the application are familiar with web interfaces and functionality in course management.
"""

from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Junction table to establish many-to-many relationship
student_courses = Table(
    'student_courses',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

class Course(Base):
    """
    Model representing a Course.

    Attributes:
        id (int): The unique identifier for the course.
        name (str): The name of the course.
        level (str): The level of the course (e.g., beginner, intermediate).
    """

    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    # Establishing the relationship to Student through the junction table
    students = relationship('Student', secondary=student_courses, back_populates='courses')
```