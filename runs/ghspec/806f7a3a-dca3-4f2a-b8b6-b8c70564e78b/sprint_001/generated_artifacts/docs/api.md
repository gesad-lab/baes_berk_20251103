# API Documentation

## Student Management API

### Endpoints

#### 1. Create a Student
- **Endpoint**: `POST /students`
- **Request Body**: 
  ```json
  {
      "name": "string"
  }
  ```
- **Response**: 
  - **201 Created**: Student successfully created.
  - **400 Bad Request**: Invalid input for name.

#### 2. Get a Student by ID
- **Endpoint**: `GET /students/{id}`
- **Response**: 
  - **200 OK**: 
    ```json
    {
        "id": "integer",
        "name": "string"
    }
    ```
  - **404 Not Found**: Student does not exist.

#### 3. Update a Student
- **Endpoint**: `PUT /students/{id}`
- **Request Body**: 
  ```json
  {
      "name": "string"
  }
  ```
- **Response**: 
  - **200 OK**: Student successfully updated.
  - **400 Bad Request**: Invalid input for name.
  - **404 Not Found**: Student does not exist.

#### 4. Delete a Student
- **Endpoint**: `DELETE /students/{id}`
- **Response**: 
  - **204 No Content**: Student successfully deleted.
  - **404 Not Found**: Student does not exist.

### API Usage Example
```bash
# Create a new student
curl -X POST http://localhost:5000/students -H "Content-Type: application/json" -d '{"name": "John Doe"}'

# Get a student by ID
curl -X GET http://localhost:5000/students/1

# Update a student
curl -X PUT http://localhost:5000/students/1 -H "Content-Type: application/json" -d '{"name": "Jane Doe"}'

# Delete a student
curl -X DELETE http://localhost:5000/students/1
```

### Automatic Schema Creation
- The application will automatically generate the SQLite database schema on startup if it doesn't already exist, specifically for the Student entity.

---

## Tests

### Test Cases

#### Test: Delete Student Successfully
Implementing `test_delete_student_successfully`.

```python
def test_delete_student_successfully(client):
    # Arrange: Create a student first to ensure there's someone to delete
    response = client.post('/students', json={'name': 'Test Student'})
    assert response.status_code == 201
    student_id = response.json['id']

    # Act: Attempt to delete the student
    delete_response = client.delete(f'/students/{student_id}')

    # Assert: Check the response status code
    assert delete_response.status_code == 204

    # Confirm deletion by trying to retrieve the deleted student
    get_response = client.get(f'/students/{student_id}')
    assert get_response.status_code == 404
```

### Additional Notes
- Ensure to include additional test cases for all endpoints to maintain high test coverage.
- Follow README.md guidelines for running tests and more information on usage.