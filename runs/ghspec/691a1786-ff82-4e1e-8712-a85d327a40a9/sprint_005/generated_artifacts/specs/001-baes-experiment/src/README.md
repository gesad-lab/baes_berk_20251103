# README.md

# Project Name

This project provides an API for managing teachers, students, and courses. 

## API Documentation

### Endpoints

1. **Create Teacher**
   - **Method**: POST
   - **Endpoint**: `/teachers`
   - **Request Body**: 
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```
   - **Response**:
     - **201 Created**: Returns the newly created teacher details.
     - **Example Response**:
       ```json
       {
         "id": 1,
         "name": "John Doe",
         "email": "john.doe@example.com"
       }
       ```

2. **Retrieve Teacher Details**
   - **Method**: GET
   - **Endpoint**: `/teachers/{id}`
   - **Response**:
     - **200 OK**: Returns the teacher details.
     - **404 Not Found**: If the teacher does not exist.
     - **Example Response** (200 OK):
       ```json
       {
         "id": 1,
         "name": "John Doe",
         "email": "john.doe@example.com"
       }
       ```

3. **Update Teacher Information**
   - **Method**: PUT or PATCH
   - **Endpoint**: `/teachers/{id}`
   - **Request Body**: 
     ```json
     {
       "name": "Jane Doe",
       "email": "jane.doe@example.com"
     }
     ```
   - **Response**:
     - **200 OK**: Returns the updated teacher details.
     - **404 Not Found**: If the teacher does not exist.
     - **Example Response** (200 OK):
       ```json
       {
         "id": 1,
         "name": "Jane Doe",
         "email": "jane.doe@example.com"
       }
       ```

4. **Delete Teacher**
   - **Method**: DELETE
   - **Endpoint**: `/teachers/{id}`
   - **Response**:
     - **200 OK**: Returns confirmation of deletion.
     - **404 Not Found**: If the teacher does not exist.
     - **Example Response** (200 OK):
       ```json
       {
         "message": "Teacher deleted successfully."
       }
       ```

### Database Schema

The database includes a new **Teacher** table with the following fields:
- `id`: Integer, primary key.
- `name`: String, required.
- `email`: String, required.

### Database Migration

The migration process creates the new Teacher table while preserving existing data in the Student, Course, and any related tables. This ensures seamless integration with the current database structure.