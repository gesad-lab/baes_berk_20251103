# Updated README.md

# Project Title

*Brief description of the project.*

## API Documentation

### Teachers

The new `/teachers` routes have been added to manage teacher entities. Below are the details of the routes.

#### GET /teachers

- **Description**: Retrieve a list of all teachers in the system.
- **Response**:
  - **200 OK**: Returns an array of teacher objects.
    ```json
    [
      {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "subject": "Mathematics"
      },
      {
        "id": 2,
        "name": "Jane Smith",
        "email": "janesmith@example.com",
        "subject": "Science"
      }
    ]
    ```

#### POST /teachers

- **Description**: Create a new teacher in the system.
- **Request Body**:
  ```json
  {
    "name": "New Teacher",
    "email": "newteacher@example.com",
    "subject": "History"
  }
  ```
- **Response**:
  - **201 Created**: Returns the created teacher object.
    ```json
    {
      "id": 3,
      "name": "New Teacher",
      "email": "newteacher@example.com",
      "subject": "History"
    }
    ```
  - **400 Bad Request**: Returns error details if validation fails.
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Invalid email format",
        "details": {}
      }
    }
    ```

## Database Schema Updates

The database schema has been updated to include the new `Teacher` entity. The `Teacher` entity has the following fields:

- **id**: Integer, Primary Key
- **name**: String, Name of the teacher
- **email**: String, Email address of the teacher
- **subject**: String, Subject taught by the teacher
- **created_at**: Timestamp, Record creation date
- **updated_at**: Timestamp, Record update date

Refer to the migration files for details on how to set up the database with the new schema.

## Installation

*Instructions for setting up the project environment.*

## Usage

*Instructions for how to use the project.*

## Contributing

*Instructions for contributing to the project.*

## License

*License information.*