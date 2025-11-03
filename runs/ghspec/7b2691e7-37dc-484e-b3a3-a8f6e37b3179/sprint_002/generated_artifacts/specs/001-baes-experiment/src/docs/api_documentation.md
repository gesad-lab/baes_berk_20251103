---
# Updated api_documentation.md

## API Documentation

### Creating a Student

#### Endpoint
`POST /students`

#### Request Payload
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

#### Responses
- **201 Created**: Successfully created student record with the following response:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```
- **400 Bad Request**: If the request is missing the 'name' field or 'email' field (if validation fails), the response will indicate the issue:
  ```json
  {
    "error": {
      "code": "E001",
      "message": "Name is required."
    }
  }
  ```

### Creating a Student without Email

#### Request Payload
```json
{
  "name": "Jane Doe"
}
```

#### Responses
- **201 Created**: Successfully created student record without email:
  ```json
  {
    "id": 2,
    "name": "Jane Doe",
    "email": null
  }
  ```

### Retrieving a Student’s Email

#### Endpoint
`GET /students/{id}`

#### Responses
- **200 OK**: Successfully retrieved student record:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```
- **404 Not Found**: If no student exists with the given ID:
  ```json
  {
    "error": {
      "code": "E002",
      "message": "Student not found."
    }
  }
  ```

### Validation of Email Format

#### Request Payload
```json
{
  "name": "John Doe",
  "email": "invalid_email_format"
}
```

#### Responses
- **400 Bad Request**: If provided email format is invalid:
  ```json
  {
    "error": {
      "code": "E003",
      "message": "Invalid email format."
    }
  }
  ```

### Additional Considerations

#### Error Handling
All error responses must be structured as:
```json
{
  "error": {
    "code": "EXXX",
    "message": "Descriptive error message."
  }
}
```

#### Sanitization and Security
Ensure that all inputs to the `/students` endpoint are sanitized to prevent SQL injection attacks and that error messages do not expose sensitive application information.

### Testing Coverage
Ensure that the following test cases are included:
1. Attempt creating a student with valid name and valid email address.
2. Attempt creating a student without an email.
3. Retrieve a student’s information by valid ID.
4. Attempt to create a student with an invalid email format.

All potential input cases must be thoroughly tested and documented to ensure comprehensive coverage of the API behaviors.