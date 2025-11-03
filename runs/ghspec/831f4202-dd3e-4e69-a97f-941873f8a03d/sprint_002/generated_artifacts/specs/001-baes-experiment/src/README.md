# Updated README.md

## Student Management Application

### Overview
The Student Management Application allows users to create, retrieve, and manage student records efficiently. 

### API Endpoints

#### 1. Create a New Student

- **Endpoint**: `POST /students`
- **Description**: Creates a new student record.
- **Request Body**:
  - `name`: String, required - The student's name.
  - `email`: String, required, must be a valid email format - The student's email address.

##### Example Request:
```json
{
  "name": "Jane Doe",
  "email": "jane.doe@example.com"
}
```

- **Response**: 
  - **201 Created**: Returns the created student object.
  - **400 Bad Request**: Returns an error if the input is invalid.

#### 2. Retrieve All Students

- **Endpoint**: `GET /students`
- **Description**: Retrieves a list of all student records.
- **Response**:
  - **200 OK**: Returns an array of student objects, including their email addresses.

##### Example Response:
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

### Email Field Requirements
- The email field is mandatory for creating a new student record.
- The application will validate the email format as per standard practices.
- Existing student records were preserved during the addition of the email field through a database migration.

### Database Updates
- The Student entity has been updated to include the following fields:
  - `id`: Integer, primary key, auto-increment.
  - `name`: String, required.
  - `email`: String, required, validated against standard email formatting.

### Migration Process
The database migration ensures that existing student data remains intact while the new email field is introduced. Please follow the migration instructions in the setup guide.

### Setup Instructions
1. Install the required dependencies.
2. Initialize the SQLite database by running the application.
3. Use the provided API endpoints to manage student records.

### Usage
Refer to the API documentation for complete usage examples and further details.

### License
This project is licensed under the MIT License - see the LICENSE file for details.