import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db.database import Base
from src.models.student import Student
from src.models.course import Course
from src.models.student_course import StudentCourse
from src.services.student_service import enroll_student_in_course, remove_course_from_student

@pytest.fixture(scope='module')
def test_db():
    # Setup the test database
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    yield session  # This is where the testing happens

    # Teardown the database
    session.close()
    Base.metadata.drop_all(engine)

@pytest.fixture
def setup_students_and_courses(test_db):
    # Create a sample student and course for testing
    student = Student(name="Test Student")
    course = Course(title="Test Course")
    
    # Add and commit initial data
    test_db.add(student)
    test_db.add(course)
    test_db.commit()

    return student, course

def test_enroll_student_in_course(test_db, setup_students_and_courses):
    student, course = setup_students_and_courses
    
    # Enroll the student in the course
    updated_student = enroll_student_in_course(test_db, student.id, course.id)

    # Verify that the student is enrolled
    assert updated_student is not None
    assert len(updated_student.courses) == 1
    assert updated_student.courses[0].course_id == course.id

def test_remove_course_from_student(test_db, setup_students_and_courses):
    student, course = setup_students_and_courses
    
    # Enroll the student first
    enroll_student_in_course(test_db, student.id, course.id)
    
    # Now remove the enrolled course
    updated_student = remove_course_from_student(test_db, student.id, course.id)

    # Verify that the course has been removed
    assert updated_student is not None
    assert len(updated_student.courses) == 0

def test_student_course_migration_integrity(test_db):
    # Ensure the StudentCourse relationship table is created properly
    student_course_table = StudentCourse.__table__
    assert student_course_table is not None

    # Verify the columns exist in the join table
    assert 'student_id' in student_course_table.c
    assert 'course_id' in student_course_table.c
    
    # Check if foreign key constraints are set (assumed to be present based on original requirements)
    assert len(student_course_table.foreign_keys) == 2

    student = Student(name="Test Student Migration")
    course = Course(title="Test Course Migration")
    
    test_db.add(student)
    test_db.add(course)
    test_db.commit()

    # Enroll student in the course using the StudentCourse table directly
    test_db.execute(
        student_course_table.insert().values(student_id=student.id, course_id=course.id)
    )

    # Verify enrollment integrity
    enrolled_record = test_db.query(StudentCourse).filter_by(student_id=student.id, course_id=course.id).first()
    assert enrolled_record is not None

    # Clean up
    test_db.delete(enrolled_record)
    test_db.commit()