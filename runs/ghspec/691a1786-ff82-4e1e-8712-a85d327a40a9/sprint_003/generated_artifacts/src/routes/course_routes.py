```python
from fastapi import APIRouter, HTTPException, status
from src.models.course import Course
from src.schemas.course_schemas import CourseCreate, CourseResponse
from src.services.course_service import CourseService
from sqlalchemy.exc import NoResultFound

router = APIRouter()
course_service = CourseService()

@router.post("/courses/", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
async def create_course(course: CourseCreate):
    """
    Create a new course.

    Args:
        course (CourseCreate): The course details to create.

    Returns:
        CourseResponse: The created course details.
    """
    try:
        created_course = await course_service.create_course(course)
        return created_course
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        

@router.get("/courses/{course_id}", response_model=CourseResponse)
async def get_course(course_id: int):
    """
    Retrieve a course by its ID.

    Args:
        course_id (int): The ID of the course.

    Returns:
        CourseResponse: The course details.
    """
    try:
        course = await course_service.get_course(course_id)
        return course
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.put("/courses/{course_id}", response_model=CourseResponse)
async def update_course(course_id: int, course: CourseCreate):
    """
    Update an existing course.

    Args:
        course_id (int): The ID of the course to update.
        course (CourseCreate): The new course details.

    Returns:
        CourseResponse: The updated course details.
    """
    try:
        updated_course = await course_service.update_course(course_id, course)
        return updated_course
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/courses/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(course_id: int):
    """
    Delete a course by its ID.

    Args:
        course_id (int): The ID of the course to delete.
    
    Returns:
        None: Returns a success message if deletion is successful.
    """
    try:
        await course_service.delete_course(course_id)
        return {"detail": "Course deleted successfully"}
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
```
