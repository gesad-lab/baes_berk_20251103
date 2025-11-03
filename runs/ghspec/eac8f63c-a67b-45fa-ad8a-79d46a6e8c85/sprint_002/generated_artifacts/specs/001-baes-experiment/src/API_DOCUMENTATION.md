# API_DOCUMENTATION.md

# API Documentation

## Endpoints

### Create Student

**POST** `/students`

#### Description
Creates a new student record in the system.

#### Request Body
- `name` (string, required): The name of the student.
- `age` (integer, required): The age of the student.
- `email` (string, required): The email address of the student.

#### Responses
- **201 Created**: Returns the created student object.
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "age": 20,
        "email": "john.doe@example.com"
    }
    ```
- **400 Bad Request**: Returns an error if the request data is invalid.
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Invalid email format",
            "details": {}
        }
    }
    ```
- **400 Bad Request**: Returns an error if required fields are missing.
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Missing required field: email",
            "details": {}
        }
    }
    ```

### Other Endpoints
- Documentation of other endpoints can be found below this section.

## Usage Notes
Make sure to provide all required fields when creating a student. Email validation is enforced, so ensure that the format is correct to avoid errors when submitting requests.