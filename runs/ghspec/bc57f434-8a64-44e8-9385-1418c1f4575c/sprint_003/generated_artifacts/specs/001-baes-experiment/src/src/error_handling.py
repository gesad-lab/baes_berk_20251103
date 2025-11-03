```python
# src/error_handling.py

from fastapi import HTTPException
from fastapi.responses import JSONResponse

class CourseErrorMessages:
    """Class to manage custom error messages for course-related operations."""
    
    @staticmethod
    def validation_error(message: str) -> HTTPException:
        """Create a validation error response.
        
        Args:
            message (str): The error message to return.
        
        Returns:
            HTTPException: FastAPI HTTPException with validation details.
        """
        return HTTPException(
            status_code=400,
            detail={"error": {"code": "E001", "message": message}}
        )
    
    @staticmethod
    def course_not_found(course_id: int) -> HTTPException:
        """Create an error response for when a course is not found.
        
        Args:
            course_id (int): The ID of the course that was not found.
        
        Returns:
            HTTPException: FastAPI HTTPException indicating course not found.
        """
        return HTTPException(
            status_code=404,
            detail={"error": {"code": "E002", "message": f"Course with ID {course_id} not found."}}
        )

# Example usage within an API endpoint
# from fastapi import FastAPI, Depends
# from .validation import CourseCreate  # Assuming this exists as a Pydantic model
# from .models import Course  # Assuming Course model exists
# from .database import get_db  # Assuming database session handling exists

# app = FastAPI()

# @app.post("/courses")
# async def create_course(course: CourseCreate, db: Session = Depends(get_db)):
#     if not course.name or not isinstance(course.name, str):
#         raise CourseErrorMessages.validation_error("Course name is required and must be a string.")
#     if not course.level or not isinstance(course.level, str):
#         raise CourseErrorMessages.validation_error("Course level is required and must be a string.")

#     # Logic to create a course
#     ...

# @app.get("/courses/{course_id}")
# async def get_course(course_id: int, db: Session = Depends(get_db)):
#     course = db.query(Course).filter(Course.id == course_id).first()
#     if course is None:
#         raise CourseErrorMessages.course_not_found(course_id)
#     return course
```