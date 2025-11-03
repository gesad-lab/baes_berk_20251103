```python
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from src.database import get_db  # Assuming this utility is defined
from src.services.course_service import CourseService  # Importing the CourseService
from pydantic import BaseModel, Field

app = FastAPI()

# Pydantic model for creating a course
class CourseCreate(BaseModel):
    name: str = Field(..., description="The name of the course")
    level: str = Field(..., description="The level of the course")

# Pydantic model for the response
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str

# Initialize the CourseService
course_service = CourseService()

@app.post("/courses", response_model=CourseResponse, status_code=201)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    """
    Create a new course in the database.
    
    Parameters:
    - course: The CourseCreate model containing name and level.
    - db: The database session, retrieved via FastAPI dependency injection.

    Returns:
    A CourseResponse model representing the created course.
    """
    # Validate and create the course using the service layer
    try:
        created_course = course_service.create_course(course.name, course.level, db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return created_course

@app.get("/courses/{course_id}", response_model=CourseResponse)
def get_course(course_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a course by its ID.
    
    Parameters:
    - course_id: The ID of the course to retrieve.
    - db: The database session, retrieved via FastAPI dependency injection.

    Returns:
    A CourseResponse model representing the requested course.

    Raises:
    HTTPException with status code 404 if the course does not exist.
    """
    course = course_service.get_course_by_id(course_id, db)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    return course
```