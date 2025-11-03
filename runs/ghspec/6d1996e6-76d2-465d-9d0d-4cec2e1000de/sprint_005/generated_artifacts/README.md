# Updated README.md for Teacher API

# Teacher API

This API allows for management of teacher information including creating, retrieving, and updating teacher records. 

## User Scenarios & Testing

1. **Creating a New Teacher**:
   - Given the user has access to the application, when they provide valid name and email for a new teacher, a new teacher entry will be created in the database.

2. **Retrieving Teacher Information**:
   - Given the user requests a teacher by ID, when the teacher exists in the database, the application will return the teacher’s information, including their name and email in JSON format.

3. **Error Handling for Teacher Creation**:
   - Given the user tries to create a teacher with a missing name or email, the application will return a clear error message indicating the problem.

4. **Updating Teacher Information**:
   - Given the user needs to update a teacher's email or name, when valid updates are provided, the application will successfully update the teacher's information.

## Functional Requirements

1. **Create Teacher**:
   - **Endpoint**: POST `/teachers`
   - **Request Body**: JSON object containing:
     - `"name"`: (string, required)
     - `"email"`: (string, required)
   - **Response**: 
     - `201 Created` with the newly created teacher object in JSON format.

2. **Retrieve Teacher**:
   - **Endpoint**: GET `/teachers/{id}`
   - **Response**: 
     - `200 OK` with the teacher object including their details in JSON format, or `404 Not Found` if the ID does not exist.

3. **Update Teacher**:
   - **Endpoint**: PUT `/teachers/{id}`
   - **Request Body**: JSON object containing updated:
     - `"name"`: (string, optional)
     - `"email"`: (string, optional)
   - **Response**: 
     - `200 OK` with the updated teacher object in JSON format, or `404 Not Found` if the teacher ID does not exist.

## Database Schema

The database schema includes a new Teacher table with the following columns:
- `id`: Integer, auto-generated primary key.
- `name`: String, required.
- `email`: String, required.

## Success Criteria

The application must correctly respond to all endpoints related to creating, retrieving, and updating teacher information as specified above.

## Dependencies

The API is built using the following dependencies:
- **Package Manager**: pip
- Ensure to update the `requirements.txt` to include any new dependencies required for the Teacher service.

## Setup

To set up the project, follow the steps in the installation guide provided in the main repository. Make sure to configure the environment variables required for database connectivity and dependencies.

---

For further details on usage and error handling, refer to the complete API documentation or contact the development team.