from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.student import Student


async def create_student(name: str, db: AsyncSession) -> Student:
    """Create a new student in the database.

    Args:
        name (str): The name of the student.
        db (AsyncSession): The database session.

    Raises:
        ValueError: If the name is empty or invalid.

    Returns:
        Student: The created student object.
    """
    if not name:
        raise ValueError("Student name is required.")

    # Create a new student instance
    student = Student(name=name)

    # Add the student to the session and commit
    try:
        db.add(student)
        await db.commit()
        await db.refresh(student)  # Load the new student's data
        return student
    except Exception as e:
        # Handle specific exception types if necessary
        await db.rollback()  # Rollback in case of error
        raise RuntimeError("Could not create student") from e


async def retrieve_students(db: AsyncSession) -> list[Student]:
    """Retrieve all students from the database.

    Args:
        db (AsyncSession): The database session.

    Returns:
        list[Student]: A list of student objects.
    """
    result = await db.execute(select(Student))
    return result.scalars().all()  # Return the list of student instances