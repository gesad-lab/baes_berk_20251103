```python
from fastapi import APIRouter, HTTPException, Body
from src.service.course_service import create_course, get_course_by_id

router = APIRouter()

@router.post("/courses", status_code=201)
async def create_course_endpoint(name: str = Body(...), level: str = Body(...)):
    """
    Endpoint to create a new course.
    
    Parameters:
    - name: The name of the course (required).
    - level: The level of the course (required).
    
    Returns:
    - The details of the created course.
    
    Raises:
    - HTTPException if the name or level is missing.
    """
    if not name or not level:
        # Raise an error if either field is missing
        error_code = "E001"
        if not name:
            raise HTTPException(status_code=400, detail={"error": {"code": error_code, "message": "Course name is required."}})
        if not level:
            raise HTTPException(status_code=400, detail={"error": {"code": error_code, "message": "Course level is required."}})
    
    # Call service layer to create a course
    course = create_course(name=name, level=level)
    return course

@router.get("/courses/{course_id}")
async def get_course_endpoint(course_id: int):
    """
    Endpoint to retrieve course details by ID.
    
    Parameters:
    - course_id: The ID of the course to retrieve.
    
    Returns:
    - The details of the requested course.
    
    Raises:
    - HTTPException if the course does not exist.
    """
    course = get_course_by_id(course_id)
    if not course:
        raise HTTPException(status_code=404, detail={"error": {"code": "E002", "message": "Course not found."}})
    
    return course
```