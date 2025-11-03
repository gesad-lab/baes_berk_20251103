# File: tests/controllers/test_course_controller.py

```python
import pytest
from validation import validate_course_data

def test_validate_course_data_without_name():
    """
    Test case for creating a course without a name.
    Expected outcome: ValueError should be raised indicating the name field is required.
    """
    data = {'level': 'beginner'}
    with pytest.raises(ValueError) as excinfo:
        validate_course_data(data)

    assert str(excinfo.value) == "Both name and level fields are required."

def test_remove_course_from_student(client):
    """
    Test case for removing a course from a student's associations.
    Expected outcome: The specified course is removed successfully and a confirmation message is returned.
    """
    # Initially associate courses with a student
    client.post('/students/1/courses', json={'course_ids': [1, 2, 3]})
    
    # Request to remove course 2 from student 1
    response = client.delete('/students/1/courses/2')
    
    assert response.status_code == 200
    assert response.json['message'] == "Course removed from student successfully."
    
    # Verify that the course 2 is no longer associated with student 1
    response = client.get('/students/1')
    assert 2 not in response.json['courses']

def test_remove_nonexistent_course_from_student(client):
    """
    Test case for attempting to remove a course that is not associated with a student.
    Expected outcome: The application responds with an appropriate error message.
    """
    # Initially associate courses with a student
    client.post('/students/1/courses', json={'course_ids': [1, 2]})

    # Trying to remove a non-associated course (course 3)
    response = client.delete('/students/1/courses/3')
    
    assert response.status_code == 400
    assert response.json['error']['message'] == "Course not found in student's associations."
```