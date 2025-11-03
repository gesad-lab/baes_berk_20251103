# README.md

# Student Management System

## Overview
The Student Management System is a FastAPI application designed to manage student records efficiently. This API enables the creation, retrieval, updating, and deletion of student records.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/student_management.git
   cd student_management
   ```

2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Initialize the database:
   - Run the migration scripts to set up the database schema.

## Endpoints

### Student Management

#### Create Student
- **Endpoint**: `POST /students`
- **Request Body**:
  ```json
  {
    "name": "string",
    "email": "string"  // New field added in this implementation
  }
  ```
- **Response**:
  - **201 Created** on successful creation.
  - **400 Bad Request** if the request is invalid (e.g., missing fields).

#### Retrieve Students
- **Endpoint**: `GET /students`
- **Response**:
  ```json
  [
    {
      "id": "integer",
      "name": "string",
      "email": "string"  // New field added in response schema
    }
  ]
  ```
  
## Database Migration
In addition to the existing fields, the following SQL migration has been implemented to add an `email` field to the existing `students` table:
```sql
ALTER TABLE students ADD COLUMN email STRING NOT NULL;
```

## Out of Scope
- User authentication and authorization related to email addresses.
- Additional features for sending emails or notifications to students.
- Front-end interface changes for student creation or viewing records; this feature focuses solely on backend API functionality.

## Testing
Ensure that the following scenarios are covered in the tests:
- Successful student creation including the email field.
- Retrieval of all students, confirming the presence of the email field.
- Handling of invalid requests missing the email field.

## Conclusion
This project is designed as a backend-centric application. Feel free to contribute by improving existing features or adding new functionalities that align with the core objectives. 

For more information or to report issues, please open an issue on the repository page.