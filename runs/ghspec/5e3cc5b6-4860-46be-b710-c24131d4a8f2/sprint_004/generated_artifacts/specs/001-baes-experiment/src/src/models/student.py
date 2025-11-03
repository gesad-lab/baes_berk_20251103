```python
# src/models/student.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    
    # Establishing a relationship with StudentCourse
    courses = relationship('StudentCourse', back_populates='student')

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', email='{self.email}')>"

    def add_courses(self, course_ids):
        """
        Associates the student with the provided list of course IDs.
        
        :param course_ids: List of Course IDs to associate with this student.
        """
        for course_id in course_ids:
            # Assuming StudentCourse is a model that establishes many-to-many relationship
            self.courses.append(StudentCourse(course_id=course_id))
```

```python
# src/models/student_course.py

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class StudentCourse(Base):
    __tablename__ = 'student_courses'
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)

    student = relationship('Student', back_populates='courses')
    course = relationship('Course', back_populates='students')

    def __repr__(self):
        return f"<StudentCourse(student_id={self.student_id}, course_id={self.course_id})>"
```

```python
# src/models/course.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.database import Base

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    
    # Establishing a relationship with StudentCourse
    students = relationship('StudentCourse', back_populates='course')

    def __repr__(self):
        return f"<Course(id={self.id}, title='{self.title}')>"
```