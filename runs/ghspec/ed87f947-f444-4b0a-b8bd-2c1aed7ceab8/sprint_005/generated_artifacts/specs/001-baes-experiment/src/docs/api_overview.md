# docs/api_overview.md

# API Overview

## Endpoints

### Teachers

#### Create a Teacher

- **POST** `/teachers`
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
- **Description**: Creates a new teacher with the provided name and email. The email must be unique.

#### Retrieve Teacher Details

- **GET** `/teachers/{teacherId}`
- **Response** (200 OK):
  ```json
  {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
  }
  ```
- **Description**: Retrieves detailed information about a specific teacher by their unique ID.

#### Update a Teacher

- **PUT** `/teachers/{teacherId}`
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
- **Description**: Updates the information of an existing teacher. Both name and email fields must be provided.

#### Delete a Teacher

- **DELETE** `/teachers/{teacherId}`
- **Response** (204 No Content):
- **Description**: Deletes a teacher from the system by their unique ID.

## Integration with Existing Systems

- The `teachers` table has been integrated into the database schema, enabling CRUD operations through the above API endpoints. Each teacher entry must have unique email addresses to maintain data integrity.
  
- Logging and error handling are implemented to ensure smooth operations and provide feedback in case of issues. 

- Automated tests have been written to ensure that these endpoints meet the required functionality with a focus on error handling and edge cases. 

### Testing Notes

- Ensure at least 70% coverage for the `Teacher` management functionalities, especially for create, update, and delete operations to maintain code quality.

This documentation will help understand and implement operations related to teachers within the application.