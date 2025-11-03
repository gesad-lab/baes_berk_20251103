```python
import requests

BASE_URL = "http://localhost:8000/students"  # Base URL for Student API

def test_enroll_student_in_courses():
    """Test enrolling a student in a course."""
    # Create a test student (assume this endpoint exists)
    student_response = requests.post(BASE_URL, json={"name": "John Doe", "email": "john.doe@example.com"})
    assert student_response.status_code == 201  # Ensure student creation is successful
    student_id = student_response.json()["id"]

    # Create a test course (assume this endpoint exists)
    course_response = requests.post("http://localhost:8000/courses", json={"name": "Mathematics", "level": "100"})
    assert course_response.status_code == 201  # Ensure course creation is successful
    course_id = course_response.json()["id"]

    # Enroll the student in the course
    enrollment_response = requests.post(f"{BASE_URL}/{student_id}/enroll", json={"course_id": course_id})
    assert enrollment_response.status_code == 200  # Ensure enrollment is successful
    assert enrollment_response.json()["message"] == "Enrollment successful"
    
    # Verify that the student is actually enrolled
    check_enrollment_response = requests.get(f"{BASE_URL}/{student_id}/courses")
    assert check_enrollment_response.status_code == 200
    enrolled_courses = check_enrollment_response.json()
    assert course_id in [course["id"] for course in enrolled_courses]  # Check that the course is in the enrollment list

def test_unenroll_student_from_courses():
    """Test unenrolling a student from a course."""
    # Assume we use the same student and course created in the previous test
    student_id = 1  # Replace with a valid student ID from test setup
    course_id = 1   # Replace with a valid course ID from test setup

    # Unenroll the student from the course
    unenrollment_response = requests.delete(f"{BASE_URL}/{student_id}/unenroll", json={"course_id": course_id})
    assert unenrollment_response.status_code == 200  # Ensure unenrollment is successful
    assert unenrollment_response.json()["message"] == "Unenrollment successful"

    # Verify that the student is no longer enrolled
    check_enrollment_response = requests.get(f"{BASE_URL}/{student_id}/courses")
    assert check_enrollment_response.status_code == 200
    enrolled_courses = check_enrollment_response.json()
    assert course_id not in [course["id"] for course in enrolled_courses]  # Check that the course is no longer in the enrollment list

def test_enroll_student_with_invalid_course():
    """Test enrolling a student with an invalid course ID."""
    student_id = 1  # Replace with a valid student ID from test setup
    invalid_course_id = 9999  # Assuming this ID does not exist

    # Attempt to enroll the student in the invalid course
    enrollment_response = requests.post(f"{BASE_URL}/{student_id}/enroll", json={"course_id": invalid_course_id})
    assert enrollment_response.status_code == 400  # Ensure an error is returned
    assert enrollment_response.json()["error"]["message"] == "Invalid course ID"  # Check for specific error message
```