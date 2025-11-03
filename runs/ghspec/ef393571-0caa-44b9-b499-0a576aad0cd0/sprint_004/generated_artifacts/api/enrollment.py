```python
from fastapi import APIRouter, HTTPException, Path
from pydantic import BaseModel
from typing import List, Optional
import aiosqlite

# Define the request model for course enrollment
class CourseEnrollment(BaseModel):
    course_id: int

# Define the response model for enrolled courses
class EnrolledCoursesResponse(BaseModel):
    courses: List[int]  # List of course IDs

router = APIRouter()

@router.post("/students/{student_id}/courses", response_model=None)
async def enroll_student(student_id: int, enrollment: CourseEnrollment):
    """Enroll a student in a specified course."""
    async with aiosqlite.connect("database.db") as db:
        # Check if the course exists
        course_check = await db.execute("SELECT id FROM course WHERE id = ?", (enrollment.course_id,))
        course = await course_check.fetchone()
        
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")
        
        # Enroll the student in the course
        await db.execute("""
            INSERT INTO student_course (student_id, course_id) VALUES (?, ?)
            """, (student_id, enrollment.course_id))
        await db.commit()

@router.get("/students/{student_id}/courses", response_model=EnrolledCoursesResponse)
async def get_student_courses(student_id: int):
    """Retrieve all courses associated with the specified student."""
    async with aiosqlite.connect("database.db") as db:
        cursor = await db.execute("""
            SELECT course_id FROM student_course WHERE student_id = ?
        """, (student_id,))
        courses = await cursor.fetchall()
        
        return EnrolledCoursesResponse(courses=[course[0] for course in courses])

@router.get("/courses/{course_id}/students")
async def get_students_enrolled_in_course(course_id: int):
    """Retrieve all students enrolled in the specified course."""
    async with aiosqlite.connect("database.db") as db:
        cursor = await db.execute("""
            SELECT student_id FROM student_course WHERE course_id = ?
        """, (course_id,))
        students = await cursor.fetchall()
        
        # Returning student IDs as a list
        return {"students": [student[0] for student in students]}
```