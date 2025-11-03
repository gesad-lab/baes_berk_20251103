```markdown
# README.md

# Student Management Web Application

## Overview

The Student Management Web Application provides a RESTful API for managing students. Users can create, retrieve, update, and delete student records. 

## API Endpoints

### Create Student

- **Endpoint**: `POST /students`
- **Request Body**: 
```json
{
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```
- **Response**: 
```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```

### Retrieve Student

- **Endpoint**: `GET /students/{id}`
- **Response**: 
```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```

## Database Migration

The database includes an `email` field that must be present for all student records. During migration, the system ensures that existing records are preserved, and all new records must include a valid `email`. 

## Assertions for Data Integrity

After running the migration, the following assertions are made to ensure that the `email` field is present and that data integrity is maintained:

1. **Verify Email Presence**: On creating or updating a student, the `email` field must be included in the response body.
2. **Data Integrity Check**: When retrieving a student, verify that the email is a non-empty string and conforms to standard email format.

## User Scenario Testing

### Successful Creation with Email

When a valid name and email are provided, the API will return the created student's details, confirming that the `email` field has been integrated correctly into the data model.

### Invalid Email Handling

If an invalid email format is detected when creating or updating a student, the API will respond with a 400 status code and a descriptive error message indicating that the email field is required and must adhere to proper formatting.

## Additional Notes

- Review API endpoint usage and error handling in `README.md`.
- Ensure comprehensive testing in the relevant files to maintain high standards of quality and integrity.

```