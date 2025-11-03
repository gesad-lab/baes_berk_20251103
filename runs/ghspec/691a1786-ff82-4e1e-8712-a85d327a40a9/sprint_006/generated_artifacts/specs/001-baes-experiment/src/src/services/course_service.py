```python
# src/services/course_service.py

from sqlalchemy.orm import Session
from src.models.course import Course
from src.models.teacher import Teacher
from fastapi import HTTPException

class CourseService:
    def __init__(self, db: Session):
        self.db = db

    def associate_teacher(self, course_id: int, teacher_id: int) -> Course:
        """Associate a teacher with a course and return the updated course details."""
        course = self.db.query(Course).filter(Course.id == course_id).first()
        teacher = self.db.query(Teacher).filter(Teacher.id == teacher_id).first()
        
        if not course:
            raise HTTPException(status_code=404, detail="Course not found.")
        if not teacher:
            raise HTTPException(status_code=404, detail="Teacher not found.")

        course.teacher_id = teacher_id
        self.db.commit()
        self.db.refresh(course)
        return course

    def get_course_with_teacher(self, course_id: int) -> Course:
        """Retrieve a course's details including the associated teacher."""
        course = self.db.query(Course).filter(Course.id == course_id).first()
        
        if not course:
            raise HTTPException(status_code=404, detail="Course not found.")

        return course

    def update_teacher(self, course_id: int, teacher_id: int) -> Course:
        """Update the teacher associated with a course."""
        course = self.db.query(Course).filter(Course.id == course_id).first()
        teacher = self.db.query(Teacher).filter(Teacher.id == teacher_id).first()

        if not course:
            raise HTTPException(status_code=404, detail="Course not found.")
        if not teacher:
            raise HTTPException(status_code=404, detail="Teacher not found.")

        course.teacher_id = teacher_id
        self.db.commit()
        self.db.refresh(course)
        return course

    def remove_teacher_association(self, course_id: int) -> Course:
        """Remove teacher association from a course."""
        course = self.db.query(Course).filter(Course.id == course_id).first()
        
        if not course:
            raise HTTPException(status_code=404, detail="Course not found.")

        course.teacher_id = None
        self.db.commit()
        self.db.refresh(course)
        return course
```