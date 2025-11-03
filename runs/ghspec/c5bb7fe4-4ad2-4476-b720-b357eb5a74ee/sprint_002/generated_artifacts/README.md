# README.md

# Student Management Web Application

## API Documentation

### Student Creation with Email
- **Endpoint**: `POST /students`
- **Request Body**:
  - **Required**:
    - `name` (string)
    - `email` (string, required)
- **Response**:
  - **Status**: `201 Created`
  - **Body**: JSON representation of the created Student including email.

**Example Request**:
```json
{
  "name": "Jane Doe",
  "email": "jane.doe@example.com"
}
```

**Example Response**:
```json
{
  "id": 1,
  "name": "Jane Doe",
  "email": "jane.doe@example.com"
}
```

### Retrieve All Students
- **Endpoint**: `GET /students`
- **Response**:
  - **Status**: `200 OK`
  - **Body**: JSON array of Student objects including email.

**Example Response**:
```json
[
  {
    "id": 1,
    "name": "Jane Doe",
    "email": "jane.doe@example.com"
  },
  {
    "id": 2,
    "name": "John Smith",
    "email": "john.smith@example.com"
  }
]
```

### Update Existing Student Email
- **Endpoint**: `PUT /students/{id}`
- **Request Body**:
  - **Required**:
    - `email` (string, required)
- **Response**:
  - **Status**: `200 OK`
  - **Body**: JSON representation of the updated Student including email.

**Example Request**:
```json
{
  "email": "jane.updated@example.com"
}
```

**Example Response**:
```json
{
  "id": 1,
  "name": "Jane Doe",
  "email": "jane.updated@example.com"
}
```

### Database Schema Update
To accommodate the new email field in the Student entity:
- The email field will be a string and is required.
- Ensure that the migration preserves all existing Student data without loss.

### Running Migrations
To run migrations as part of the deployment process, use the following command:
```bash
flask db upgrade
```
Ensure that your database connection string is set in the environment variables as follows:

```bash
export DATABASE_URL="your_database_connection_string"
```

### Environment Variables
Make sure to configure the following environment variable before running the application:
- `DATABASE_URL`: The connection string for your database.

### Notes
- Ensure that all API functions are well-documented, especially regarding email handling.
- Further updates on API contracts and usage examples will be documented as more features are added.