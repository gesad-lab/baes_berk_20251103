```python
from sqlalchemy.orm import Session
from models import Course  # Assuming Course model is defined in models.py
from schema import CourseCreate, CourseResponse  # Assuming these schemas are defined for request and response validation
from fastapi import HTTPException, status

class CourseService:
    def __init__(self, db: Session):
        self.db = db

    def create_course(self, course_create: CourseCreate) -> CourseResponse:
        """
        Create a new course in the database.

        Args:
            course_create (CourseCreate): The data required to create a new course.

        Returns:
            CourseResponse: The created course data.

        Raises:
            HTTPException: If the course name already exists.
        """
        # Check if the course already exists by name
        existing_course = self.db.query(Course).filter(Course.name == course_create.name).first()
        if existing_course:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Course with this name already exists.",
                headers={"X-Error": "CourseNameExists"},
            )

        # Create the new course object
        new_course = Course(**course_create.dict())

        # Add to the session and commit to save it
        self.db.add(new_course)
        self.db.commit()
        self.db.refresh(new_course)  # Refresh to get the new data including generated fields (like ID)

        return CourseResponse.from_orm(new_course)  # Assuming CourseResponse is a Pydantic model for returning course data
```