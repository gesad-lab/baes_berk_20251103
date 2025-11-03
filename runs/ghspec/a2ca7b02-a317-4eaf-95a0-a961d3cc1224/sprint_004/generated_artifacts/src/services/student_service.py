```python
from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.student import Student
from models.course import Course

class StudentService:
    @staticmethod
    async def enroll_student_in_course(student_id: str, course_id: str, db: Session):
        """
        Enrolls a student in a course.

        Parameters:
        - student_id: str - The ID of the student to enroll.
        - course_id: str - The ID of the course to enroll the student in.
        - db: Session - The database session.

        Returns:
        - Updated student object with enrolled courses.

        Raises:
        - HTTPException if the student or course does not exist.
        """
        # Validate if the student exists
        student = db.query(Student).filter(Student.id == student_id).first()
        if not student:
            raise HTTPException(status_code=404, detail={"error": {"code": "E001", "message": "Student not found."}})

        # Validate if the course exists
        course = db.query(Course).filter(Course.id == course_id).first()
        if not course:
            raise HTTPException(status_code=404, detail={"error": {"code": "E002", "message": "Course not found."}})

        # Enroll student in course
        student.courses.append(course)  # Assuming 'courses' relationship is defined in the Student model
        db.commit()
        db.refresh(student)  # Refresh the student instance to get updated courses

        return student  # Return the updated student object
```