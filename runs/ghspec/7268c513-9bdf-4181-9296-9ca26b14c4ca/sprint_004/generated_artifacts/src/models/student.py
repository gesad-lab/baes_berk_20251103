```python
from app import db
from sqlalchemy import Column, Integer, ForeignKey
from app.models import Student, Course  # Importing existing models for relationships

class StudentCourse(db.Model):
    __tablename__ = 'student_course'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

# This method allows us to fetch enrolled courses for a student
def get_enrolled_courses(student_id):
    student = Student.query.get(student_id)
    if not student:
        return None  # Student not found
    
    return [course.id for course in student.courses]  # List of course ids

# This method allows us to enroll a student in a course     
def enroll_student_in_course(student_id, course_id):
    student = Student.query.get(student_id)
    if not student:
        return None  # Student not found

    course = Course.query.get(course_id)
    if not course:
        return None  # Course not found

    # Append the course to the student's courses and commit to the database
    student.courses.append(course)
    db.session.commit()
    
    return student  # Return the updated student record with new course enrollment
```