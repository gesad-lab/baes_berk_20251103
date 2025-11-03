from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import aiosqlite

# Define request and response models for Course
class CourseResponse(BaseModel):
    """Model for representing a course's details in responses."""
    id: int
    name: str
    level: str
    teacher_id: Optional[int]  # Optional since a course may not always have a teacher assigned

class CourseUpdateRequest(BaseModel):
    """Model for updating a course with a teacher association."""
    teacher_id: int

router = APIRouter()

@router.get("/courses/{course_id}", response_model=CourseResponse)
async def get_course(course_id: int):
    """Retrieve the details of a specified course including the associated teacher.

    Args:
        course_id (int): The ID of the course to retrieve.

    Raises:
        HTTPException: If the course is not found.

    Returns:
        CourseResponse: The course details along with associated teacher information.
    """
    async with aiosqlite.connect("database.db") as db:
        cursor = await db.execute("""
            SELECT id, name, level, teacher_id 
            FROM course 
            WHERE id = ?
        """, (course_id,))
        course = await cursor.fetchone()
        
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found.")

        return CourseResponse(id=course[0], name=course[1], level=course[2], teacher_id=course[3])

@router.patch("/courses/{course_id}", response_model=CourseResponse)
async def update_course(course_id: int, request: CourseUpdateRequest):
    """Update an existing course with a teacher association.

    Args:
        course_id (int): The ID of the course to update.
        request (CourseUpdateRequest): The request model containing the teacher ID.

    Raises:
        HTTPException: If the course is not found, or if a teacher is assigned to overlapping courses.

    Returns:
        CourseResponse: The updated course details.
    """
    async with aiosqlite.connect("database.db") as db:
        # Validate conditions for overlapping course assignments
        overlapping_courses = await db.execute("""
            SELECT COUNT(*) FROM course 
            WHERE teacher_id = ? AND id != ?
            AND overlapping_schedule_condition_here
        """, (request.teacher_id, course_id,))
        overlap_count = await overlapping_courses.fetchone()
        
        if overlap_count[0] > 0:
            raise HTTPException(status_code=400, detail="Teacher is assigned to overlapping courses.")

        result = await db.execute(
            "UPDATE course SET teacher_id = ? WHERE id = ?",
            (request.teacher_id, course_id)
        )
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Course not found or update conflict occurred.")
        
        await db.commit()

        # Return the updated course details
        return await get_course(course_id)

# Ensure to import this router in the main application module to make it accessible
