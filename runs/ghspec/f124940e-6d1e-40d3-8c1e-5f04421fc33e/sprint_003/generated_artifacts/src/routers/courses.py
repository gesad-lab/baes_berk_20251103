```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, constr  # Import constr for validation
from .models import Course  # Import the Course model
from .database import session  # Assuming there's a session object to interact with DB

router = APIRouter()

class CourseCreate(BaseModel):
    name: constr(min_length=1)  # Ensure name is a non-empty string
    level: constr(min_length=1)  # Ensure level is a non-empty string

class CourseResponse(BaseModel):
    id: int
    name: str
    level: str

@router.post("/courses", response_model=CourseResponse)
def create_course(course: CourseCreate):
    """
    Create a new course with the provided name and level.

    Parameters:
    - course: CourseCreate model containing the course details.

    Returns:
    - CourseResponse model of the created course.
    """
    # Check for existing course with the same name if necessary (business logic can be added)
    new_course = Course(name=course.name, level=course.level)  # Create new Course instance
    session.add(new_course)  # Add course to session
    session.commit()  # Commit changes to the database
    session.refresh(new_course)  # Refresh to get the new data from DB
    return new_course  # Return the newly created course

@router.get("/courses", response_model=list[CourseResponse])
def get_courses():
    """
    Retrieve all courses from the database.

    Returns:
    - List of CourseResponse models for all courses.
    """
    return session.query(Course).all()  # Query to get all courses

@router.put("/courses/{course_id}", response_model=CourseResponse)
def update_course(course_id: int, course: CourseCreate):
    """
    Update an existing course's details.

    Parameters:
    - course_id: ID of the course to update.
    - course: CourseCreate model with updated details.

    Returns:
    - CourseResponse model of the updated course.
    """
    existing_course = session.query(Course).filter(Course.id == course_id).first()
    if not existing_course:
        raise HTTPException(status_code=404, detail="Course not found")  # Raise error if not found
    existing_course.name = course.name  # Update name
    existing_course.level = course.level  # Update level
    session.commit()  # Commit changes
    session.refresh(existing_course)  # Refresh to ensure data is up-to-date
    return existing_course  # Return the updated course
```