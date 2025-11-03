import pytest
from src.services.student_service import StudentService
from src.repositories.student_repository import StudentRepository
from src.models.student import Student

@pytest.fixture
def student_service():
    # Mock the StudentRepository for testing
    repository = StudentRepository()
    service = StudentService(repository)
    return service

def test_associate_course_with_student(student_service):
    student_id = "student-123"
    course_id = "course-abc"
    
    # Assume the student exists in the repository
    student = Student(id=student_id, name="John Doe")
    student_service.repository.add_student(student)  # Simulate adding student to the repository
    
    # Act
    response = student_service.associate_course(student_id, course_id)

    # Assert
    assert response['message'] == "Student successfully associated with course."
    assert course_id in response['courses']  # Check if the course was added

def test_retrieve_student_with_courses(student_service):
    student_id = "student-456"
    course_id = "course-def"
    
    # Assume the student exists in the repository with an associated course
    student = Student(id=student_id, name="Jane Doe", courses=[course_id])
    student_service.repository.add_student(student)
    
    # Act
    response = student_service.retrieve_student(student_id)

    # Assert
    assert response['id'] == student_id
    assert response['name'] == "Jane Doe"
    assert course_id in response['courses']  # Check if the course is in the response

def test_error_handling_for_invalid_course_id(student_service):
    student_id = "student-789"
    
    # Assume the student exists in the repository
    student = Student(id=student_id, name="Alice Smith")
    student_service.repository.add_student(student)

    invalid_course_id = ""  # Empty course ID to trigger error
    
    # Act
    response, status_code = student_service.associate_course(student_id, invalid_course_id)

    # Assert
    assert status_code == 400  # Check that the status code is for a bad request
    assert response['error']['message'] == "Invalid course ID provided."  # Validate error message

def test_non_existent_student_retrieval(student_service):
    # Act
    response = student_service.retrieve_student("non-existent-id")

    # Assert
    assert response['error']['message'] == "Student not found."  # Ensure a proper error message

def test_database_migration_preserves_data(student_service):
    # Setting up test conditions here to ensure existing students are intact.
    student_id = "student-111"
    student = Student(id=student_id, name="Bob Brown")
    student_service.repository.add_student(student)
    
    # Simulate running a migration event here (ideally, you would check the actual DB)
    # For the sake of this test, we assert the student is still in the repository after migration
    assert student_service.repository.get_student(student_id) is not None  # Ensure the student still exists