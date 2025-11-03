# README.md

## Project Overview

This project is a FastAPI application that manages student records. It provides endpoints to create, retrieve, and update student information.

## API Documentation

### 1. Create Student (`POST /students`)
- **Request**: 
```json
{
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```
- **Response** (201 Created):
```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```
- **Description**: This endpoint allows the creation of a new student. The request must include both the `name` and `email`. The `email` is required and must be a valid email format.

### 2. Retrieve Student (`GET /students/{id}`)
- **Response** (200 OK):
```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```
- **Description**: This endpoint retrieves a student record by its unique ID.

### 3. Update Student (`PUT /students/{id}`)
- **Request**:
```json
{
    "name": "Jane Doe",
    "email": "jane.doe@example.com"
}
```
- **Response** (200 OK):
```json
{
    "id": 1,
    "name": "Jane Doe",
    "email": "jane.doe@example.com"
}
```
- **Description**: This endpoint updates an existing student's information. Both the `name` and `email` fields can be updated.

## Database Migration

To support the new `email` field:

1. **Migration Script**: Create a migration script to add the `email` column to the existing Student table using Alembic or a similar tool.
```sql
ALTER TABLE students ADD COLUMN email VARCHAR NOT NULL;
```

## Testing

- Ensure that new unit tests are written to validate email formatting and the behavior of the updated API endpoints.
- Aim for a minimum of 70% coverage for new features.

## Conclusion

This README outlines the API, the structure of the student records, and important changes required due to the introduction of the `email` column in the Student model. Please ensure all updates are reflected in the relevant codebase and tests.