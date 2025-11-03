from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel, conint
from typing import List, Optional

# Assuming there are existing services for database interactions
from src.services.course_service import enroll_student_in_course, remove_course_from_student, get_courses_for_student

router = APIRouter()

# Input schema for enrolling a student in a course
class EnrollStudentRequest(BaseModel):
    student_id: conint(gt=0)  # Ensure student_id is a positive integer
    course_id: conint(gt=0)    # Ensure course_id is a positive integer

# Input schema for removing a course from a student's list
class RemoveCourseRequest(BaseModel):
    student_id: conint(gt=0)  # Ensure student_id is a positive integer
    course_id: conint(gt=0)    # Ensure course_id is a positive integer

# Response schema for courses associated with a student
class StudentCoursesResponse(BaseModel):
    student_id: int
    courses: List[int]  # List of course IDs associated with the student

@router.post("/enroll_student", response_model=StudentCoursesResponse)
async def enroll_student(request: EnrollStudentRequest):
    """
    Enroll a student in a specified course.
    Returns the updated student details including associated courses.
    """
    try:
        student_data = await enroll_student_in_course(request.student_id, request.course_id)
        return StudentCoursesResponse(student_id=request.student_id, courses=student_data.courses)
    except ValueError as e:
        # Handle specific errors related to enrollment (e.g., student not found, course not found)
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Log the unexpected error for further investigation
        raise HTTPException(status_code=500, detail="An internal error occurred")

@router.get("/student_courses/{student_id}", response_model=StudentCoursesResponse)
async def get_student_courses(student_id: int):
    """
    Retrieve all courses associated with a particular student using their student ID.
    """
    if student_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid student ID")
        
    courses = await get_courses_for_student(student_id)
    return StudentCoursesResponse(student_id=student_id, courses=courses)

@router.delete("/remove_course", response_model=StudentCoursesResponse)
async def remove_course(request: RemoveCourseRequest):
    """
    Remove a specific course from a student's list of courses.
    Returns the updated student details confirming removal.
    """
    try:
        student_data = await remove_course_from_student(request.student_id, request.course_id)
        return StudentCoursesResponse(student_id=request.student_id, courses=student_data.courses)
    except ValueError as e:
        # Handle specific errors related to course removal
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Log the unexpected error for further investigation
        raise HTTPException(status_code=500, detail="An internal error occurred")