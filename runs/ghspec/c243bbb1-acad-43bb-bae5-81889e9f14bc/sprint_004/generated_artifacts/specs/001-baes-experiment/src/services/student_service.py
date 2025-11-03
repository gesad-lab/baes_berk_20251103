```python
# services/student_service.py

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, ForeignKey, select
from sqlalchemy.exc import NoResultFound, IntegrityError
from sqlalchemy.orm import sessionmaker

# Database setup - adjust connection as needed
DATABASE_URL = 'sqlite:///courses.db'
engine = create_engine(DATABASE_URL)
metadata = MetaData(bind=engine)

# Define the student_courses association table
student_courses_table = Table('student_courses', metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

# Create a session maker
Session = sessionmaker(bind=engine)

def enroll_student_in_course(student_id: int, course_id: int) -> str:
    """Enroll a student in a course.
    
    Args:
        student_id (int): The ID of the student.
        course_id (int): The ID of the course.
    
    Returns:
        str: Success message if enrollment is successful.
    
    Raises:
        ValueError: If the course ID does not exist.
    """
    session = Session()
    try:
        # Check if the course exists
        query = select([student_courses_table]).where(student_courses_table.c.course_id == course_id)
        course_exists = session.execute(query).fetchone()
        
        if not course_exists:
            raise ValueError(f"E001: Course ID {course_id} does not exist.")
        
        # Enroll the student in the course
        insert_stmt = student_courses_table.insert().values(student_id=student_id, course_id=course_id)
        session.execute(insert_stmt)
        session.commit()
        return f"Student {student_id} successfully enrolled in course {course_id}."
        
    except IntegrityError:
        session.rollback()
        return f"Error: Student {student_id} is already enrolled in course {course_id}."
    except Exception as e:
        session.rollback()
        raise e  # Reraise unexpected exceptions
    finally:
        session.close()

def get_student_courses(student_id: int):
    """Retrieve the list of courses a student is enrolled in.
    
    Args:
        student_id (int): The ID of the student.
    
    Returns:
        list: A list of courses associated with the student.
    
    Raises:
        ValueError: If the student ID does not exist.
    """
    session = Session()
    try:
        # Retrieve courses associated with the student
        query = select([student_courses_table]).where(student_courses_table.c.student_id == student_id)
        courses = session.execute(query).fetchall()
        
        if not courses:
            raise ValueError(f"E002: Student ID {student_id} has no courses associated.")

        return [{'course_id': course.course_id} for course in courses]  # Return only course_id for simplicity
        
    except NoResultFound:
        raise ValueError(f"E003: Student ID {student_id} does not exist.")
    finally:
        session.close()
```