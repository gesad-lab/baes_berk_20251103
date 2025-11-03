# README.md

# Project Title

## Overview

This project is designed to manage Student entities through a RESTful API. The application allows for the creation, retrieval, and management of student data.

## Email Field Addition

As part of recent updates, the Student entity now includes an email field. Below are important changes to the API functionality regarding this new field.

### Updated Student Entity

The Student entity has been modified to include the following fields:
- **name**: (string, required)
- **email**: (string, required)

### API Endpoints

#### POST /students

This endpoint allows the creation of a new student. The request must include both the name and email fields.

**Request Body:**
```json
{
    "name": "string",
    "email": "string"
}
```
Both fields are required when creating a new student entity.

#### GET /students

This endpoint retrieves a list of all students. The returned data will include name and email information.

**Response Format:**
```json
[
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "email": "jane.smith@example.com"
    }
]
```

### Database Changes

The database schema for the Student entity has been updated to incorporate the new email field. A migration strategy has been implemented to ensure that existing student data is preserved during this schema update.

### Migration Details

The migration will add the email column to the Student table, ensuring that no existing data is lost and that the application continues to operate smoothly.

## Documentation Updates

Automatic API documentation generated using FastAPI’s built-in OpenAPI support has also been updated to reflect new fields and endpoints.

## Conclusion

The addition of the email field enhances the functionality of the Student entity and allows for more comprehensive data management through the API. Further enhancements related to email functionalities will be considered in future sprints.