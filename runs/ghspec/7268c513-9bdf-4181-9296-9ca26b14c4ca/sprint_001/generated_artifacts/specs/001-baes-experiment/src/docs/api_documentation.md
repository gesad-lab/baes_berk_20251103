# API Documentation for the Project

This documentation provides an overview of the API endpoints available in the application. The API is built using Flask and follows RESTful principles.

## Base URL

```plaintext
http://<host>:<port>/api/v1
```

## Authentication

- The API uses token-based authentication. Clients must include a valid token in the `Authorization` header for protected endpoints.

## Endpoints

### 1. User Management

#### Create User

- **Endpoint**: `/users`
- **Method**: `POST`
- **Description**: Create a new user.
- **Request Body**:
    - `username` (string, required): The user's username.
    - `email` (string, required): The user's email address.
    - `password` (string, required): The user's password.
- **Responses**:
    - `201 Created`: User created successfully.
    - `400 Bad Request`: Invalid input data.

#### Get User

- **Endpoint**: `/users/<user_id>`
- **Method**: `GET`
- **Description**: Retrieve details of a specific user.
- **Path Parameters**:
    - `user_id` (integer, required): The ID of the user to retrieve.
- **Responses**:
    - `200 OK`: User details retrieved successfully.
    - `404 Not Found`: User not found.

#### Update User

- **Endpoint**: `/users/<user_id>`
- **Method**: `PUT`
- **Description**: Update the user's information.
- **Path Parameters**:
    - `user_id` (integer, required): The ID of the user to update.
- **Request Body**:
    - `username` (string, optional): Updated username.
    - `email` (string, optional): Updated email address.
    - `password` (string, optional): Updated password.
- **Responses**:
    - `200 OK`: User updated successfully.
    - `404 Not Found`: User not found.

#### Delete User

- **Endpoint**: `/users/<user_id>`
- **Method**: `DELETE`
- **Description**: Delete a specific user.
- **Path Parameters**:
    - `user_id` (integer, required): The ID of the user to delete.
- **Responses**:
    - `204 No Content`: User deleted successfully.
    - `404 Not Found`: User not found.

### 2. Authentication

#### User Login

- **Endpoint**: `/auth/login`
- **Method**: `POST`
- **Description**: Log in a user and retrieve an authentication token.
- **Request Body**:
    - `email` (string, required): User's email address.
    - `password` (string, required): User's password.
- **Responses**:
    - `200 OK`: Login successful, token returned.
    - `401 Unauthorized`: Invalid credentials.

#### Logout

- **Endpoint**: `/auth/logout`
- **Method**: `POST`
- **Description**: Log out the current user (invalidate the token).
- **Responses**:
    - `200 OK`: Logout successful.

## Error Handling

All error responses have the following structure:

```json
{
  "error": {
    "code": "<error_code>",
    "message": "<error_message>",
    "details": {}
  }
}
```

## Versioning

The API is versioned using the URL, with the current version being `v1`.

## Conclusion

This API documentation should help developers integrate with the provided endpoints efficiently. For any issues or questions, please reach out to the development team.