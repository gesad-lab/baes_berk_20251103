# API Specifications

## Overview
This document outlines the API specifications for the application. It provides details on the available endpoints, their methods, parameters, request and response formats, and error handling.

## Base URL
The base URL for the API is:

```
https://api.example.com/v1
```

## Endpoints

### 1. User Management

#### 1.1 Create User
- **Endpoint**: `/users`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "string",
    "email": "string",
    "password": "string"
  }
  ```
- **Response**:
  - **201 Created**:
    ```json
    {
      "id": "integer",
      "username": "string",
      "email": "string"
    }
    ```
  - **400 Bad Request** (if input validation fails):
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Invalid email format",
        "details": {}
      }
    }
    ```

#### 1.2 Get User
- **Endpoint**: `/users/{id}`
- **Method**: `GET`
- **URL Parameters**:
  - `id` (integer): ID of the user to retrieve.
- **Response**:
  - **200 OK**:
    ```json
    {
      "id": "integer",
      "username": "string",
      "email": "string"
    }
    ```
  - **404 Not Found** (if user does not exist):
    ```json
    {
      "error": {
        "code": "E002",
        "message": "User not found",
        "details": {}
      }
    }
    ```

### 2. Authentication

#### 2.1 User Login
- **Endpoint**: `/auth/login`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "email": "string",
    "password": "string"
  }
  ```
- **Response**:
  - **200 OK**:
    ```json
    {
      "token": "string"
    }
    ```
  - **401 Unauthorized** (if credentials are invalid):
    ```json
    {
      "error": {
        "code": "E003",
        "message": "Invalid credentials",
        "details": {}
      }
    }
    ```

### 3. Error Handling
All error responses follow the same structured format:
```json
{
  "error": {
    "code": "EXXX",
    "message": "Error description",
    "details": {} // Optional: Additional details about the error
  }
}
```

## Versioning
API versioning is implemented in the URL. Ensure to specify the correct version in requests to avoid compatibility issues.

## Conclusion
This document is intended to provide comprehensive information about the API endpoints available. For any additional features or endpoints, this document will be updated accordingly.