```python
# /src/services/student_service.py

from models.student import Student
from models.course import Course
from database import get_db
from sqlalchemy.orm import Session
from fastapi import HTTPException

async def associate_course_with_student(student_id: int, course_id: int):
    """
    Associates a course with a student.

    Parameters:
    - student_id: The ID of the student to associate the course with.
    - course_id: The ID of the course to associate with the student.

    Returns:
    - A success message upon successful association of the course.
    
    Raises:
    - HTTPException: If the course_id is not valid.
    """
    async with get_db() as session:  # Ensure the database session is properly managed
        student = await session.get(Student, student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

        course = await session.get(Course, course_id)
        if not course:
            raise HTTPException(status_code=400, detail="Invalid course ID")

        # Add course ID to the student's course_ids list
        if student.course_ids is None:
            student.course_ids = []
        
        if course_id not in student.course_ids:
            student.course_ids.append(course_id)
            session.add(student)
            await session.commit()  # Commit the transaction
        return {"message": "Course successfully associated with student"}

async def get_student_courses(student_id: int):
    """
    Retrieves the courses associated with a student.

    Parameters:
    - student_id: The ID of the student whose courses are to be retrieved.

    Returns:
    - A list of course objects associated with the student.
    
    Raises:
    - HTTPException: If the student is not found.
    """
    async with get_db() as session:  # Ensure the database session is properly managed
        student = await session.get(Student, student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

        # Retrieve courses based on the course IDs stored in the student record
        courses = []
        if student.course_ids:
            courses = await session.query(Course).filter(Course.id.in_(student.course_ids)).all()
        
        return courses
```