# README.md

# Project Title

## Overview

This project implements various APIs to manage students, courses, and enrollment processes. The focus of the current development sprint is to extend functionalities to include Teacher APIs, enhancing the system's ability to manage educational resources effectively.

## Teacher API Endpoints

### 1. Create Teacher

- **Endpoint**: `/teachers`
- **Method**: `POST`
- **Request Format**:
    ```json
    {
        "name": "John Doe",
        "subject": "Mathematics",
        "email": "john.doe@example.com"
    }
    ```
- **Response Format**:
    - **201 Created**:
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "subject": "Mathematics",
        "email": "john.doe@example.com"
    }
    ```
    - **400 Bad Request**:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Invalid teacher data."
        }
    }
    ```

### 2. Get Teacher by ID

- **Endpoint**: `/teachers/{teacher_id}`
- **Method**: `GET`
- **Response Format**:
    - **200 OK**:
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "subject": "Mathematics",
        "email": "john.doe@example.com"
    }
    ```
    - **404 Not Found**:
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Teacher not found."
        }
    }
    ```

### 3. Update Teacher

- **Endpoint**: `/teachers/{teacher_id}`
- **Method**: `PUT`
- **Request Format**:
    ```json
    {
        "name": "John Doe",
        "subject": "Physics",
        "email": "john.doe@example.com"
    }
    ```
- **Response Format**:
    - **200 OK**:
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "subject": "Physics",
        "email": "john.doe@example.com"
    }
    ```
    - **404 Not Found**:
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Teacher not found."
        }
    }
    ```

### 4. Delete Teacher

- **Endpoint**: `/teachers/{teacher_id}`
- **Method**: `DELETE`
- **Response Format**:
    - **204 No Content**:
    - **404 Not Found**:
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Teacher not found."
        }
    }
    ```

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo.git
    cd your-repo
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the database:
    ```bash
    # Make sure to configure your database settings
    ```

4. Start the application:
    ```bash
    uvicorn main:app --reload
    ```

## Testing

To run the tests, use the following command:
```bash
pytest tests/
```

## CHANGELOG

### [1.0.0] - 2023-10-10
- Initial implementation of Student and Course APIs.

### [1.1.0] - 2023-10-15
- Added Teacher API endpoints for creating, retrieving, updating, and deleting teachers.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

Thank you for being part of our project. Contributions are welcome!