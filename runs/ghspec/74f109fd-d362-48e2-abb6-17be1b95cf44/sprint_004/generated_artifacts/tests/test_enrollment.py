```python
import pytest
from src.models.student import Student
from src.models.course import Course
from src.repositories.student_courses_repository import StudentCoursesRepository
from src.services.student_courses_service import StudentCoursesService
from sqlalchemy.exc import IntegrityError

@pytest.fixture
def student_courses_repository():
    """Fixture for initializing the StudentCoursesRepository for tests."""
    return StudentCoursesRepository()

@pytest.fixture
def student_courses_service(student_courses_repository):
    """Fixture for initializing the StudentCoursesService for tests."""
    return StudentCoursesService(student_courses_repository)

@pytest.fixture
def valid_student():
    """Fixture for creating a valid student instance."""
    student = Student(name="John Doe")
    return student

@pytest.fixture
def valid_course():
    """Fixture for creating a valid course instance."""
    course = Course(name="Math 101")
    return course

def test_enroll_student_in_course_valid(student_courses_service, valid_student, valid_course):
    """
    Test enrolling a student in a course with valid IDs.
    Expect successful enrollment response.
    """
    # Assume both student and course are created and IDs are available
    student_id = valid_student.id  # Simulate existing student
    course_id = valid_course.id  # Simulate existing course
    
    response = student_courses_service.enroll_student_in_course(student_id, course_id)
    
    assert response['student_id'] == student_id
    assert response['course_id'] == course_id
    assert response['message'] == "Enrollment successful"

def test_enroll_student_in_course_invalid_student(student_courses_service, valid_course):
    """
    Test attempting to enroll a student in a course with an invalid student ID.
    Expect error response indicating invalid student.
    """
    invalid_student_id = 9999  # Simulating a non-existent student ID
    course_id = valid_course.id
    
    with pytest.raises(IntegrityError):
        student_courses_service.enroll_student_in_course(invalid_student_id, course_id)

def test_enroll_student_in_course_invalid_course(student_courses_service, valid_student):
    """
    Test attempting to enroll a student in a course with an invalid course ID.
    Expect error response indicating invalid course.
    """
    student_id = valid_student.id
    invalid_course_id = 9999  # Simulating a non-existent course ID
    
    with pytest.raises(IntegrityError):
        student_courses_service.enroll_student_in_course(student_id, invalid_course_id)

def test_retrieve_student_courses_valid(student_courses_service, valid_student):
    """
    Test retrieving courses for a student with valid ID.
    Expect a list of courses associated with the student.
    """
    student_id = valid_student.id  # Simulate existing student
    
    response = student_courses_service.get_student_courses(student_id)

    assert isinstance(response, list)  # Expect a list of courses
    assert all('course_id' in course for course in response)  # Each course should have a course_id

def test_retrieve_student_courses_invalid(student_courses_service):
    """
    Test retrieving courses for a student with an invalid ID.
    Expect error response indicating invalid student.
    """
    invalid_student_id = 9999  # Simulating a non-existent student ID
    
    response = student_courses_service.get_student_courses(invalid_student_id)

    assert response['error']['code'] == "E001"
    assert response['error']['message'] == "Student does not exist"
```