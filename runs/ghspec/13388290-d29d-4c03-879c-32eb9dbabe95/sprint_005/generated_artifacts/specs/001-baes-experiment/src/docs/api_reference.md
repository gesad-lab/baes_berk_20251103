# Updated API Documentation for `/teachers` Endpoints

# API Reference

## GET /teachers
### Description
Retrieve a list of all teachers.
- **Response**: Returns a JSON array of teacher objects, each containing the `id`, `name`, and `subject`.

### Example Response
```json
[
    {
        "id": 1,
        "name": "John Smith",
        "subject": "Mathematics"
    },
    {
        "id": 2,
        "name": "Jane Doe",
        "subject": "Science"
    }
]
```

## POST /teachers
### Description
Add a new teacher to the system.
- **Request Body**: Requires a JSON object with `name` and `subject`.

### Example Request
```json
{
    "name": "Alice Johnson",
    "subject": "History"
}
```

### Response
- **Status 201**: Returns the created teacher object with its `id`.
  
### Example Response
```json
{
    "id": 3,
    "name": "Alice Johnson",
    "subject": "History"
}
```

## GET /teachers/{id}
### Description
Retrieve information about a specific teacher by their ID.
- **Response**: Returns a JSON object representing the teacher.

### Example Response
```json
{
    "id": 1,
    "name": "John Smith",
    "subject": "Mathematics"
}
```

## PUT /teachers/{id}
### Description
Update the details of a specific teacher.
- **Request Body**: Can update the `name` and/or `subject` fields.

### Example Request
```json
{
    "name": "John Smith",
    "subject": "Advanced Mathematics"
}
```

### Response
- **Status 200**: Returns the updated teacher object.

### Example Response
```json
{
    "id": 1,
    "name": "John Smith",
    "subject": "Advanced Mathematics"
}
```

## DELETE /teachers/{id}
### Description
Remove a teacher from the system by their ID.
- **Response**: Status 204 for successful deletion, with no content returned.

### Error Responses
- **Status 404**: Teacher not found.

## Conclusion
These endpoints allow for full CRUD operations (Create, Read, Update, Delete) on teacher records in the application. Ensure all requests are properly authenticated, and adherence to formats specified above is maintained.

--- 

# Note
This documentation represents a high-level overview of the newly added `/teachers` endpoints. Please ensure that the implementations behind these endpoints follow the specified behaviors. 

---

# README.md Updates
- Update the setup instructions to include how to test the `/teachers` endpoints using the testing framework specified in the previous sprint files.