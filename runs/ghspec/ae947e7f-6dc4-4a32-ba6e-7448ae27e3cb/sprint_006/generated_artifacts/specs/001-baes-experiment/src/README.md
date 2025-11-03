# Updated README.md

# Course Management API

## API Endpoints

### Associate a Teacher with a Course

- **POST /courses/{id}/teacher**
  - **Request Body**: JSON object containing `teacher_id`.
  - **Success Response**:
    - **Code**: 200 OK
    - **Content**: `{"message": "Teacher has been associated with the course."}`
  
### Retrieve Course with Teacher Information

- **GET /courses/{id}**
  - **Success Response**:
    - **Code**: 200 OK
    - **Content**: 
      ```json
      {
        "course_id": 1,
        "course_name": "Mathematics",
        "teacher": {
          "name": "John Doe",
          "email": "john.doe@example.com"
        }
      }
      ```

### Validate Association with Invalid Course or Teacher

- **POST /courses/{id}/teacher**
  - **Request Body**: JSON object containing `teacher_id` for a non-existing teacher.
  - **Error Response**:
    - **Code**: 400 Bad Request
    - **Content**: `{"error": {"code": "E001", "message": "Teacher does not exist."}}`

### Dissociate a Teacher from a Course

- **DELETE /courses/{id}/teacher**
  - **Success Response**:
    - **Code**: 200 OK
    - **Content**: `{"message": "Teacher has been removed from the course."}`
  
## Testing

### Testing Scenarios

1. **Scenario 1**: Associate a Teacher with a Course
   - As an admin user, associate a specific teacher with a course to ensure each course has a designated educator.
   
2. **Scenario 2**: Retrieve Course with Teacher Information
   - Retrieve information about a course, including the associated teacher's details to confirm the correct assignment.
   
3. **Scenario 3**: Validate Association with Invalid Course or Teacher
   - Ensure that attempts to associate a course with a non-existent teacher return an error.
   
4. **Scenario 4**: Dissociate a Teacher from a Course
   - Dissociate a teacher from a course to remove their assignment when necessary.

### Example Test for Dissociating a Teacher

To test the `DELETE /courses/{id}/teacher` endpoint, you can use the following pytest function in your test suite:

```python
def test_dissociate_teacher_from_course(client):
    """Test dissociating a teacher from a course."""
    course_id = 1
    teacher_id = 1  # Assuming this teacher exists
    
    # First, associate the teacher with the course
    client.post(f"/courses/{course_id}/teacher", json={"teacher_id": teacher_id})
    
    # Now, dissociate the teacher
    response = client.delete(f"/courses/{course_id}/teacher")
    assert response.status_code == 200  # 200 OK
    assert response.json() == {"message": "Teacher has been removed from the course."}
```

Please ensure you have the necessary setup to run the tests using `pytest` and the FastAPI testing client.