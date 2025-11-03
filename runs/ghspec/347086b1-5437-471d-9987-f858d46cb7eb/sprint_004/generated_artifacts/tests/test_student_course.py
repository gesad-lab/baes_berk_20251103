# tests/test_student_course.py

def test_associate_student_with_course(client):
    """Test successful association of an existing Student with a Course."""
    response = client.post("/students/1/courses", json={"course_id": 1})
    assert response.status_code == 200
    assert response.json()["student_id"] == 1
    assert response.json()["course_id"] == 1

def test_associate_nonexistent_student(client):
    """Test association request for a non-existent Student."""
    response = client.post("/students/999/courses", json={"course_id": 1})
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "E001"  # Student not found

def test_associate_nonexistent_course(client):
    """Test association request for an existing Student and a non-existent Course."""
    response = client.post("/students/1/courses", json={"course_id": 999})
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "E002"  # Course not found

def test_get_courses_for_student(client):
    """Test retrieval of Courses associated with a Student."""
    response = client.get("/students/1/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Check that response is a list

def test_get_courses_for_student_with_no_courses(client):
    """Test retrieval for a Student that has no associated Courses."""
    response = client.get("/students/2/courses")  # Assuming student 2 has no courses
    assert response.status_code == 200
    assert response.json() == []  # Expecting an empty list

def test_retaining_existing_student_data(client):
    """Test that existing student data is not altered during course association."""
    response_before = client.get("/students/1")
    existing_data = response_before.json()

    # Associate with a new course
    client.post("/students/1/courses", json={"course_id": 1})

    response_after = client.get("/students/1")
    assert response_after.status_code == 200
    assert response_after.json() == existing_data  # Ensure no changes in student data