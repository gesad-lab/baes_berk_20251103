# Update API documentation to include the email field

# File: docs/api_reference.md

## API Reference

### Student Entity

The Student entity represents an individual within the system with associated attributes for managing their information and communications.

#### Attributes

- **id**: (integer) A unique identifier for each student.
- **name**: (string) The name of the student.
- **email**: (string, required) The email address of the student. This field must conform to a standard email format. Invalid or unauthorized email inputs will trigger an error response.

#### Responses

All API responses related to the Student entity will now include the `email` field where applicable. Below are the updated JSON response formats:

**Successful Creation of a Student**:
```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```

**Successful Retrieval of a Student**:
```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```

**Successful Update of a Student**:
```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```

#### Error Responses

In case of errors related to the email input, the following format will be returned:

```json
{
    "error": {
        "code": "E001",
        "message": "Invalid email format.",
        "details": {}
    }
}
```

### Implementation Details

1. **Email Validation**:
   - The application will perform email validation to ensure all email inputs conform to the standard format.
   - If invalid, a `400 Bad Request` status will be returned with the appropriate error message.

2. **Database Migration**:
   - The database schema has been updated to include the new `email` field in the `Student` table, ensuring no loss of existing data.

3. **Testing**:
   - Tests will verify that creating, retrieving, and updating Students with the email field return the expected JSON responses.
   - Validation errors will return appropriate status codes (e.g., `400 Bad Request` for invalid email formats).

### Migration Instructions

When deploying updates that include the new email field, please ensure to follow these migration steps to preserve existing data:

- Generate a new migration using Alembic for the schema update.
- Verify that the migration retains all existing Student data while adding the new email field to the schema.

### Conclusion

This update enhances the Student entity by incorporating an email field, allowing better communication and notification management for students. This change also includes necessary validations and structured error handling to maintain data integrity and improve user experience.