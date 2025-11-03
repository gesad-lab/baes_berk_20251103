```python
from pydantic import BaseModel, conint, validator
from sqlalchemy.orm import Session
from models.student import Student
from models.course import Course

class EnrollmentSchema(BaseModel):
    student_id: conint(gt=0)  # Ensures student_id is a positive integer
    course_id: conint(gt=0)   # Ensures course_id is a positive integer

    @validator('student_id')
    def validate_student_exists(cls, student_id):
        if not Student.query.get(student_id):
            raise ValueError(f'E001: Student with ID {student_id} does not exist.')
        return student_id

    @validator('course_id')
    def validate_course_exists(cls, course_id):
        if not Course.query.get(course_id):
            raise ValueError(f'E002: Course with ID {course_id} does not exist.')
        return course_id

    @validator('course_id', pre=True, always=True)
    def validate_enrollment_not_duplicate(cls, course_id, values):
        student_id = values.get('student_id')
        # Checking if the student is already enrolled in the course
        if student_id and Course.query.filter_by(id=course_id).filter(Student.courses.any(id=student_id)).count() > 0:
            raise ValueError(f'E003: Student with ID {student_id} is already enrolled in course {course_id}.')
        return course_id
```