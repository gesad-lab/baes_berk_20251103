# File: docs/api_spec.md

# API Specification Documentation

## Overview

This document outlines the API routes available for managing courses, along with their expected request and response formats. It serves as a guide for developers to understand and use the API effectively.

## API Endpoints

### 1. Create a Course

- **URL**: `/courses`
- **Method**: `POST`
- **Request Body**:
```json
{
    "name": "Mathematics",
    "description": "An advanced course in mathematics."
}
```
- **Response**:
  - **Status Code**: `201 Created`
  - **Response Body**:
    ```json
    {
        "id": 1,
        "name": "Mathematics",
        "description": "An advanced course in mathematics."
    }
    ```

### 2. Retrieve a Course

- **URL**: `/courses/{course_id}`
- **Method**: `GET`
- **Path Parameters**:
  - `course_id` (integer): ID of the course to retrieve.
- **Response**:
  - **Status Code**: `200 OK`
  - **Response Body**:
    ```json
    {
        "id": 1,
        "name": "Mathematics",
        "description": "An advanced course in mathematics."
    }
    ```

### 3. Update a Course

- **URL**: `/courses/{course_id}`
- **Method**: `PUT`
- **Path Parameters**:
  - `course_id` (integer): ID of the course to update.
- **Request Body**:
```json
{
    "name": "Mathematics Basic",
    "description": "An introductory course in mathematics."
}
```
- **Response**:
  - **Status Code**: `200 OK`
  - **Response Body**:
    ```json
    {
        "id": 1,
        "name": "Mathematics Basic",
        "description": "An introductory course in mathematics."
    }
    ```

### 4. Delete a Course

- **URL**: `/courses/{course_id}`
- **Method**: `DELETE`
- **Path Parameters**:
  - `course_id` (integer): ID of the course to delete.
- **Response**:
  - **Status Code**: `204 No Content`

## Database Schema Updates

- New relationships have been established in the database schema to accommodate the updated API functionality. For detailed information on these updates, please refer to the `README.md` file in the project root.

## Conclusion

This API documentation provides the necessary information for developers to integrate with the course management system effectively. Ensure to follow the structure and format specified to maintain consistency across the API.