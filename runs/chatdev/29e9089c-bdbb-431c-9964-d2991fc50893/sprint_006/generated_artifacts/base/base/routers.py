'''
Router module to include API routes for students and courses.
'''
from fastapi import APIRouter
from . import student, course  # Importing student and course routers
router = APIRouter()
router.include_router(student.router)
router.include_router(course.router)