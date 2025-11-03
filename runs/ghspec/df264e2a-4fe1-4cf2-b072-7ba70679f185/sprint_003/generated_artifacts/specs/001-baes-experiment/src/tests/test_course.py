```python
# app/services/course_service.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from fastapi import HTTPException

Base = declarative_base()

# Define the Course model
class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

# Service to handle course-related logic
class CourseService:
    @staticmethod
    def create_course(db: Session, course_data: dict) -> Course:
        """Create a new course with the given data."""
        name = course_data.get("name")
        level = course_data.get("level")

        # Validate required fields
        if not name or not level:
            raise HTTPException(
                status_code=400,
                detail={"error": {"code": "E001", "message": "Both name and level are required."}}
            )
        
        new_course = Course(name=name, level=level)
        db.add(new_course)
        db.commit()
        db.refresh(new_course)
        return new_course

    @staticmethod
    def get_course(db: Session, course_id: int) -> Course:
        """Retrieve a course by ID."""
        course = db.query(Course).filter(Course.id == course_id).first()
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")
        return course
```