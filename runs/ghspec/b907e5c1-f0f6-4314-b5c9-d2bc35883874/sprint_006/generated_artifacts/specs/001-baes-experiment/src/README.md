```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Course, Teacher

# Define a fixture to set up the database connection and necessary tables
@pytest.fixture(scope='module')
def db_setup():
    # Create a temporary in-memory SQLite database for testing
    engine = create_engine('sqlite:///test_database.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the tables for Course and Teacher models
    Course.metadata.create_all(engine)
    Teacher.metadata.create_all(engine)

    yield session  # Provide the session to tests

    session.close()
    # Optionally remove the database file after tests if needed
    import os
    if os.path.exists('test_database.db'):
        os.remove('test_database.db')

def test_assign_teacher_to_course(db_setup):
    session = db_setup

    # Create a teacher instance and add it to the database
    teacher = Teacher(name="John Doe")
    session.add(teacher)
    session.commit()

    # Create a course instance and add it to the database
    course = Course(title="Mathematics")
    session.add(course)
    session.commit()

    # Assign the teacher to the course
    course.teacher_id = teacher.id
    session.commit()

    # Retrieve the course from the database
    updated_course = session.query(Course).filter_by(id=course.id).first()

    # Assert the course has the assigned teacher
    assert updated_course.teacher_id == teacher.id

def test_get_course_details_with_teacher(db_setup):
    session = db_setup

    # Create a teacher instance and add it to the database
    teacher = Teacher(name="Jane Smith")
    session.add(teacher)
    session.commit()

    # Create a course instance and assign the teacher to it
    course = Course(title="Physics", teacher_id=teacher.id)
    session.add(course)
    session.commit()

    # Retrieve course details
    retrieved_course = session.query(Course).filter_by(id=course.id).first()

    # Assert the course title and the assigned teacher's details
    assert retrieved_course.title == "Physics"
    assert retrieved_course.teacher_id == teacher.id

def test_list_courses_with_teachers(db_setup):
    session = db_setup

    # Create a teacher instance and add it to the database
    teacher1 = Teacher(name="Mark Twain")
    teacher2 = Teacher(name="Emily Dickinson")
    session.add(teacher1)
    session.add(teacher2)
    session.commit()

    # Create courses with assigned teachers
    course1 = Course(title="Literature", teacher_id=teacher1.id)
    course2 = Course(title="Poetry", teacher_id=teacher2.id)
    session.add(course1)
    session.add(course2)
    session.commit()

    # Retrieve all courses
    courses = session.query(Course).all()

    # Assert the courses are retrieved correctly with associated teacher info
    assert len(courses) == 2
    assert courses[0].teacher_id == teacher1.id
    assert courses[1].teacher_id == teacher2.id
```