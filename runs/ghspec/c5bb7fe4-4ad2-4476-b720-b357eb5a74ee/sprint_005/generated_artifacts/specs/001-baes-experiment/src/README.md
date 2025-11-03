# README.md

# Project Overview

This project provides an API for managing educational entities such as Students, Courses, and Teachers. The API allows for creating, retrieving, and updating records, and follows RESTful principles.

## User Scenarios & Testing

1. **Adding a Teacher**: 
   - As an admin user, I want to create a new teacher record by providing their name and email.
   - *Testing*: Verify that when valid name and email values are submitted, the teacher record is created successfully in the database.

2. **Retrieving Teacher Details**: 
   - As a user, I want to view the information of a specific teacher by querying the system.
   - *Testing*: Verify that fetching a specific teacher's record returns accurate details including their name and email.

3. **Updating Teacher Information**: 
   - As an admin user, I want to update the name and/or email of an existing teacher.
   - *Testing*: Verify that when valid updates are made to a teacher's name or email, the changes are reflected in the teacher's stored data.

4. **Error Handling for Invalid Teacher Data**: 
   - As an admin user, I want to receive informative error messages if I attempt to create a teacher without mandatory fields.
   - *Testing*: Ensure that submitting incomplete data prompts appropriate error responses.

## Functional Requirements

1. **Create New Teacher**
   - Endpoint: `POST /teachers`
   - Request Body: 
     - Required:
       - `name` (string)
       - `email` (string)
   - Response: 
     - Status: `201 Created`
     - Body: JSON representation of the created Teacher.

2. **Retrieve Teacher**
   - Endpoint: `GET /teachers/{id}`
   - Response:
     - Status: `200 OK`
     - Body: JSON representation of the Teacher, including name and email.

3. **Update Teacher**
   - Endpoint: `PUT /teachers/{id}`
   - Request Body: 
     - Optional:
       - `name` (string)
       - `email` (string)
   - Response: 
     - Status: `200 OK`
     - Body: JSON representation of the updated Teacher.

4. **Database Schema Update**
   - The database schema must be updated to include a new Teacher table with the following fields:
     - `id` (integer, auto-incremented primary key)
     - `name` (string, required)
     - `email` (string, required)

## API Endpoints

### Teachers

- `POST /teachers`: Create a new teacher record.
- `GET /teachers/{id}`: Retrieve a specific teacher's details.
- `PUT /teachers/{id}`: Update an existing teacher's information.

### Error Handling

- Ensure informative error messages are returned when:
  - Required fields are missing during creation.
  - Invalid email formats are provided.

## Testing

Each user scenario should be accompanied by appropriate tests. It is advised to cover the following:

- Unit tests for each API endpoint.
- Integration tests to check interactions between components, especially for creating and updating teachers.

## Development Notes

To maintain project structure, the following changes will be made in the next iterations:

1. Introduce a `Teacher` model in `src/models/teacher.py`.
2. Implement API handling in `src/api/teacher_api.py`.
3. Scaffold business logic in `src/services/teacher_service.py`.
4. Follow the migration plan using Alembic for the `teachers` table creation.

For any further modifications or enhancements, follow the project's structure and adhere to established coding standards and principles.