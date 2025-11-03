# File: docs/api_documentation.md

# API Documentation

## User Scenarios & Testing

1. **User Creates a New Teacher**:
   - User sends a request to create a new teacher with a name and email.
   - Application will create the teacher record and respond with the created teacher data.

   **Endpoint**: `POST /teachers`  
   **Request Body**: 
   ```json
   {
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```
   **Response**:
   ```json
   {
       "id": 1,
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```
   **Status Codes**:
   - 201 Created: Successful creation of teacher
   - 400 Bad Request: Invalid input (e.g., missing fields)

2. **User Retrieves Teacher Information**:
   - User requests to view a specific teacher's information using their unique identifier.
   - Application will return the teacher's data (name and email) in JSON format.

   **Endpoint**: `GET /teachers/{id}`  
   **Response**:
   ```json
   {
       "id": 1,
       "name": "John Doe",
       "email": "john.doe@example.com"
   }
   ```
   **Status Codes**:
   - 200 OK: Successfully retrieved teacher data
   - 404 Not Found: Teacher not found with the given ID

3. **User Handles Validation Errors for Teacher Creation**:
   - User attempts to create a teacher without providing required fields (name or email).
   - Application will respond with relevant validation error messages indicating the missing fields.

   **Example Scenario**: Sending a request without the 'name' field.
   **Response**:
   ```json
   {
       "error": {
           "code": "E001",
           "message": "Missing required field: name"
       }
   }
   ```
   **Status Codes**:
   - 400 Bad Request: Validation error due to missing fields

4. **User Updates Existing Teacher Information**:
   - User sends a request to update an existing teacher's name or email.
   - Application will correctly update the teacher's record and respond with the updated teacher data.

   **Endpoint**: `PUT /teachers/{id}`  
   **Request Body**: 
   ```json
   {
       "name": "Jane Doe",
       "email": "jane.doe@example.com"
   }
   ```
   **Response**:
   ```json
   {
       "id": 1,
       "name": "Jane Doe",
       "email": "jane.doe@example.com"
   }
   ```
   **Status Codes**:
   - 200 OK: Successfully updated teacher information
   - 404 Not Found: Teacher not found
   - 400 Bad Request: Invalid input (e.g., missing fields)

## Functional Requirements

1. **Create Teacher Entity**:
   - **Endpoint**: `POST /teachers`
   - Required fields:
     - `name` (string, required)
     - `email` (string, required)

2. **Retrieve Teacher Information**:
   - **Endpoint**: `GET /teachers/{id}`
   - Returns a teacher object with:
     - `id` (int)
     - `name` (string)
     - `email` (string)

3. **Validation**:
   - Ensure both `name` and `email` fields are provided and meet necessary format requirements (e.g., proper email format).
   - Return appropriate validation error messages for any missing or invalid fields during teacher creation.

4. **Database Migration**:
   - Update the database schema to add a new Teacher table.
   - Ensure no disruption to existing Student and Course data.

## Out of Scope
- User authentication or authorization for creating or modifying teacher records.