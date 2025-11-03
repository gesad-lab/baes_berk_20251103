# Updated README.md

# README.md

## Student API

This API allows for the management of student entities, including creating and retrieving student information. 

### Endpoints

#### POST /students

Creates a new student in the database.

**Request Body**:
```json
{
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```

**Response**:
- **Success (201 Created)**:
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    ```
- **Error (400 Bad Request)** when email is missing:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Email is required."
        }
    }
    ```

### Database Schema

The `students` table includes the following fields:
- `id`: Integer (Primary Key)
- `name`: String (not null)
- `email`: String (not null)

*Note: Ensure the email field is provided when creating a student. The application will return a 400 error if the email is missing.*

### Migration Steps

Upon startup, the database schema will be automatically updated to include the email field for the `students` table. Existing student records will remain unaffected during this migration. 

Make sure to apply any database migrations using your preferred migration strategy or framework integrated with your application.

### Error Handling

The API will respond with validation errors for invalid input, including a missing email. Please ensure all required fields are included in the request body to avoid errors.