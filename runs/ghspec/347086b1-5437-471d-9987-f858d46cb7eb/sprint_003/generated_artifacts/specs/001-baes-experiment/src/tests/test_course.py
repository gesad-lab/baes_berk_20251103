# tests/test_course.py

def test_create_course(client):
    """Test creation of a new Course with valid parameters."""
    response = client.post("/courses", json={"name": "Introduction to Programming", "level": "Beginner"})
    assert response.status_code == 201  # Expecting Successful creation
    assert response.json()["name"] == "Introduction to Programming"  # Check course name
    assert response.json()["level"] == "Beginner"  # Check course level

def test_create_course_missing_name(client):
    """Test creation of a Course without name should return an error."""
    response = client.post("/courses", json={"level": "Beginner"})
    assert response.status_code == 400  # Expecting Bad Request due to missing name
    assert response.json()["error"]["code"] == "E001"  # Code for missing name

def test_create_course_missing_level(client):
    """Test creation of a Course without level should return an error."""
    response = client.post("/courses", json={"name": "Introduction to Programming"})
    assert response.status_code == 400  # Expecting Bad Request due to missing level
    assert response.json()["error"]["code"] == "E002"  # Code for missing level

def test_retrieve_courses(client):
    """Test retrieving all Courses."""
    response = client.get("/courses")
    assert response.status_code == 200  # Expecting Successful retrieval
    assert isinstance(response.json(), list)  # Ensure response is a list
    # Here you can add additional assertions about the contents if specific courses were created beforehand.