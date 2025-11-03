# README.md

# Project Documentation

## API Endpoints

### Create Teacher
- **Method**: POST
- **Endpoint**: `/teachers`
- **Request Body**:
  ```json
  {
    "name": "Jane Doe",
    "email": "jane.doe@example.com"
  }
  ```
- **Response**:
  - **201 Created**:
    ```json
    {
      "id": 1,
      "name": "Jane Doe",
      "email": "jane.doe@example.com"
    }
    ```

### Get All Teachers
- **Method**: GET
- **Endpoint**: `/teachers`
- **Response**:
  - **200 OK**:
    ```json
    [
      {
        "id": 1,
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
      }
    ]
    ```

### Update Teacher
- **Method**: PUT
- **Endpoint**: `/teachers/{id}`
- **Request Body**:
  ```json
  {
    "name": "Jane NewName",
    "email": "jane.new.email@example.com"
  }
  ```
- **Response**:
  - **200 OK**:
    ```json
    {
      "id": 1,
      "name": "Jane NewName",
      "email": "jane.new.email@example.com"
    }
    ```

### Delete Teacher
- **Method**: DELETE
- **Endpoint**: `/teachers/{id}`
- **Response**:
  - **204 No Content**: on successful deletion.

## User Scenarios
1. **Create a Teacher**: A user can create a new Teacher by providing a name and an email address.
2. **View Teachers**: A user can view a list of all Teachers stored in the system.
3. **Update Teacher Details**: A user can update the name or email of an existing Teacher.
4. **Delete a Teacher**: A user can remove a Teacher from the system.

## Functional Requirements
1. **Create Teacher**:
   - Endpoint: POST `/teachers`
   - Request: JSON object with `name` (string, required) and `email` (string, required).
   - Response: JSON object with a confirmation of the created Teacher, including the assigned Teacher ID.

2. **Get All Teachers**:
   - Endpoint: GET `/teachers`
   - Response: JSON array of Teacher objects.

3. **Update Teacher**:
   - Endpoint: PUT `/teachers/{id}`
   - Request: JSON object with optional `name` (string) and `email` (string).
   - Response: JSON object confirming the details have been updated.

4. **Delete Teacher**:
   - Endpoint: DELETE `/teachers/{id}`
   - Response: JSON object confirming the Teacher has been deleted.

5. **Database Migration**:
   - Create a new Teacher table with the following fields:
       - **id**: Unique identifier (auto-generated)
       - **name**: String (required)
       - **email**: String (required)
   - Ensure this migration preserves existing Student and Course data.