```python
from fastapi import FastAPI, HTTPException, Depends, Path
from pydantic import BaseModel
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .models import Student, Course, StudentCourse
from .database import get_db

app = FastAPI()

# Request model for course enrollment
class EnrollmentRequest(BaseModel):
    course_ids: List[int]

@app.post("/students/{id}/courses", status_code=200)
async def enroll_student(id: int, enrollment_request: EnrollmentRequest, db: AsyncSession = Depends(get_db)):
    """Enroll a student into one or more courses."""
    # Validate that the student exists
    student = await db.execute(select(Student).where(Student.id == id))
    student = student.scalar_one_or_none()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Validate course IDs
    courses = await db.execute(select(Course).where(Course.id.in_(enrollment_request.course_ids)))
    valid_courses = courses.scalars().all()
    
    not_found_courses = set(enrollment_request.course_ids) - {course.id for course in valid_courses}
    if not_found_courses:
        raise HTTPException(status_code=400, detail=f"Invalid course IDs: {not_found_courses}")

    # Enroll student in valid courses
    for course in valid_courses:
        student_course = StudentCourse(student_id=id, course_id=course.id)
        db.add(student_course)

    await db.commit()
    return {"message": "Enrolled successfully", "enrolled_courses": [course.id for course in valid_courses]}

@app.delete("/students/{id}/courses/{course_id}", status_code=204)
async def unenroll_student(id: int, course_id: int, db: AsyncSession = Depends(get_db)):
    """Unenroll a student from a specific course."""
    # Check if student-course relationship exists
    student_course = await db.execute(
        select(StudentCourse).where(StudentCourse.student_id == id, StudentCourse.course_id == course_id)
    )
    student_course = student_course.scalar_one_or_none()
    
    if not student_course:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    
    await db.delete(student_course)
    await db.commit()

@app.get("/students/{id}/courses", status_code=200)
async def get_student_courses(id: int, db: AsyncSession = Depends(get_db)):
    """Retrieve all courses associated with a student."""
    student_courses = await db.execute(
        select(Course).join(StudentCourse).where(StudentCourse.student_id == id)
    )
    return student_courses.scalars().all()

@app.get("/students/{id}", status_code=200)
async def get_student_details(id: int, db: AsyncSession = Depends(get_db)):
    """Retrieve detailed information about a student, including enrolled courses."""
    student = await db.execute(select(Student).where(Student.id == id))
    student = student.scalar_one_or_none()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    courses = await db.execute(
        select(Course).join(StudentCourse).where(StudentCourse.student_id == id)
    )
    enrolled_courses = courses.scalars().all()

    return {
        "student": student,
        "enrolled_courses": [course for course in enrolled_courses]
    }
```