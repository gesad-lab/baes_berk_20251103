# Updated Documentation for Teacher API

## Teacher API Documentation

### Endpoints

#### 1. Create a Teacher

- **Endpoint**: `/api/teachers`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    ```
- **Success Response**:
    - **Code**: `201 Created`
    - **Content**:
        ```json
        {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com"
        }
        ```
- **Error Responses**:
    - **Code**: `400 Bad Request`
        - **Content**:
            ```json
            {
                "error": {
                    "code": "E001",
                    "message": "Invalid email format."
                }
            }
            ```
        - **Explanation**: The request body is missing required fields or contains an invalid email format.
        
#### 2. Get Teacher Details

- **Endpoint**: `/api/teachers/<id>`
- **Method**: `GET`
- **URL Parameters**:
    - `id` (integer) - The ID of the teacher to retrieve.
- **Success Response**:
    - **Code**: `200 OK`
    - **Content**:
        ```json
        {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com"
        }
        ```
- **Error Responses**:
    - **Code**: `404 Not Found`
        - **Content**:
            ```json
            {
                "error": {
                    "code": "E002",
                    "message": "Teacher not found."
                }
            }
            ```
        - **Explanation**: The provided Teacher ID does not exist in the database.

### Validation Checks
When creating a Teacher, the API will validate:
- The presence of required fields (`name` and `email`).
- The format of the email must conform to standard email format rules.

### JSON Response Format
All responses will be in JSON format, containing fields for Teacher ID, name, and email as specified.

### Schema for Teacher Table
The database schema for the Teacher table will include:
- `ID` (Integer, Auto-incremented Primary Key)
- `Name` (String, Required)
- `Email` (String, Required)

### Overview
This Document outlines the specifications for the Teacher API endpoints, detailing how to create and retrieve teacher entries in the system. Ensure adherence to the validation rules to avoid erroneous submissions.

---

**Note**: Make sure to test all endpoints and ensure proper error handling is implemented in the application to reflect the documented behaviors.