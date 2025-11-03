```python
from fastapi import APIRouter, HTTPException
from src.service.course_service import retrieve_course
from src.model.course import Course
from src.model.teacher import Teacher

router = APIRouter()

@router.get("/courses/{course_id}", response_model=Course)
async def get_course_details(course_id: int):
    """
    Retrieve details of a course including associated teacher information.

    Parameters:
        course_id (int): The ID of the course to retrieve.

    Returns:
        Course: The course details, including teacher information if associated.

    Raises:
        HTTPException: If the course with the given ID does not exist.
    """
    # Attempt to retrieve the course by ID
    course = await retrieve_course(course_id)

    if course is None:
        # If course is not found, raise a 404 error
        raise HTTPException(status_code=404, detail={"code": "E404", "message": "Course not found."})

    # Return the retrieved course
    return course
```