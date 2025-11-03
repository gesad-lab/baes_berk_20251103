```markdown
# README.md

# Project Documentation

## API Endpoints

### Assign Teacher to Course

**POST /courses/{course_id}/assign_teacher**

Assigns a teacher to a specific course. 

**Request Body**:
```json
{
    "teacher_id": "<id_of_the_teacher>"
}
```

**Responses**:
- **201 Created**: Successfully assigned teacher to the course.
    ```json
    {
        "message": "Teacher assigned successfully.",
        "course": {
            "id": "<course_id>",
            "name": "<course_name>",
            "teacher": {
                "id": "<teacher_id>",
                "name": "<teacher_name>"
            }
        }
    }
    ```
- **404 Not Found**: When the specified course or teacher does not exist.
    ```json
    {
        "error": {
            "code": "E404",
            "message": "Course or Teacher not found."
        }
    }
    ```

### View Course with Teacher Information

**GET /courses/{course_id}**

Retrieves the details of a specific course along with the assigned teacher's information.

**Responses**:
- **200 OK**: Successfully retrieved course details.
    ```json
    {
        "id": "<course_id>",
        "name": "<course_name>",
        "teacher": {
            "id": "<teacher_id>",
            "name": "<teacher_name>"
        }
    }
    ```

- **404 Not Found**: If the course does not exist.
    ```json
    {
        "error": {
            "code": "E404",
            "message": "Course not found."
        }
    }
    ```

### Error Handling for Invalid Course-Teacher Association

When attempting to assign a non-existent teacher to a course, the application will return appropriate error messages.

**Responses**:
- **400 Bad Request**: When trying to assign a non-existent teacher.
    ```json
    {
        "error": {
            "code": "E400",
            "message": "Invalid teacher ID supplied."
        }
    }
    ```

## Test Cases

### Assign Teacher to Course Tests
- Test successful assignment of a teacher to a course.
- Verify error handling when assigning a non-existent teacher.
- Verify error handling when assigning to a non-existent course.

### Retrieve Course with Teacher Information Tests
- Check response structure and correctness of displayed teacher information for a course.

Ensure that these features work as expected by running the following tests:

```shell
pytest tests/test_routes.py
pytest tests/test_models.py
```

```python
# Ensure to create the tests in their respective test files. 
# Example additions in tests/test_routes.py

def test_assign_teacher_to_course(client):
    # Assuming a course with ID 1 and a teacher with ID 1 exists
    response = client.post('/courses/1/assign_teacher', json={'teacher_id': 1})
    assert response.status_code == 201
    assert response.json['message'] == "Teacher assigned successfully."

def test_assign_non_existent_teacher(client):
    response = client.post('/courses/1/assign_teacher', json={'teacher_id': 999})
    assert response.status_code == 404
    assert response.json['error']['code'] == "E404"

def test_get_course_with_teacher(client):
    # Add a sample course and teacher for testing
    response = client.get('/courses/1')
    assert response.status_code == 200
    assert 'teacher' in response.json
```
```
