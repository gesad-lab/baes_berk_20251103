# README.md

# Teacher Management API

## Overview

This API allows you to create and retrieve `Teacher` resources. Teachers are associated with courses where they can facilitate learning.

## API Endpoints

### Create a Teacher

- **Endpoint:** `/teachers`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "name": "John Doe",
        "subject": "Mathematics"
    }
    ```
- **Response:**
    - **Status Code:** `201 Created`
    - **Response Body:**
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "subject": "Mathematics"
    }
    ```

### Retrieve a Teacher

- **Endpoint:** `/teachers/{id}`
- **Method:** `GET`
- **URL Parameters:**
    - `id` (integer): The ID of the teacher to retrieve.
- **Response:**
    - **Status Code:** `200 OK`
    - **Response Body:**
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "subject": "Mathematics"
    }
    ```

## Examples

### Example Request to Create a Teacher

```bash
curl -X POST http://localhost:8000/teachers \
-H "Content-Type: application/json" \
-d '{"name": "John Doe", "subject": "Mathematics"}'
```

### Example Response

```json
{
    "id": 1,
    "name": "John Doe",
    "subject": "Mathematics"
}
```

### Example Request to Retrieve a Teacher

```bash
curl -X GET http://localhost:8000/teachers/1
```

### Example Response

```json
{
    "id": 1,
    "name": "John Doe",
    "subject": "Mathematics"
}
```

## Error Handling

Errors will be returned in a consistent format:

- **Example Error Response:**
```json
{
    "error": {
        "code": "E001",
        "message": "Teacher not found",
        "details": {}
    }
}
```

## Conclusion

This API is designed to allow easy management of teacher resources within the system. By following the examples provided, you can seamlessly create and retrieve teacher information.