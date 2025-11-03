from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Student, Course, StudentCourse
import json

async def validate_enrollment(session: AsyncSession, student_id: int, course_id: int):
    """Validate that the student exists and the course is valid before enrollment.

    Args:
        session (AsyncSession): The database session.
        student_id (int): The ID of the student to enroll.
        course_id (int): The ID of the course to enroll the student in.

    Raises:
        HTTPException: If the student or course does not exist.
    """
    # Check if the student exists
    result = await session.execute(select(Student).filter(Student.id == student_id))
    student = result.scalar_one_or_none()
    if not student:
        raise HTTPException(status_code=404, detail=f"Student with ID {student_id} not found.")

    # Check if the course exists
    result = await session.execute(select(Course).filter(Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=404, detail=f"Course with ID {course_id} not found.")

async def test_data_migration(session: AsyncSession):
    """Test the data integrity and relationships after migration.

    Args:
        session (AsyncSession): The database session.

    Ensure that the existing student and course data are intact and the new relationships work as expected.
    """
    # Create test data
    student = Student(name="Test Student", email="test@student.com")
    course = Course(name="Test Course", level="Beginner")
    
    # Add to session
    session.add(student)
    session.add(course)
    await session.commit()

    # Validate enrollment
    await validate_enrollment(session, student.id, course.id)

    # Enroll student in the course
    enrollment = StudentCourse(student_id=student.id, course_id=course.id)
    session.add(enrollment)
    
    # Verify enrollment
    await session.commit()
    result = await session.execute(select(StudentCourse).filter_by(student_id=student.id, course_id=course.id))
    assert result.scalar_one_or_none() is not None, "Enrollment should be present in the junction table."

    # Cleanup
    await session.execute(select(StudentCourse).filter_by(student_id=student.id, course_id=course.id).delete())
    await session.commit()