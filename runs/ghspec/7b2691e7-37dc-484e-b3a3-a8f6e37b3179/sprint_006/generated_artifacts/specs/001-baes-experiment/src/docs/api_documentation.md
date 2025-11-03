# docs/api_documentation.md

## API Documentation

### Overview
This documentation provides information on the API endpoints available in the application, including request parameters and response formats.

### Teachers API

#### Create Teacher
- **Endpoint**: `POST /teachers`
- **Description**: Creates a new teacher.
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```
- **Response**:
  - **201 Created**: Returns the created teacher object.
  - **400 Bad Request**: Returns validation errors.

#### Get Teacher
- **Endpoint**: `GET /teachers/{teacherId}`
- **Description**: Retrieves details of a specific teacher by ID.
- **Response**:
  - **200 OK**: Returns the teacher object.
  - **404 Not Found**: Teacher with the specified ID does not exist.

### Courses API

#### Assign Teacher to Course
- **Endpoint**: `POST /courses/{courseId}/assign-teacher`
- **Description**: Assigns a teacher to a course by their respective IDs.
- **Request Body**:
  ```json
  {
    "teacher_id": 1
  }
  ```
- **Response**:
  - **200 OK**: Returns a confirmation message indicating the teacher has been assigned.
  - **400 Bad Request**: Returns validation errors (e.g., invalid course ID or teacher ID).
  - **404 Not Found**: Returns an error if the specified course or teacher does not exist.

### Error Handling
All endpoints return standardized error responses in the following format:
```json
{
  "error": {
    "code": "E001",
    "message": "Invalid teacher ID",
    "details": {}
  }
}
```

### Setup Instructions
To set up the development environment for this API:
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install Flask SQLAlchemy Marshmallow pytest
   ```

### Additional Notes
Make sure to run database migrations before starting the application to ensure all models and relationships are up to date. Use Alembic for managing migrations, particularly after adding new fields or making structural changes to the database.
