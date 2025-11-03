```python
from fastapi import APIRouter, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.repository.models import StudentCourses
from src.database import get_db

router = APIRouter()

@router.delete("/api/v1/students/{student_id}/courses/{course_id}", response_model=dict)
async def unenroll_student_from_course(student_id: int, course_id: int, db: AsyncSession = Depends(get_db)):
    """
    Unenroll a student from a specific course.
    
    Args:
        student_id (int): The ID of the student to unenroll.
        course_id (int): The ID of the course to unenroll from.
        db (AsyncSession): The database session.
        
    Returns:
        dict: Confirmation message about the unenrollment.
    
    Raises:
        HTTPException: If the unenrollment fails or the record does not exist.
    """
    # Attempt to find the StudentCourses record
    student_course = await db.execute(
        select(StudentCourses).where(
            StudentCourses.student_id == student_id,
            StudentCourses.course_id == course_id
        )
    )
    student_course = student_course.scalar_one_or_none()

    # If no record found, return an error response
    if not student_course:
        raise HTTPException(status_code=404, detail="Enrollment record not found.")

    # Remove the StudentCourses record
    await db.delete(student_course)
    await db.commit()

    return {"message": "Student unenrolled from course successfully."}
```