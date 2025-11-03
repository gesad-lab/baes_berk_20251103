'''
Router module to include API routes for students, courses, and teachers.
'''
from fastapi import APIRouter
from student import router as student_router  # Import student router
from course import router as course_router    # Import course router
from teacher import router as teacher_router  # Import teacher router
router = APIRouter()
# Include the routers
router.include_router(student_router)
router.include_router(course_router)
router.include_router(teacher_router)