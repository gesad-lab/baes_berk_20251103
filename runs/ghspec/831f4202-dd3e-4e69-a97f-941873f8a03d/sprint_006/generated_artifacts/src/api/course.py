```python
# src/api/course.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.database import get_db
from src.models import Course, Teacher

router = APIRouter()

@router.post("/courses/{course_id}/assign_teacher")
async def assign_teacher(course_id: int, teacher_id: int, db: AsyncSession = Depends(get_db)):
    """
    Assign a teacher to a course by its ID.

    Args:
        course_id (int): The ID of the course.
        teacher_id (int): The ID of the teacher to assign.

    Raises:
        HTTPException: If the course or teacher is not found.

    Returns:
        dict: Result message indicating success.
    """
    # Fetch the course from the database
    course_stmt = select(Course).where(Course.id == course_id)
    result = await db.execute(course_stmt)
    course = result.scalar_one_or_none()  # Retrieve single course or None

    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    # Verify if the teacher exists
    teacher_stmt = select(Teacher).where(Teacher.id == teacher_id)
    result = await db.execute(teacher_stmt)
    teacher = result.scalar_one_or_none()  # Retrieve single teacher or None

    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")

    # Assign the teacher to the course
    course.teacher_id = teacher_id
    db.add(course)
    await db.commit()  # Persist changes
    await db.refresh(course)  # Fetch updated course state

    return {"message": "Teacher assigned successfully", "course_id": course.id, "teacher_id": course.teacher_id}

@router.put("/courses/{course_id}/update_teacher")
async def update_teacher(course_id: int, teacher_id: int, db: AsyncSession = Depends(get_db)):
    """
    Update the assigned teacher for a course.

    Args:
        course_id (int): The ID of the course.
        teacher_id (int): The new teacher's ID to assign.

    Raises:
        HTTPException: If the course or new teacher is not found.

    Returns:
        dict: Result message indicating success.
    """
    # Fetch the course from the database
    course_stmt = select(Course).where(Course.id == course_id)
    result = await db.execute(course_stmt)
    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    # Verify if the new teacher exists
    teacher_stmt = select(Teacher).where(Teacher.id == teacher_id)
    result = await db.execute(teacher_stmt)
    teacher = result.scalar_one_or_none()

    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")

    # Update the teacher assignment
    course.teacher_id = teacher_id
    db.add(course)
    await db.commit()
    await db.refresh(course)

    return {"message": "Teacher updated successfully", "course_id": course.id, "teacher_id": course.teacher_id}

@router.get("/courses")
async def get_courses(db: AsyncSession = Depends(get_db)):
    """
    Retrieve all courses, including assigned teacher information.

    Returns:
        list: A list of courses with assigned teachers.
    """
    courses_stmt = select(Course)
    result = await db.execute(courses_stmt)
    courses = result.scalars().all()  # Retrieve all courses

    return [{"course_id": course.id, "teacher_id": course.teacher_id, "teacher_name": course.teacher.name if course.teacher else "Unassigned"} for course in courses]
```